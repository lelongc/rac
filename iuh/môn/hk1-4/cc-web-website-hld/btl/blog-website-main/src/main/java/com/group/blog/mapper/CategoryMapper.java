package com.group.blog.mapper;

import com.group.blog.dto.request.CategoryRequest;
import com.group.blog.dto.response.CategoryResponse;
import com.group.blog.entity.Category;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;

@Mapper(componentModel = "spring")
public interface CategoryMapper {
    @Mapping(target = "blogs", ignore = true)
    Category toCategory(CategoryRequest request);

    CategoryResponse toCategoryResponse(Category category);
}

