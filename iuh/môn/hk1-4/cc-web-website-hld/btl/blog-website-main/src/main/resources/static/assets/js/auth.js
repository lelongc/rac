function renderAuth() {
    var $d = $('#auth-area').empty();
    var $m = $('#mob-auth').empty();

    const token = localStorage.getItem('token');
    const uname = localStorage.getItem('username');

    const isAuth = token !== null && token !== "";

    if (isAuth) {
        const displayName = uname || 'Guest';

        $d.append(
            $('<button class="btn-newpost">').html(
                '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>New Post'
            ).on('click', function(){ window.location.href = 'editor.html'; })
        );

        var $wrap = $('<div style="position:relative;"></div>');
        var $av   = $('<div class="avatar">').text(initials(displayName)).attr('title', displayName);
        var $dd   = $('<div class="user-dd">');

        $dd.append(
            $('<div class="dd-head">').html(
                '<div class="dn">' + displayName + '</div><div class="dr">Author</div>'
            )
        );

        $dd.append('<div class="dd-sep"></div>');

        $dd.append(
            $('<button class="dd-btn red">').html(
                '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>Log Out'
            ).on('click', handleLogout)
        );

        $av.on('click', function(e){
            e.stopPropagation();
            $('.user-dd').not($dd).removeClass('open');
            $dd.toggleClass('open');
        });

        $wrap.append($av, $dd);
        $d.append($wrap);

    } else {
        $d.append(
            $('<button class="btn-login">').text('Log In').on('click', function(){
                window.location.href = 'login.html';
            })
        );
        $d.append(
            $('<button class="btn-register">').text('Sign Up').on('click', function(){
                window.location.href = 'register.html';
            })
        );
    }
}

function initials(name) {
    if (!name || name === 'Guest') return "?";

    name = name.trim();
    var parts = name.split(' ');

    if (parts.length >= 2) {
        return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
    } else {
        return name.slice(0, 2).toUpperCase();
    }
}

function handleLogout() {
    localStorage.removeItem('token');
    localStorage.removeItem('username');

    if(typeof toast === 'function') toast('Đã đăng xuất thành công.');

    setTimeout(() => {
        window.location.href = 'home-page.html';
    }, 500);
}

$(document).ready(function() {
    renderAuth();
});

$(document).on('click', function(){ $('.user-dd').removeClass('open'); });
