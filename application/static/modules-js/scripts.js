$(document).ready(function () {
    // Read the cookie and if it's defined scroll to id
    var scroll = $.cookie('scroll');
    if(scroll){
        scrollToID(scroll, 1000);
        $.removeCookie('scroll');
    }

    // Handle event onclick, setting the cookie when the href != #
    $('.nav a').click(function (e) {
        e.preventDefault();
        var id = $(this).data('id');
        var href = $(this).attr('href');
        if(href === '#'){
            scrollToID(id, 1000);
        }else{
            $.cookie('scroll', id);
            window.location.href = href;
        }
    });

    // scrollToID function
    function scrollToID(id, speed) {
        var offSet = 70;
        var obj = $('#' + id).offset();
        var targetOffset = obj.top - offSet;
        $('html,body').animate({ scrollTop: targetOffset }, speed);
    }
});