package com.group.blog.config;

import com.group.blog.entity.Blog;
import com.group.blog.entity.Category;
import com.group.blog.entity.Tag;
import com.group.blog.entity.User;
import com.group.blog.enums.Role;
import com.group.blog.repository.BlogRepository;
import com.group.blog.repository.CategoryRepository;
import com.group.blog.repository.TagRepository;
import com.group.blog.repository.UserRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.time.LocalDateTime;
import java.util.HashSet;
import java.util.Set;

@Configuration
public class ApplicationInitConfig {
    private static final Logger log = LoggerFactory.getLogger(ApplicationInitConfig.class);

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Bean
    ApplicationRunner applicationRunner(
            UserRepository userRepository,
            CategoryRepository categoryRepository,
            TagRepository tagRepository,
            BlogRepository blogRepository
    ) {
        return args -> {
            if (userRepository.findByUsername("admin").isEmpty()) {
                // 1. Tạo tài khoản Admin
                Set<String> adminRoles = new HashSet<>();
                adminRoles.add(Role.ADMIN.name());
                adminRoles.add(Role.USER.name());

                User admin = User.builder()
                        .username("admin")
                        .email("admin@blog.com")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Quản trị viên hệ thống Blog Bleb")
                        .avatarUrl("https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=150")
                        .roles(adminRoles)
                        .build();
                userRepository.save(admin);

                // 2. Tạo tài khoản các thành viên nhóm
                Set<String> userRoles = new HashSet<>();
                userRoles.add(Role.USER.name());

                User duong = User.builder()
                        .username("duonghd")
                        .email("duong.24743991@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Hoàng Đại Dương - MSSV: 24743991")
                        .avatarUrl("https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(duong);

                User dung = User.builder()
                        .username("dungnt")
                        .email("dung.24000905@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Nguyễn Trung Dũng - MSSV: 24000905")
                        .avatarUrl("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(dung);

                User longMember = User.builder()
                        .username("longlt")
                        .email("long.23630851@iuh.edu.vn")
                        .password(passwordEncoder.encode("123456"))
                        .bio("Lê Thành Long - MSSV: 23630851")
                        .avatarUrl("https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=150")
                        .roles(userRoles)
                        .build();
                userRepository.save(longMember);

                // 3. Tạo Danh mục (Categories)
                Category catTech = categoryRepository.save(Category.builder().name("Technology").build());
                Category catDev = categoryRepository.save(Category.builder().name("Programming").build());
                Category catDesign = categoryRepository.save(Category.builder().name("Web Design").build());
                Category catLife = categoryRepository.save(Category.builder().name("Life & Tips").build());

                // 4. Tạo Thẻ (Tags)
                Tag tagJava = tagRepository.save(Tag.builder().name("Java").build());
                Tag tagSpring = tagRepository.save(Tag.builder().name("SpringBoot").build());
                Tag tagBootstrap = tagRepository.save(Tag.builder().name("Bootstrap").build());
                Tag tagThymeleaf = tagRepository.save(Tag.builder().name("Thymeleaf").build());
                Tag tagAI = tagRepository.save(Tag.builder().name("AI").build());

                // 5. Tạo các bài viết mẫu (Sample Blogs)
                Set<Tag> tags1 = new HashSet<>();
                tags1.add(tagSpring);
                tags1.add(tagJava);

                Blog blog1 = Blog.builder()
                        .title("Khám phá kiến trúc Spring Boot 3 và cơ chế In-Memory H2 Database")
                        .description("Tìm hiểu cách xây dựng ứng dụng Web hoàn chỉnh với Spring Boot 3, Hibernate JPA và giải pháp H2 Database nhúng không cần cài đặt MySQL.")
                        .content("Spring Boot là một trong những framework phổ biến nhất trong hệ sinh thái Java. Kết hợp với H2 In-memory Database giúp việc kiểm thử và triển khai diễn ra cực kỳ nhanh chóng và tiện lợi.")
                        .banner("https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800")
                        .draft(false)
                        .author(duong)
                        .category(catDev)
                        .tags(tags1)
                        .publishedAt(LocalDateTime.now())
                        .build();
                blogRepository.save(blog1);

                Set<Tag> tags2 = new HashSet<>();
                tags2.add(tagBootstrap);
                tags2.add(tagThymeleaf);

                Blog blog2 = Blog.builder()
                        .title("Thiết kế giao diện hiện đại với Bootstrap 5 & Thymeleaf View Engine")
                        .description("Tối ưu hóa trải nghiệm người dùng với hệ thống lưới Bootstrap 5 kết hợp cùng khả năng render mạnh mẽ từ Thymeleaf trên Spring Boot.")
                        .content("Bootstrap 5 mang đến bộ công cụ CSS mạnh mẽ, hỗ trợ responsive hoàn hảo trên mọi thiết bị di động và máy tính bảng.")
                        .banner("https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800")
                        .draft(false)
                        .author(dung)
                        .category(catDesign)
                        .tags(tags2)
                        .publishedAt(LocalDateTime.now().minusHours(2))
                        .build();
                blogRepository.save(blog2);

                Set<Tag> tags3 = new HashSet<>();
                tags3.add(tagAI);
                tags3.add(tagSpring);

                Blog blog3 = Blog.builder()
                        .title("Ứng dụng Trí tuệ Nhân tạo và Công nghệ Web hướng dữ liệu 2026")
                        .description("Tổng quan về xu hướng phát triển ứng dụng Web tương tác dữ liệu lớn và tích hợp trợ lý AI thông minh.")
                        .content("Trí tuệ nhân tạo đang làm thay đổi toàn diện cách thức các lập trình viên xây dựng và tối ưu hệ thống web hiện đại.")
                        .banner("https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800")
                        .draft(false)
                        .author(longMember)
                        .category(catTech)
                        .tags(tags3)
                        .publishedAt(LocalDateTime.now().minusDays(1))
                        .build();
                blogRepository.save(blog3);

                log.info("Initialized Sample Data Successfully: 4 Users, 4 Categories, 5 Tags, 3 Blogs!");
            }
        };
    }
}

