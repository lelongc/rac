$(document).ready(function() {

    const urlParams = new URLSearchParams(window.location.search);
    const catSlug = urlParams.get('cat');

    if (catSlug) {
        S.cat = extractIdFromSlug(catSlug);
    }

    if (typeof fetchAndRenderFilters === 'function') {
        fetchAndRenderFilters();
    }

    if (typeof renderPosts === 'function') {
        renderPosts();
    }

    if (typeof renderSbCategories === 'function') {
        renderSbCategories();
    }

    if (typeof renderSbTrending === 'function') {
        renderSbTrending();
    }

});
