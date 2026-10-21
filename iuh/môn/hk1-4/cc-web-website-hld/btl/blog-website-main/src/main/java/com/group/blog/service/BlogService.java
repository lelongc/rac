package com.group.blog.service;

import com.group.blog.dto.request.BlogCreationRequest;
import com.group.blog.dto.request.BlogUpdateRequest;
import com.group.blog.dto.response.BlogResponse;
import com.group.blog.dto.response.BlogSuggestionResponse;
import com.group.blog.entity.*;
import com.group.blog.exception.AppException;
import com.group.blog.exception.ErrorCode;
import com.group.blog.mapper.BlogMapper;
import com.group.blog.repository.*;
import com.group.blog.util.SlugUtils;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.UUID;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class BlogService {

    BlogRepository blogRepository;
    UserRepository userRepository;
    CategoryRepository categoryRepository;
    TagRepository tagRepository;
    BlogMapper blogMapper;

    BlogViewRepository blogViewRepository;
    BlogLikeRepository blogLikeRepository;
    CommentRepository commentRepository;

    BookmarkRepository bookmarkRepository;
    @Transactional
    public BlogResponse createBlog(BlogCreationRequest request) {
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();
        User author = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        Category category = null;
        if (request.getCategoryId() != null) {
            category = categoryRepository.findById(request.getCategoryId())
                    .orElseThrow(() -> new AppException(ErrorCode.CATEGORY_NOT_FOUND));
        }

        Blog blog = blogMapper.toBlog(request);
        blog.setAuthor(author);
        blog.setCategory(category);

        if (request.getTags() != null && !request.getTags().isEmpty()) {
            Set<Tag> finalTags = new HashSet<>();
            for (String tagName : request.getTags()) {
                Tag tag = tagRepository.findByName(tagName)
                        .orElseGet(() -> {
                            Tag newTag = new Tag();
                            newTag.setName(tagName);
                            return tagRepository.save(newTag);
                        });
                finalTags.add(tag);
            }
            blog.setTags(finalTags);
        }
        return enrichBlogResponse(blogRepository.save(blog));
    }

    @Transactional
    public BlogResponse updateBlog(UUID id, BlogUpdateRequest request) {
        Blog blog = blogRepository.findById(id)
                .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));

        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();
        if (!blog.getAuthor().getUsername().equals(currentUsername)) {
            throw new AppException(ErrorCode.UNAUTHORIZED);
        }

        if (request.getCategoryId() != null && (blog.getCategory() == null || !request.getCategoryId().equals(blog.getCategory().getId()))) {
            Category newCategory = categoryRepository.findById(request.getCategoryId())
                    .orElseThrow(() -> new AppException(ErrorCode.CATEGORY_NOT_FOUND));
            blog.setCategory(newCategory);
        }

        if(request.getTitle() != null) blog.setTitle(request.getTitle());
        if(request.getDescription() != null) blog.setDescription(request.getDescription());

        boolean isRequestingSaveDraft = Boolean.TRUE.equals(request.getDraft());

        if (isRequestingSaveDraft) {
            if (blog.isDraft()) {
                if(request.getContent() != null) blog.setContent(request.getContent());
                if(request.getBanner() != null) blog.setBanner(request.getBanner());

            } else {
                if(request.getContent() != null) blog.setDraftContent(request.getContent());
                if(request.getBanner() != null) blog.setDraftBanner(request.getBanner());
            }

        } else {
            if(request.getContent() != null) blog.setContent(request.getContent());
            if(request.getBanner() != null) blog.setBanner(request.getBanner());

            blog.setDraftContent(null);
            blog.setDraftBanner(null);

            blog.setDraft(false);

            if (blog.getPublishedAt() == null) {
                blog.setPublishedAt(LocalDateTime.now());
            }
        }

        if (request.getTags() != null) {
            Set<Tag> finalTags = new HashSet<>();
            for (String tagName : request.getTags()) {
                Tag tag = tagRepository.findByName(tagName)
                        .orElseGet(() -> {
                            Tag newTag = new Tag();
                            newTag.setName(tagName);
                            return tagRepository.save(newTag);
                        });
                finalTags.add(tag);
            }
            blog.setTags(finalTags);
        }

        return enrichBlogResponse(blogRepository.save(blog));
    }

    @Transactional
    public BlogResponse getBlogById(UUID id) {
        Blog blog = blogRepository.findById(id)
                .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));

        BlogView view = new BlogView();
        view.setBlog(blog);
        blogViewRepository.save(view);

        return enrichBlogResponse(blog);
    }

    public List<BlogResponse> getAllBlogs() {
        List<Object[]> results = blogRepository.findAllBlogsWithCounts();

        return results.stream().map(row -> {
            Blog blog = (Blog) row[0];
            long viewCount = (long) row[1];
            long likeCount = (long) row[2];
            long commentCount = (long) row[3];

            BlogResponse response = blogMapper.toBlogResponse(blog);

            String generatedSlug = SlugUtils.generateSlug(blog.getTitle()) + "-" + blog.getId().toString();
            response.setSlug(generatedSlug);

            response.setTotalReads((int) viewCount);
            response.setTotalLikes((int) likeCount);
            response.setTotalComments((int) commentCount);

            return response;
        }).toList();
    }

    @Transactional
    public void deleteBlog(UUID id) {
        Blog blog = blogRepository.findById(id)
                .orElseThrow(() -> new AppException(ErrorCode.BLOG_NOT_FOUND));

        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();

        boolean isAuthor = blog.getAuthor().getUsername().equals(currentUsername);
        boolean isAdmin = context.getAuthentication().getAuthorities().stream()
                .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"));

        if (!isAuthor && !isAdmin) {
            throw new AppException(ErrorCode.UNAUTHORIZED);
        }

        blogRepository.deleteById(id);
    }

    public List<BlogResponse> getMyBlogs() {
        var context = SecurityContextHolder.getContext();
        String currentUsername = context.getAuthentication().getName();

        List<Object[]> results = blogRepository.findByAuthorUsernameWithCounts(currentUsername);

        return results.stream().map(this::mapRowToBlogResponse).toList();
    }

    public List<BlogResponse> getBlogsByCategory(UUID categoryId) {
        List<Object[]> results = blogRepository.findBlogsByCategoryIdWithCounts(categoryId);
        return results.stream().map(this::mapRowToBlogResponse).toList();
    }

    public List<BlogResponse> getBlogsByTag(UUID tagId) {
        List<Object[]> results = blogRepository.findBlogsByTagIdWithCounts(tagId);
        return results.stream().map(this::mapRowToBlogResponse).toList();
    }

    public List<BlogResponse> searchBlogs(String keyword) {
        List<Object[]> results = blogRepository.searchBlogsByKeywordWithCounts(keyword);
        return results.stream().map(this::mapRowToBlogResponse).toList();
    }

    public List<BlogSuggestionResponse> getSearchSuggestions(String keyword) {
        return blogRepository.findTop5ByTitleContainingIgnoreCaseAndDraftIsFalse(keyword)
                .stream().map(blog -> BlogSuggestionResponse.builder()
                        .id(blog.getId())
                        .title(blog.getTitle())
                        .slug(SlugUtils.generateSlug(blog.getTitle()) + "-" + blog.getId())
                        .authorName(blog.getAuthor() != null ? blog.getAuthor().getUsername() : "Anonymous")
                        .categoryName(blog.getCategory() != null ? blog.getCategory().getName() : "Khác")

                        .build())
                .toList();
    }

    public List<BlogResponse> filterBlogs(String keyword, UUID categoryId) {
        List<Object[]> results;

        boolean hasKeyword = (keyword != null && !keyword.trim().isEmpty());
        boolean hasCategory = (categoryId != null);

        if (hasKeyword && hasCategory) {
            results = blogRepository.findByKeywordAndCategoryIdWithCounts(keyword, categoryId);
        } else if (hasKeyword) {
            results = blogRepository.searchBlogsByKeywordWithCounts(keyword);
        } else if (hasCategory) {
            results = blogRepository.findBlogsByCategoryIdWithCounts(categoryId);
        } else {
            results = blogRepository.findAllBlogsWithCounts();
        }

        return results.stream().map(this::mapRowToBlogResponse).toList();
    }

    private BlogResponse mapRowToBlogResponse(Object[] row) {
        Blog blog = (Blog) row[0];
        long viewCount = (long) row[1];
        long likeCount = (long) row[2];
        long commentCount = (long) row[3];

        BlogResponse response = blogMapper.toBlogResponse(blog);
        response.setSlug(SlugUtils.generateSlug(blog.getTitle()) + "-" + blog.getId());
        response.setTotalReads((int) viewCount);
        response.setTotalLikes((int) likeCount);
        response.setTotalComments((int) commentCount);
        return response;
    }

    private BlogResponse enrichBlogResponse(Blog blog) {
        BlogResponse response = blogMapper.toBlogResponse(blog);

        String generatedSlug = SlugUtils.generateSlug(blog.getTitle()) + "-" + blog.getId().toString();
        response.setSlug(generatedSlug);

        response.setTotalReads((int) blogViewRepository.countByBlogId(blog.getId()));
        response.setTotalLikes((int) blogLikeRepository.countByBlogId(blog.getId()));
        response.setTotalComments((int) commentRepository.countByBlogId(blog.getId()));

        var authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication != null && authentication.isAuthenticated() && !authentication.getName().equals("anonymousUser")) {
            String currentUsername = authentication.getName();
            boolean isLiked = blogLikeRepository.existsByBlogIdAndUserUsername(blog.getId(), currentUsername);
            boolean isBookmarked = bookmarkRepository.existsByBlogIdAndUserUsername(blog.getId(), currentUsername);
            response.setLikedByCurrentUser(isLiked);
            response.setBookmarkedByCurrentUser(isBookmarked);
        } else {
            response.setLikedByCurrentUser(false);
            response.setBookmarkedByCurrentUser(false);
        }
        return response;
    }

    public List<BlogResponse> getPublishedBlogsByUsername(String username) {
        List<Object[]> results = blogRepository.findPublishedByAuthorUsernameWithCounts(username);
        return results.stream().map(this::mapRowToBlogResponse).toList();
    }

    public long countTotalBlogs() {
        return blogRepository.count();
    }

    public List<BlogResponse> getRecentBlogs(int limit) {
        return blogRepository.findTop5ByDraftFalseOrderByCreatedAtDesc().stream()
                .map(blogMapper::toBlogResponse)
                .toList();
    }
}
