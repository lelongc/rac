package com.group.blog.mapper;

import com.group.blog.dto.request.BlogCreationRequest;
import com.group.blog.dto.request.BlogUpdateRequest;
import com.group.blog.dto.response.BlogResponse;
import com.group.blog.entity.Blog;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;
import org.mapstruct.MappingTarget;

@Mapper(componentModel = "spring")
public interface BlogMapper {

    @Mapping(target = "category", ignore = true)
    @Mapping(target = "tags", ignore = true)
    @Mapping(target = "author", ignore = true)
    Blog toBlog(BlogCreationRequest request);

    BlogResponse toBlogResponse(Blog blog);

    @Mapping(target = "category", ignore = true)
    @Mapping(target = "tags", ignore = true)
    void updateBlog(@MappingTarget Blog blog, BlogUpdateRequest request);
}
