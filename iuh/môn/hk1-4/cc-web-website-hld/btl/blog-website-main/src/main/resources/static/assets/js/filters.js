var CATEGORIES = [];
var TAGS = [];
var TOTAL_POSTS = 0;

function fetchAndRenderFilters() {

    callApi('/categories', 'GET').done(function(res) {
        CATEGORIES = res.result || res;

        TOTAL_POSTS = 0;
        $.each(CATEGORIES, function(_, c) {
            TOTAL_POSTS += (c.postCount || 0);
        });

        renderCatTabs();
    });

    callApi('/tags', 'GET').done(function(res) {
        TAGS = res.result || res;
        renderTagChips();
    });
}

function updateUrlWithFilters() {
    let newUrl = '/';
    let params = new URLSearchParams();

    if (S.keyword) params.append('q', S.keyword);
    if (S.cat) params.append('cat', S.cat);
    if (S.tag) params.append('tag', S.tag);

    if (params.toString() !== '') {
        newUrl += '?' + params.toString();
    }
    window.history.pushState({}, '', newUrl);
}

function renderCatTabs() {
    var $el = $('#cat-tabs').empty();

    if (!CATEGORIES || CATEGORIES.length === 0) {
        $el.append('<span class="text-muted" style="font-size: 0.85rem;">Đang tải bộ lọc...</span>');
        return;
    }

    $el.append(
        $('<button class="cat-btn' + (!S.cat ? ' on' : '') + '">').html(
            'All Posts <span style="font-size:.68rem;opacity:.65;margin-left:.25rem;">(' + TOTAL_POSTS + ')</span>'
        ).on('click', function(){
            S.cat = null;

            updateUrlWithFilters();

            renderCatTabs();
            if (typeof renderSbCategories === 'function') renderSbCategories();
            if (typeof renderPosts === 'function') renderPosts();
        })
    );

    $.each(CATEGORIES, function(_, c){
        $el.append(
            $('<button class="cat-btn' + (S.cat === c.id ? ' on' : '') + '">').html(
                c.name + '<span style="font-size:.68rem;opacity:.65;margin-left:.28rem;">(' + (c.postCount || 0) + ')</span>'
            ).on('click', function(){
                S.cat = (S.cat === c.id) ? null : c.id;

                updateUrlWithFilters();

                renderCatTabs();
                if (typeof renderSbCategories === 'function') renderSbCategories();
                if (typeof renderPosts === 'function') renderPosts();
            })
        );
    });
}

function renderTagChips() {
    var $el = $('#tag-chips').empty();

    if (!TAGS || TAGS.length === 0) {
        $el.append('<span class="text-muted" style="font-size: 0.85rem;">Đang tải thẻ...</span>');
        return;
    }

    $.each(TAGS, function(_, t){
        $el.append(
            $('<button class="tag-chip' + (S.tag === t.id ? ' on' : '') + '">').html(
                '#' + t.name +
                '<span style="font-size:.65rem;opacity:.6;margin-left:.2rem;">(' + (t.postCount || 0) + ')</span>'
            ).on('click', function(){
                S.tag = (S.tag === t.id) ? null : t.id;

                updateUrlWithFilters();

                renderTagChips();

                if (typeof renderSbTags === 'function') renderSbTags();

                if (typeof renderPosts === 'function') renderPosts();
            })
        );
    });
}
