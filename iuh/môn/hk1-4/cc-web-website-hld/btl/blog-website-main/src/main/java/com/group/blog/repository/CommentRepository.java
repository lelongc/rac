package com.group.blog.repository;

import com.group.blog.entity.Comment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;
import java.util.UUID;

@Repository
public interface CommentRepository extends JpaRepository<Comment, UUID> {
    long countByBlogId(UUID blogId);

    List<Comment> findByBlogIdAndParentIsNullOrderByCreatedAtDesc(UUID blogId);
}
