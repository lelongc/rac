package com.group.blog.util;

import java.text.Normalizer;
import java.util.regex.Pattern;

public class SlugUtils {

    public static String generateSlug(String title) {
        if (title == null || title.trim().isEmpty()) {
            return "";
        }

        String slug = title.trim().toLowerCase();

        slug = Normalizer.normalize(slug, Normalizer.Form.NFD);
        Pattern pattern = Pattern.compile("\\p{InCombiningDiacriticalMarks}+");
        slug = pattern.matcher(slug).replaceAll("");

        slug = slug.replace("đ", "d");

        slug = slug.replaceAll("[^a-z0-9]+", "-");

        slug = slug.replaceAll("-+", "-");

        slug = slug.replaceAll("^-|-$", "");

        return slug;
    }
}
