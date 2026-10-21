package com.group.blog.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class ViewController {

    @GetMapping({"/", "/home", "/home-page.html"})
    public String homePage() {
        return "public/home-page";
    }

    @GetMapping({"/login", "/login.html"})
    public String loginPage() {
        return "public/login";
    }

    @GetMapping({"/register", "/register.html"})
    public String registerPage() {
        return "public/register";
    }

    @GetMapping({"/forgot-password", "/forgot-password.html"})
    public String forgotPasswordPage() {
        return "public/forgot-password";
    }

    @GetMapping({"/post", "/post.html"})
    public String postDetailPage() {
        return "public/post";
    }

    @GetMapping({"/blog-editor", "/blog-editor.html"})
    public String blogEditorPage() {
        return "public/blog-editor";
    }

    @GetMapping({"/user-profile", "/user-profile.html"})
    public String userProfilePage() {
        return "public/user-profile";
    }

    @GetMapping({"/edit-profile", "/edit-profile.html"})
    public String editProfilePage() {
        return "public/edit-profile";
    }

    @GetMapping({"/saved-blogs", "/saved-blogs.html"})
    public String savedBlogsPage() {
        return "public/saved-blogs";
    }

    @GetMapping({"/notifications", "/notifications.html"})
    public String notificationsPage() {
        return "public/notifications";
    }

    @GetMapping({"/manage-blogs", "/manage-blogs.html", "/Manage-Blogs.html"})
    public String manageBlogsPage() {
        return "public/Manage-Blogs";
    }

    @GetMapping({"/change-password", "/change-password.html"})
    public String changePasswordPage() {
        return "public/change-password";
    }

    @GetMapping({"/admin", "/admin/dashboard", "/admin/dashboard.html"})
    public String adminDashboardPage() {
        return "admin/dashboard";
    }

    @GetMapping({"/admin/posts", "/admin/posts.html"})
    public String adminPostsPage() {
        return "admin/posts";
    }

    @GetMapping({"/admin/users", "/admin/users.html"})
    public String adminUsersPage() {
        return "admin/users";
    }

    @GetMapping({"/admin/categories-tags", "/admin/categories-tags.html"})
    public String adminCategoriesTagsPage() {
        return "admin/categories-tags";
    }
}
