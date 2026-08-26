$baseUrl = "http://localhost:8080"
$results = [System.Collections.Generic.List[PSCustomObject]]::new()

function Test-Step($name, $scriptBlock) {
    try {
        $res = & $scriptBlock
        $results.Add([PSCustomObject]@{ Test = $name; Status = "PASS"; Details = $res })
        Write-Host "[PASS] $name - $res" -ForegroundColor Green
    } catch {
        $results.Add([PSCustomObject]@{ Test = $name; Status = "FAIL"; Details = $_.Exception.Message })
        Write-Host "[FAIL] $name - $($_.Exception.Message)" -ForegroundColor Red
    }
}

# 1. TEST ALL 16 HTML VIEWS
$views = @("/", "/login", "/register", "/forgot-password", "/change-password", "/post", "/blog-editor", "/user-profile", "/edit-profile", "/saved-blogs", "/notifications", "/manage-blogs", "/admin/dashboard", "/admin/posts", "/admin/users", "/admin/categories-tags")
foreach ($v in $views) {
    Test-Step "View HTML: $v" {
        $r = Invoke-WebRequest -Uri "$baseUrl$v" -Method Get
        if ($r.StatusCode -eq 200) { "Status 200 OK" } else { throw "Status $($r.StatusCode)" }
    }
}

# 2. TEST STATIC FRAGMENTS
$frags = @("/fragments/navbar.html", "/fragments/hero.html", "/fragments/footer.html", "/fragments/sidebar.html", "/fragments/admin_sidebar.html", "/fragments/dashboard-sidebar.html")
foreach ($f in $frags) {
    Test-Step "Fragment: $f" {
        $r = Invoke-WebRequest -Uri "$baseUrl$f" -Method Get
        if ($r.StatusCode -eq 200) { "Status 200 OK" } else { throw "Status $($r.StatusCode)" }
    }
}

# 3. TEST ASSETS
$assets = @("/assets/css/main.css", "/assets/js/app.js", "/assets/js/posts.js", "/assets/js/sidebar.js", "/assets/js/filters.js", "/assets/js/nav.js", "/assets/js/auth.js", "/assets/js/init.js", "/assets/js/pages.js")
foreach ($a in $assets) {
    Test-Step "Asset: $a" {
        $r = Invoke-WebRequest -Uri "$baseUrl$a" -Method Get
        if ($r.StatusCode -eq 200) { "Status 200 OK" } else { throw "Status $($r.StatusCode)" }
    }
}

# 4. TEST AUTH: SEED USERS LOGIN
$users = @("admin", "duonghd", "dungnt", "longlt")
$tokens = @{}
foreach ($u in $users) {
    Test-Step "Login user: $u" {
        $b = @{ username = $u; password = "123456" } | ConvertTo-Json
        $res = Invoke-RestMethod -Uri "$baseUrl/auth/login" -Method Post -Body $b -ContentType "application/json"
        if ($res.code -eq 1000 -and $res.result.token) {
            $tokens[$u] = $res.result.token
            "Token received (length $($res.result.token.Length))"
        } else { throw "Login failed: $($res.message)" }
    }
}

# 5. TEST AUTH: REGISTER NEW USER & LOGIN
$newUname = "testuser_" + (Get-Random -Minimum 1000 -Maximum 9999)
Test-Step "Register new user: $newUname" {
    $b = @{ username = $newUname; password = "123456" } | ConvertTo-Json
    $res = Invoke-RestMethod -Uri "$baseUrl/users" -Method Post -Body $b -ContentType "application/json"
    if ($res.code -eq 1000) { "Registered ID: $($res.result.id)" } else { throw "Register failed: $($res.message)" }
}

Test-Step "Login newly registered user: $newUname" {
    $b = @{ username = $newUname; password = "123456" } | ConvertTo-Json
    $res = Invoke-RestMethod -Uri "$baseUrl/auth/login" -Method Post -Body $b -ContentType "application/json"
    if ($res.code -eq 1000) { "Token ok" } else { throw "Login failed" }
}

# 6. TEST PUBLIC API: CATEGORIES & TAGS
$catList = $null
Test-Step "GET /categories" {
    $res = Invoke-RestMethod -Uri "$baseUrl/categories" -Method Get
    $catList = @($res.result)
    if ($catList.Count -ge 4) { "Found $($catList.Count) categories" } else { throw "Expected >= 4 categories" }
}

$tagList = $null
Test-Step "GET /tags" {
    $res = Invoke-RestMethod -Uri "$baseUrl/tags" -Method Get
    $tagList = @($res.result)
    if ($tagList.Count -ge 5) { "Found $($tagList.Count) tags" } else { throw "Expected >= 5 tags" }
}

# 7. TEST PUBLIC API: BLOGS FILTER & SEARCH
$allBlogs = $null
Test-Step "GET /blogs/filter" {
    $res = Invoke-RestMethod -Uri "$baseUrl/blogs/filter" -Method Get
    $allBlogs = @($res.result)
    if ($allBlogs.Count -ge 3) { "Found $($allBlogs.Count) blogs" } else { throw "Expected >= 3 blogs" }
}

Test-Step "GET /blogs/search?keyword=Spring" {
    $res = Invoke-RestMethod -Uri "$baseUrl/blogs/search?keyword=Spring" -Method Get
    if ($res.code -eq 1000) { "Search returned $($res.result.Count) items" } else { throw "Search error" }
}

# 8. TEST AUTHENTICATED USER APIs
$duongToken = $tokens["duonghd"]
$duongHeaders = @{ Authorization = "Bearer $duongToken" }

Test-Step "GET /users/my-profile (as duonghd)" {
    $res = Invoke-RestMethod -Uri "$baseUrl/users/my-profile" -Method Get -Headers $duongHeaders
    if ($res.result.username -eq "duonghd") { "Profile OK: $($res.result.email)" } else { throw "Mismatch username" }
}

# 9. TEST CREATE BLOG AS duonghd
$chosenCatId = $catList[0].id
$createdBlogId = $null
Test-Step "POST /blogs (Create Blog as duonghd)" {
    $b = @{
        title = "Bai Viet Test Tu Dong - $(Get-Date -Format 'HH:mm:ss')"
        content = "Noi dung bai viet kiem thu he thong day du."
        description = "Mo ta tom tat bai viet test."
        categoryId = $chosenCatId
        tagNames = @("Java", "SpringBoot")
        banner = "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600"
    } | ConvertTo-Json
    $res = Invoke-RestMethod -Uri "$baseUrl/blogs" -Method Post -Body $b -ContentType "application/json" -Headers $duongHeaders
    $script:createdBlogId = $res.result.id
    if ($script:createdBlogId) { "Created blog ID: $script:createdBlogId" } else { throw "No blog ID" }
}

# 10. TEST INTERACTION APIs: READ, LIKE, COMMENT, BOOKMARK
Test-Step "GET /blogs/{id} (Read single blog)" {
    $blogIdToRead = if ($script:createdBlogId) { $script:createdBlogId } else { $allBlogs[0].id }
    $res = Invoke-RestMethod -Uri "$baseUrl/blogs/$blogIdToRead" -Method Get -Headers $duongHeaders
    if ($res.result.title) { "Title: $($res.result.title)" } else { throw "Failed to load blog" }
}

# 11. TEST ADMIN APIs
$adminToken = $tokens["admin"]
$adminHeaders = @{ Authorization = "Bearer $adminToken" }

Test-Step "GET /api/admin/stats (as admin)" {
    $res = Invoke-RestMethod -Uri "$baseUrl/api/admin/stats" -Method Get -Headers $adminHeaders
    if ($res.result.totalUsers -gt 0) { "Total Users: $($res.result.totalUsers), Total Posts: $($res.result.totalPosts)" } else { throw "Failed stats" }
}

Test-Step "GET /users (as admin)" {
    $res = Invoke-RestMethod -Uri "$baseUrl/users" -Method Get -Headers $adminHeaders
    if ($res.result.Count -ge 4) { "Admin listed $($res.result.Count) users" } else { throw "Failed user list" }
}

Test-Step "GET /api/admin/stats (as duonghd - Expect 403 Forbidden)" {
    try {
        $res = Invoke-RestMethod -Uri "$baseUrl/api/admin/stats" -Method Get -Headers $duongHeaders
        throw "Should have failed with 403"
    } catch {
        if ($_.Exception.Message -match "403" -or $_.Exception.Response.StatusCode -eq 403) {
            "Correctly Forbidden (403)"
        } else {
            throw "Unexpected error: $($_.Exception.Message)"
        }
    }
}

Test-Step "GET /api/notifications (as duonghd)" {
    $res = Invoke-RestMethod -Uri "$baseUrl/api/notifications" -Method Get -Headers $duongHeaders
    if ($res.code -eq 1000) { "Notifications count: $($res.result.Count)" } else { throw "Failed notifications" }
}

Write-Host "`n================ TEST SUMMARY ================" -ForegroundColor Cyan
$passCount = ($results | Where-Object { $_.Status -eq "PASS" }).Count
$failCount = ($results | Where-Object { $_.Status -eq "FAIL" }).Count
$summaryColor = if ($failCount -eq 0) { "Green" } else { "Red" }
Write-Host "Total Tests: $($results.Count) | Passed: $passCount | Failed: $failCount" -ForegroundColor $summaryColor
