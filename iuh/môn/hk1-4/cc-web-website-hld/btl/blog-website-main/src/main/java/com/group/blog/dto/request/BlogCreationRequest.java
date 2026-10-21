package com.group.blog.dto.request;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.util.Set;
import java.util.UUID;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)

public class BlogCreationRequest {
    String title;
    String banner;
    String description;
    String content;
    boolean draft;
    UUID categoryId;
    Set<String> tags;
}
