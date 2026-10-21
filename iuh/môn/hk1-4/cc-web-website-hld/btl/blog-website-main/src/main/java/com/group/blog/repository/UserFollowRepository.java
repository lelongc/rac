package com.group.blog.repository;

import com.group.blog.entity.User;
import com.group.blog.entity.UserFollow;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface UserFollowRepository extends JpaRepository<UserFollow, UUID> {

    long countByFollowing(User following);

    long countByFollower(User follower);

    Optional<UserFollow> findByFollowerAndFollowing(User follower, User following);

    boolean existsByFollowerUsernameAndFollowing(String followerUsername, User following);

    List<UserFollow> findByFollowingOrderByCreatedAtDesc(User following);

    List<UserFollow> findByFollowerOrderByCreatedAtDesc(User follower);
}
