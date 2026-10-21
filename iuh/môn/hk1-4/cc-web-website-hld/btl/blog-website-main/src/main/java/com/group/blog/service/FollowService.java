package com.group.blog.service;

import com.group.blog.dto.response.UserResponse;
import com.group.blog.entity.User;
import com.group.blog.entity.UserFollow;
import com.group.blog.exception.AppException;
import com.group.blog.exception.ErrorCode;
import com.group.blog.mapper.UserMapper;
import com.group.blog.repository.UserFollowRepository;
import com.group.blog.repository.UserRepository;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class FollowService {
    NotificationService notificationService;
    UserRepository userRepository;
    UserFollowRepository userFollowRepository;
    UserMapper userMapper;

    @Transactional
    public void toggleFollow(String targetUsername) {
        String currentUsername = SecurityContextHolder.getContext().getAuthentication().getName();

        if (currentUsername.equals(targetUsername)) {
            throw new RuntimeException("Bạn không thể tự theo dõi chính mình!");
        }

        User follower = userRepository.findByUsername(currentUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));
        User following = userRepository.findByUsername(targetUsername)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        Optional<UserFollow> existingFollow = userFollowRepository.findByFollowerAndFollowing(follower, following);

        if (existingFollow.isPresent()) {
            userFollowRepository.delete(existingFollow.get());
        } else {
            UserFollow newFollow = UserFollow.builder().follower(follower).following(following).build();
            userFollowRepository.save(newFollow);
            notificationService.createNotification(
                    following,
                    "@" + currentUsername + " started following you.",
                    "user-profile.html?user=" + currentUsername,
                    "FOLLOW"
            );
        }

    }

    public List<UserResponse> getFollowers(String username) {
        User targetUser = userRepository.findByUsername(username)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        return userFollowRepository.findByFollowingOrderByCreatedAtDesc(targetUser)
                .stream()
                .map(uf -> enrichUserResponse(uf.getFollower()))
                .toList();
    }

    public List<UserResponse> getFollowing(String username) {
        User targetUser = userRepository.findByUsername(username)
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        return userFollowRepository.findByFollowerOrderByCreatedAtDesc(targetUser)
                .stream()
                .map(uf -> enrichUserResponse(uf.getFollowing()))
                .toList();
    }

    public UserResponse enrichUserResponse(User user) {
        UserResponse response = userMapper.toUserResponse(user);

        response.setTotalFollowers(userFollowRepository.countByFollowing(user));
        response.setTotalFollowing(userFollowRepository.countByFollower(user));

        var auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth != null && auth.isAuthenticated() && !auth.getName().equals("anonymousUser")) {
            boolean isFollowed = userFollowRepository.existsByFollowerUsernameAndFollowing(auth.getName(), user);
            response.setFollowedByCurrentUser(isFollowed);
        } else {
            response.setFollowedByCurrentUser(false);
        }

        return response;
    }
}
