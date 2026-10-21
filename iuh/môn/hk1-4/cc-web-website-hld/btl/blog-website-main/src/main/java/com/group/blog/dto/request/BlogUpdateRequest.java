package com.group.blog.dto.request;

import lombok.*;
import lombok.experimental.FieldDefaults;

import java.util.Set;
import java.util.UUID;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
public class BlogUpdateRequest {

    String title;
    String banner;
    String description;
    String content;

    Boolean draft;

    UUID categoryId;
    Set<String> tags;
}
