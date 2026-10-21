var S = {
    page:   'home',
    cat:    null,
    tag:    null,
    keyword: null,
    sort:   'createdAt,desc',

    get isAuth() { return localStorage.getItem('token') !== null; },
    get uname()  { return localStorage.getItem('username') || 'Guest'; }
};

function fmtDate(iso) {
    if(!iso) return "N/A";
    return new Date(iso).toLocaleDateString('en-US', { month:'short', day:'numeric', year:'numeric' });
}

function excerpt(s, n) {
    if (!s) return "";
    n = n || 200;
    let plainText = "";

    try {
        let parsedData = JSON.parse(s);
        if (parsedData && parsedData.blocks) {
            plainText = parsedData.blocks
                .filter(b => b.type === 'paragraph')
                .map(b => b.data.text.replace(/<[^>]*>/g, ''))
                .join(' ');
        }
    } catch (e) {
        plainText = s.replace(/<[^>]*>/g, '').trim();
    }

    if (plainText.length <= n) return plainText;
    return plainText.substring(0, n).split(' ').slice(0,-1).join(' ') + '…';
}

function extractText(s, n) {
    return excerpt(s, n);
}
window.extractText = excerpt;
window.excerpt = excerpt;

function initials(name) {
    if(!name || name === 'Guest') return "?";
    var parts = name.trim().split(' ');
    if(parts.length === 1) return name.slice(0,2).toUpperCase();
    return (parts[0][0] + parts[parts.length-1][0]).toUpperCase();
}

function extractIdFromSlug(slug) {
    if (!slug) return null;
    return slug.slice(-36);
}

function toast(msg) {
    var $el = $('<div class="toast-item"><span class="toast-dot"></span><span>' + msg + '</span></div>');
    $('#toasts').append($el);
    setTimeout(function(){
        $el.fadeOut(300, function(){ $el.remove(); });
    }, 2800);
}

const API_BASE_URL = (window.location.port === '8080' || window.location.host === 'localhost:8080') ? '' : 'http://localhost:8080';

function callApi(endpoint, method, data = null) {
    var token = localStorage.getItem('token');

    var ajaxConfig = {
        url: API_BASE_URL + endpoint,
        type: method,
        contentType: 'application/json',
        beforeSend: function(xhr) {
            if (token) {
                xhr.setRequestHeader('Authorization', 'Bearer ' + token);
            }
        }
    };

    if (data) {
        ajaxConfig.data = JSON.stringify(data);
    }

    return $.ajax(ajaxConfig).fail(function(xhr) {
        console.error("API Error: ", xhr.responseText);
        if (xhr.status === 401 || xhr.status === 403) {
            toast("Phiên đăng nhập hết hạn hoặc không có quyền!");
        }
    });
}
