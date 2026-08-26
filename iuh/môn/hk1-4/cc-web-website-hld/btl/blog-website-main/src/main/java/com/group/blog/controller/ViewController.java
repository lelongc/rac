package com.group.blog.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ViewController {

    // 1. Trang chu (Home Page)
    @GetMapping({"/", "/home", "/home-page.html"})
    public String homePage() {
        return "public/home-page";
    }

    // 2. Trang Dang Nhap (Login)
    @GetMapping({"/login", "/login.html"})
    public String loginPage() {
        return "public/login";
    }

    // 3. Trang Dang Ky (Register)
    @GetMapping({"/register", "/register.html"})
    public String registerPage() {
        return "public/register";
    }

    // 4. Trang Quen Mat Khau (Forgot Password)
    @GetMapping({"/forgot-password", "/forgot-password.html"})
    public String forgotPasswordPage() {
        return "public/forgot-password";
    }

    // 5. Trang Chi Tiet Bai Viet (Post Detail)
    @GetMapping({"/post", "/post.html"})
    public String postDetailPage() {
        return "public/post";
    }

    // 6. Trang Soan Thao Bai Viet (Blog Editor)
    @GetMapping({"/blog-editor", "/blog-editor.html"})
    public String blogEditorPage() {
        return "public/blog-editor";
    }

    // 7. Trang Ho So Nguoi Dung (User Profile)
    @GetMapping({"/user-profile", "/user-profile.html"})
    public String userProfilePage() {
        return "public/user-profile";
    }

    // 8. Trang Chinh Sua Ho So (Edit Profile)
    @GetMapping({"/edit-profile", "/edit-profile.html"})
    public String editProfilePage() {
        return "public/edit-profile";
    }

    // 9. Trang Bai Viet Da Luu (Saved Blogs)
    @GetMapping({"/saved-blogs", "/saved-blogs.html"})
    public String savedBlogsPage() {
        return "public/saved-blogs";
    }

    // 10. Trang Thong Bao (Notifications)
    @GetMapping({"/notifications", "/notifications.html"})
    public String notificationsPage() {
        return "public/notifications";
    }

    // 11. Trang Quan Ly Bai Viet Cua Toi (Manage Blogs)
    @GetMapping({"/manage-blogs", "/Manage-Blogs.html"})
    public String manageBlogsPage() {
        return "public/Manage-Blogs";
    }
}
