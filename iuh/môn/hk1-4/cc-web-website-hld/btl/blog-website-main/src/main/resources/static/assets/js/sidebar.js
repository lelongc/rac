function renderSbCategories() {
    var $el = $('#sb-categories');

    $el.html('<div class="text-muted py-2" style="font-size: 0.85rem;">Đang tải chủ đề...</div>');

    callApi('/categories', 'GET').done(function(res) {
        $el.empty();
        var catsList = res.result || res;

        $.each(catsList, function(_, c){
            var isActive = (S.cat === c.id) ? ' active' : '';

            var btnHtml = c.name + '<span style="opacity: 0.6; font-size: 0.75rem; margin-left: 5px; font-family: Inter, sans-serif;">(' + (c.postCount || 0) + ')</span>';

            var $btn = $('<a href="javascript:void(0)" class="cat-pill' + isActive + '">')
                .html(btnHtml)
                .on('click', function(e){
                    e.preventDefault();

                    S.cat = (S.cat === c.id) ? null : c.id;

                    let newUrl = '/';
                    let params = new URLSearchParams();

                    if (S.keyword) params.append('q', S.keyword);
                    if (S.cat) params.append('cat', S.cat);

                    if (params.toString() !== '') {
                        newUrl += '?' + params.toString();
                    }
                    window.history.pushState({}, '', newUrl);

                    renderSbCategories();

                    if (typeof renderCatTabs === 'function') renderCatTabs();

                    if (typeof renderPosts === 'function') renderPosts();
                });

            $el.append($btn);
        });
    });
}

function renderSbTrending() {
    var $el = $('#sb-trending');

    $el.html('<div class="text-muted py-3" style="font-size: 0.85rem;">Đang tải xu hướng...</div>');

    callApi('/blogs', 'GET').done(function(res) {
        $el.empty();
        var allPosts = res.result || res;

        var trendingPosts = allPosts.sort(function(a, b) {
            return (b.totalReads || 0) - (a.totalReads || 0);
        }).slice(0, 5);

        $.each(trendingPosts, function(i, p){
            var catName = p.category ? p.category.name : 'Chưa phân loại';

            var plainTextContent = excerpt(p.content, 99999);
            var readingTime = Math.ceil((plainTextContent.split(/\s+/).length || 1) / 200);
            if (readingTime === 0) readingTime = 1;

            $el.append(
                $('<div class="tr-item">').html(
                    '<div class="tr-n">0' + (i+1) + '</div>' +
                    '<div>' +
                    '<div class="tr-ttl">' + p.title + '</div>' +
                    '<div class="tr-meta">' + readingTime + ' min · ' + catName + '</div>' +
                    '</div>'
                ).on('click', function(){
                    window.location.href = 'post.html?id=' + p.slug;
                })
            );
        });
    });
}
