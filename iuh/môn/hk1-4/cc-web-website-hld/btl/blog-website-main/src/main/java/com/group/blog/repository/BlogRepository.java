package com.group.blog.repository;

import com.group.blog.entity.Blog;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface BlogRepository extends JpaRepository<Blog, UUID> {

    @Query("""
       SELECT b,COUNT(DISTINCT v.id),COUNT(DISTINCT l.id),COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog=b
       LEFT JOIN BlogView  v ON v.blog=b
       LEFT JOIN Comment  c ON c.blog=b
       WHERE b.draft=false
       GROUP BY b
       ORDER BY b.publishedAt DESC

    """)
    List<Object[]> findAllBlogsWithCounts();

    @Query("""
       SELECT b,COUNT(DISTINCT v.id),COUNT(DISTINCT l.id),COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog=b
       LEFT JOIN BlogView  v ON v.blog=b
       LEFT JOIN Comment  c ON c.blog=b
       WHERE b.category.id=:categoryId AND b.draft=false
       GROUP BY b
       ORDER BY b.publishedAt DESC

    """)
    List<Object[]> findBlogsByCategoryIdWithCounts(@Param("categoryId") UUID categoryId);

    @Query("""
       SELECT b,COUNT(DISTINCT v.id),COUNT(DISTINCT l.id),COUNT(DISTINCT c.id)
       FROM Blog b
       JOIN b.tags t
       LEFT JOIN BlogLike l ON l.blog=b
       LEFT JOIN BlogView  v ON v.blog=b
       LEFT JOIN Comment  c ON c.blog=b
       WHERE t.id=:tagId AND b.draft=false
       GROUP BY b
       ORDER BY b.publishedAt DESC

    """)
    List<Object[]> findBlogsByTagIdWithCounts(@Param("tagId") UUID tagId);

    @Query("""
       SELECT b,COUNT(DISTINCT v.id),COUNT(DISTINCT l.id),COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog=b
       LEFT JOIN BlogView  v ON v.blog=b
       LEFT JOIN Comment  c ON c.blog=b
       WHERE LOWER(b.title) LIKE TRIM(LOWER(CONCAT('%',:keyword,'%'))) AND b.draft=false
       GROUP BY b
       ORDER BY b.publishedAt DESC

    """)
    List<Object[]> searchBlogsByKeywordWithCounts(@Param("keyword") String keyword);

    List<Blog> findTop5ByTitleContainingIgnoreCaseAndDraftIsFalse(String title);

    @Query("""
       SELECT b,COUNT(DISTINCT v.id),COUNT(DISTINCT l.id),COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog=b
       LEFT JOIN BlogView  v ON v.blog=b
       LEFT JOIN Comment  c ON c.blog=b
       WHERE LOWER(b.title) LIKE TRIM(LOWER(CONCAT('%',:keyword,'%'))) AND b.category.id=:categoryId AND b.draft=false
       GROUP BY b
       ORDER BY b.publishedAt DESC

    """)
    List<Object[]> findByKeywordAndCategoryIdWithCounts(@Param("keyword") String keyword, @Param("categoryId") UUID categoryId);

    @Query("""
       SELECT b,COUNT(DISTINCT v.id),COUNT(DISTINCT l.id),COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog=b
       LEFT JOIN BlogView  v ON v.blog=b
       LEFT JOIN Comment  c ON c.blog=b
       WHERE b.author.username = :username
       GROUP BY b
       ORDER BY b.publishedAt DESC

    """)
    List<Object[]> findByAuthorUsernameWithCounts(@Param("username") String username);

    @Query("""
       SELECT b,COUNT(DISTINCT v.id),COUNT(DISTINCT l.id),COUNT(DISTINCT c.id)
       FROM Blog b
       LEFT JOIN BlogLike l ON l.blog=b
       LEFT JOIN BlogView  v ON v.blog=b
       LEFT JOIN Comment  c ON c.blog=b
       WHERE b.author.username = :username AND b.draft=false
       GROUP BY b
       ORDER BY b.publishedAt DESC

    """)
    List<Object[]> findPublishedByAuthorUsernameWithCounts(@Param("username") String username);

    List<Blog> findTop5ByDraftFalseOrderByCreatedAtDesc();

    long countByDraftFalse();
}
