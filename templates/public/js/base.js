/**
 * Created by Nurs on 28.06.2017.
 */
$(document).ready(function () {
    $('.main_slider').slick({
        dots: true,
        speed: 1500,
        autoplay: false,
        draggable: false,
        cssEase: 'ease-in-out',
        dotsClass: 'main-dots',
        arrows: false,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    adaptiveHeight: true
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    adaptiveHeight: true
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    });
    $('.left_panel ul li a').on('click', function (e) {
        e.preventDefault();
        $(this).parent().addClass('left_panel_active_tab');
        $(this).parent().siblings().removeClass('left_panel_active_tab');
        var get_content = $(this).attr('href');
        $(get_content).siblings().fadeOut("slow");
        $('.category').fadeIn("slow");
        $(get_content).fadeIn("slow", function () {
            var get_scroll = $(get_content).offset().top;
            $('html,body').stop().animate({scrollTop: get_scroll}, 1000);
        });
    });
    $('.hamburger').on('click', function (e) {
        e.preventDefault();
        var Getblock = $(this).attr('href');
        if ($(this).hasClass('closed')) {
            $(Getblock).css({
                'opacity': 1,
                'visibility': 'visible'
            });
            $(this).parent().css({

                'background-color': 'transparent'
            });
            $(this).html('<i class="fa fa-close"></i>');
            $(this).removeClass('closed');
        }
        else {
            $(Getblock).css({
                'opacity': 0,
                'visibility': 'hidden'
            });
            $(this).parent().css({
                'background-color': 'rgba(' + 52 + ',' + 116 + ',' + 48 + ',' + 0.5+')'
            });
            $(this).html('<i class="fa fa-bars"></i>');
            $(this).addClass('closed');
        }
    });
});
$(document).scroll(function () {
    if ($(document).scrollTop() > '500') {
        $('.right_banner').addClass('fixed_banner');
        $('.left_panel').addClass('fixed_banner');
    }
    else {
        $('.right_banner').removeClass('fixed_banner');
        $('.left_panel').removeClass('fixed_banner');
    }
});