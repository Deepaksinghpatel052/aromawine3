$(document).ready(function(){
    $('.vintageshow').click(function(event){
        event.stopPropagation();
         $(".sincebox").slideToggle("fast");
    });
    $(".sincebox").on("click", function (event) {
        event.stopPropagation();
    });
});

$(document).on("click", function () {
    $(".sincebox").hide();
});

$(document).ready(function(){
    $('.vintageshow1').click(function(event){
        event.stopPropagation();
         $(".redtoggle").slideToggle("fast");
    });
    $(".redtoggle").on("click", function (event) {
        event.stopPropagation();
    });
});

$(document).on("click", function () {
    $(".redtoggle").hide();
});


jQuery(document).ready(function($) {
    $(".region_tabs li").hover(function() {
        $(".mega_menu_show").hide();
        $(".region_tabs li").removeClass('active');                  
        $(this).addClass("active");                 
        var selected_tab = $(this).find("a").attr("href");
        $(selected_tab).show();
        return false;
    });
});


jQuery(document).ready(function($) {
    $(".region_tabs_w li").hover(function() {
        $(".mega_menu_show_w").hide();
        $(".region_tabs_w li").removeClass('active');                  
        $(this).addClass("active");                 
        var selected_tab = $(this).find("a").attr("href");
        $(selected_tab).show();
        return false;
    });
});


jQuery(document).ready(function($) {
    $(".france_w li").hover(function() {
        $(".country_div").hide();
        $(".france_w li").removeClass('active');                  
        $(this).addClass("active");                 
        var selected_tab = $(this).find("a").attr("href");
        $(selected_tab).show();
        return false;
    });
});

jQuery(document).ready(function($) {
    $(".region_b li").hover(function() {
        $(".applicon_w").hide();
        $(".region_b li").removeClass('active');                  
        $(this).addClass("active");                 
        var selected_tab = $(this).find("a").attr("href");
        $(selected_tab).show();
        return false;
    });
});



$(document).ready(function () {
    
    $(".accordion_head").click(function () {
        if ($('.accordion_body').is(':visible')) {
            $(".accordion_body").slideUp(300);
            $(".plusminus").text('+');
        }
        if ($(this).next(".accordion_body").is(':visible')) {
            $(this).next(".accordion_body").slideUp(300);
            $(this).children(".plusminus").text('+');
        } else {
            $(this).next(".accordion_body").slideDown(300);
            $(this).children(".plusminus").text('-');
        }
    });
});
$(document).ready(function(){
    
    $('ul.product-tabs li').click(function(){
        var tab_id = $(this).attr('data-tab');

        $('ul.product-tabs li').removeClass('current');
        $('.tab-content').removeClass('current');

        $(this).addClass('current');
        $("#"+tab_id).addClass('current');
    })
    
    $('ul.product-tabs1 li').click(function(){
        var tab_id = $(this).attr('data-tab');

        $('ul.product-tabs1 li').removeClass('current');
        $('.tab-content1').removeClass('current');

        $(this).addClass('current');
        $("#"+tab_id).addClass('current');
    })

})     
    
jQuery(document).ready(function(){
jQuery('#carouselExampleIndicators').carousel({
  interval: 2000
})
});

/*------------------------------------
    single-carousel
    ------------------------------------- */  
    $("#single-carousel").owlCarousel({
        autoplay: false,
        slideSpeed:1500,
        pagination:false,
        nav: true,
        items : 4,
        margin:30,
        itemsDesktop : [1199,3],
        itemsDesktopSmall : [980,2],
        itemsTablet: [768,2],
        itemsMobile : [479,1],
    });
    
 
    


  jQuery("#carousel").owlCarousel({
    autoplay: true,
    lazyLoad: true,
    loop: true,
    margin: 20,
     /*
    animateOut: 'fadeOut',
    animateIn: 'fadeIn',
    */
    responsiveClass: true,
    autoHeight: true,
    autoplayTimeout: 7000,
    smartSpeed: 800,
    nav: true,
    responsive: {
      0: {
        items: 1
      },
  
      600: {
        items: 2
      },
  
      1024: {
        items: 3
      },
  
      1366: {
        items:6
      }
    }
  });

  jQuery("#carousel1").owlCarousel({
    autoplay: true,
    lazyLoad: true,
    loop: true,
    margin: 20,
     /*
    animateOut: 'fadeOut',
    animateIn: 'fadeIn',
    */
    responsiveClass: true,
    autoHeight: true,
    autoplayTimeout: 7000,
    smartSpeed: 800,
    nav: true,
    responsive: {
      0: {
        items: 1
      },
  
      600: {
        items: 3
      },
  
      1024: {
        items: 4
      },
  
      1366: {
        items: 4
      }
    }
  });
  
  
  jQuery("#releted-product").owlCarousel({
    autoplay: true,
    lazyLoad: true,
    loop: true,
    margin: 20,
     /*
    animateOut: 'fadeOut',
    animateIn: 'fadeIn',
    */
    responsiveClass: true,
    autoHeight: true,
    autoplayTimeout: 7000,
    smartSpeed: 800,
    nav: true,
    responsive: {
      0: {
        items: 1
      },
  
      600: {
        items: 3
      },
  
      1024: {
        items: 4
      },
  
      1366: {
        items: 4
      }
    }
  });
  
  jQuery("#releted-product1").owlCarousel({
    autoplay: true,
    lazyLoad: true,
    loop: true,
    margin: 20,
     /*
    animateOut: 'fadeOut',
    animateIn: 'fadeIn',
    */
    responsiveClass: true,
    autoHeight: true,
    autoplayTimeout: 7000,
    smartSpeed: 800,
    nav: true,
    responsive: {
      0: {
        items: 1
      },
  
      600: {
        items: 3
      },
  
      1024: {
        items: 4
      },
  
      1366: {
        items: 4
      }
    }
  });
  

        function openCity(cityName,elmnt,color) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
      tablinks = document.getElementsByClassName("tablink");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
      }
      document.getElementById(cityName).style.display = "block";
      elmnt.style.backgroundColor = color;
    
    }
    // Get the element with id="defaultOpen" and click on it
    // document.getElementById("defaultOpen").click();

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

  jQuery(function ($) {
jQuery('.article-title').on('click', function () {
 
  jQuery(this).next().slideToggle(200);
 
  jQuery(this).toggleClass('open');
});

});

$(document).ready(function(){
  $(".read-more-show").click(function(){
    $(".details").slideDown();
    $(".read-more-show").hide();
  });
  $(".read-less").click(function(){
    $(".details").slideUp();
    $(".read-more-show").show();
  });
});


(function($) {
    'use strict';

    var _currentSpinnerId = 0;

    function _scopedEventName(name, id) {
        return name + '.touchspin_' + id;
    }

    function _scopeEventNames(names, id) {
        return $.map(names, function(name) {
            return _scopedEventName(name, id);
        });
    }

    $.fn.TouchSpin = function(options) {

        if (options === 'destroy') {
            this.each(function() {
                var originalinput = $(this),
                    originalinput_data = originalinput.data();
                $(document).off(_scopeEventNames([
                  'mouseup',
                  'touchend',
                  'touchcancel',
                  'mousemove',
                  'touchmove',
                  'scroll',
                  'scrollstart'], originalinput_data.spinnerid).join(' '));
            });
            return;
        }

        var defaults = {
            min: 0,
            max: 100,
            initval: '',
            replacementval: '',
            step: 1,
            decimals: 0,
            stepinterval: 100,
            forcestepdivisibility: 'round', // none | floor | round | ceil
            stepintervaldelay: 500,
            verticalbuttons: false,
            verticalupclass: 'glyphicon glyphicon-chevron-up',
            verticaldownclass: 'glyphicon glyphicon-chevron-down',
            prefix: '',
            postfix: '',
            prefix_extraclass: '',
            postfix_extraclass: '',
            booster: true,
            boostat: 10,
            maxboostedstep: false,
            mousewheel: true,
            buttondown_class: 'btn btn-default',
            buttonup_class: 'btn btn-default',
            buttondown_txt: '-',
            buttonup_txt: '+'
        };

        var attributeMap = {
            min: 'min',
            max: 'max',
            initval: 'init-val',
            replacementval: 'replacement-val',
            step: 'step',
            decimals: 'decimals',
            stepinterval: 'step-interval',
            verticalbuttons: 'vertical-buttons',
            verticalupclass: 'vertical-up-class',
            verticaldownclass: 'vertical-down-class',
            forcestepdivisibility: 'force-step-divisibility',
            stepintervaldelay: 'step-interval-delay',
            prefix: 'prefix',
            postfix: 'postfix',
            prefix_extraclass: 'prefix-extra-class',
            postfix_extraclass: 'postfix-extra-class',
            booster: 'booster',
            boostat: 'boostat',
            maxboostedstep: 'max-boosted-step',
            mousewheel: 'mouse-wheel',
            buttondown_class: 'button-down-class',
            buttonup_class: 'button-up-class',
            buttondown_txt: 'button-down-txt',
            buttonup_txt: 'button-up-txt'
        };

        return this.each(function() {

            var settings,
                originalinput = $(this),
                originalinput_data = originalinput.data(),
                container,
                elements,
                value,
                downSpinTimer,
                upSpinTimer,
                downDelayTimeout,
                upDelayTimeout,
                spincount = 0,
                spinning = false;

            init();


            function init() {
                if (originalinput.data('alreadyinitialized')) {
                    return;
                }

                originalinput.data('alreadyinitialized', true);
                _currentSpinnerId += 1;
                originalinput.data('spinnerid', _currentSpinnerId);


                if (!originalinput.is('input')) {
                    console.log('Must be an input.');
                    return;
                }

                _initSettings();
                _setInitval();
                _checkValue();
                _buildHtml();
                _initElements();
                _hideEmptyPrefixPostfix();
                _bindEvents();
                _bindEventsInterface();
                elements.input.css('display', 'block');
            }

            function _setInitval() {
                if (settings.initval !== '' && originalinput.val() === '') {
                    originalinput.val(settings.initval);
                }
            }

            function changeSettings(newsettings) {
                _updateSettings(newsettings);
                _checkValue();

                var value = elements.input.val();

                if (value !== '') {
                    value = Number(elements.input.val());
                    elements.input.val(value.toFixed(settings.decimals));
                }
            }

            function _initSettings() {
                settings = $.extend({}, defaults, originalinput_data, _parseAttributes(), options);
            }

            function _parseAttributes() {
                var data = {};
                $.each(attributeMap, function(key, value) {
                    var attrName = 'bts-' + value + '';
                    if (originalinput.is('[data-' + attrName + ']')) {
                        data[key] = originalinput.data(attrName);
                    }
                });
                return data;
            }

            function _updateSettings(newsettings) {
                settings = $.extend({}, settings, newsettings);
            }

            function _buildHtml() {
                var initval = originalinput.val(),
                    parentelement = originalinput.parent();

                if (initval !== '') {
                    initval = Number(initval).toFixed(settings.decimals);
                }

                originalinput.data('initvalue', initval).val(initval);
                originalinput.addClass('form-control');

                if (parentelement.hasClass('input-group')) {
                    _advanceInputGroup(parentelement);
                }
                else {
                    _buildInputGroup();
                }
            }

            function _advanceInputGroup(parentelement) {
                parentelement.addClass('bootstrap-touchspin');

                var prev = originalinput.prev(),
                    next = originalinput.next();

                var downhtml,
                    uphtml,
                    prefixhtml = '<span class="input-group-addon bootstrap-touchspin-prefix">' + settings.prefix + '</span>',
                    postfixhtml = '<span class="input-group-addon bootstrap-touchspin-postfix">' + settings.postfix + '</span>';

                if (prev.hasClass('input-group-btn')) {
                    downhtml = '<button class="' + settings.buttondown_class + ' bootstrap-touchspin-down mybut" type="button">' + settings.buttondown_txt + '</button>';
                    prev.append(downhtml);
                }
                else {
                    downhtml = '<span class="input-group-btn"><button class="' + settings.buttondown_class + ' bootstrap-touchspin-down" type="button">' + settings.buttondown_txt + '</button></span>';
                    $(downhtml).insertBefore(originalinput);
                }

                if (next.hasClass('input-group-btn')) {
                    uphtml = '<button class="' + settings.buttonup_class + ' bootstrap-touchspin-up" type="button">' + settings.buttonup_txt + '</button>';
                    next.prepend(uphtml);
                }
                else {
                    uphtml = '<span class="input-group-btn"><button class="' + settings.buttonup_class + ' bootstrap-touchspin-up" type="button">' + settings.buttonup_txt + '</button></span>';
                    $(uphtml).insertAfter(originalinput);
                }

                $(prefixhtml).insertBefore(originalinput);
                $(postfixhtml).insertAfter(originalinput);

                container = parentelement;
            }

            function _buildInputGroup() {
                var html;

                if (settings.verticalbuttons) {
                    html = '<div class="input-group bootstrap-touchspin"><span class="input-group-addon bootstrap-touchspin-prefix">' + settings.prefix + '</span><span class="input-group-addon bootstrap-touchspin-postfix">' + settings.postfix + '</span><span class="input-group-btn-vertical"><button class="' + settings.buttondown_class + ' bootstrap-touchspin-up" type="button"><i class="' + settings.verticalupclass + '"></i></button><button class="' + settings.buttonup_class + ' bootstrap-touchspin-down" type="button"><i class="' + settings.verticaldownclass + '"></i></button></span></div>';
                }
                else {
                    html = '<div class="input-group bootstrap-touchspin"><span class="input-group-btn"><button class="' + settings.buttondown_class + ' bootstrap-touchspin-down" type="button">' + settings.buttondown_txt + '</button></span><span class="input-group-addon bootstrap-touchspin-prefix">' + settings.prefix + '</span><span class="input-group-addon bootstrap-touchspin-postfix">' + settings.postfix + '</span><span class="input-group-btn"><button class="' + settings.buttonup_class + ' bootstrap-touchspin-up" type="button">' + settings.buttonup_txt + '</button></span></div>';
                }

                container = $(html).insertBefore(originalinput);

                $('.bootstrap-touchspin-prefix', container).after(originalinput);

                if (originalinput.hasClass('input-sm')) {
                    container.addClass('input-group-sm');
                }
                else if (originalinput.hasClass('input-lg')) {
                    container.addClass('input-group-lg');
                }
            }

            function _initElements() {
                elements = {
                    down: $('.bootstrap-touchspin-down', container),
                    up: $('.bootstrap-touchspin-up', container),
                    input: $('input', container),
                    prefix: $('.bootstrap-touchspin-prefix', container).addClass(settings.prefix_extraclass),
                    postfix: $('.bootstrap-touchspin-postfix', container).addClass(settings.postfix_extraclass)
                };
            }

            function _hideEmptyPrefixPostfix() {
                if (settings.prefix === '') {
                    elements.prefix.hide();
                }

                if (settings.postfix === '') {
                    elements.postfix.hide();
                }
            }

            function _bindEvents() {
                originalinput.on('keydown', function(ev) {
                    var code = ev.keyCode || ev.which;

                    if (code === 38) {
                        if (spinning !== 'up') {
                            upOnce();
                            startUpSpin();
                        }
                        ev.preventDefault();
                    }
                    else if (code === 40) {
                        if (spinning !== 'down') {
                            downOnce();
                            startDownSpin();
                        }
                        ev.preventDefault();
                    }
                });

                originalinput.on('keyup', function(ev) {
                    var code = ev.keyCode || ev.which;

                    if (code === 38) {
                        stopSpin();
                    }
                    else if (code === 40) {
                        stopSpin();
                    }
                });

                originalinput.on('blur', function() {
                    _checkValue();
                });

                elements.down.on('keydown', function(ev) {
                    var code = ev.keyCode || ev.which;

                    if (code === 32 || code === 13) {
                        if (spinning !== 'down') {
                            downOnce();
                            startDownSpin();
                        }
                        ev.preventDefault();
                    }
                });

                elements.down.on('keyup', function(ev) {
                    var code = ev.keyCode || ev.which;

                    if (code === 32 || code === 13) {
                        stopSpin();
                    }
                });

                elements.up.on('keydown', function(ev) {
                    var code = ev.keyCode || ev.which;

                    if (code === 32 || code === 13) {
                        if (spinning !== 'up') {
                            upOnce();
                            startUpSpin();
                        }
                        ev.preventDefault();
                    }
                });

                elements.up.on('keyup', function(ev) {
                    var code = ev.keyCode || ev.which;

                    if (code === 32 || code === 13) {
                        stopSpin();
                    }
                });

                elements.down.on('mousedown.touchspin', function(ev) {
                    elements.down.off('touchstart.touchspin');  // android 4 workaround

                    if (originalinput.is(':disabled')) {
                        return;
                    }

                    downOnce();
                    startDownSpin();

                    ev.preventDefault();
                    ev.stopPropagation();
                });

                elements.down.on('touchstart.touchspin', function(ev) {
                    elements.down.off('mousedown.touchspin');  // android 4 workaround

                    if (originalinput.is(':disabled')) {
                        return;
                    }

                    downOnce();
                    startDownSpin();

                    ev.preventDefault();
                    ev.stopPropagation();
                });

                elements.up.on('mousedown.touchspin', function(ev) {
                    elements.up.off('touchstart.touchspin');  // android 4 workaround

                    if (originalinput.is(':disabled')) {
                        return;
                    }

                    upOnce();
                    startUpSpin();

                    ev.preventDefault();
                    ev.stopPropagation();
                });

                elements.up.on('touchstart.touchspin', function(ev) {
                    elements.up.off('mousedown.touchspin');  // android 4 workaround

                    if (originalinput.is(':disabled')) {
                        return;
                    }

                    upOnce();
                    startUpSpin();

                    ev.preventDefault();
                    ev.stopPropagation();
                });

                elements.up.on('mouseout touchleave touchend touchcancel', function(ev) {
                    if (!spinning) {
                        return;
                    }

                    ev.stopPropagation();
                    stopSpin();
                });

                elements.down.on('mouseout touchleave touchend touchcancel', function(ev) {
                    if (!spinning) {
                        return;
                    }

                    ev.stopPropagation();
                    stopSpin();
                });

                elements.down.on('mousemove touchmove', function(ev) {
                    if (!spinning) {
                        return;
                    }

                    ev.stopPropagation();
                    ev.preventDefault();
                });

                elements.up.on('mousemove touchmove', function(ev) {
                    if (!spinning) {
                        return;
                    }

                    ev.stopPropagation();
                    ev.preventDefault();
                });

                $(document).on(_scopeEventNames(['mouseup', 'touchend', 'touchcancel'], _currentSpinnerId).join(' '), function(ev) {
                    if (!spinning) {
                        return;
                    }

                    ev.preventDefault();
                    stopSpin();
                });

                $(document).on(_scopeEventNames(['mousemove', 'touchmove', 'scroll', 'scrollstart'], _currentSpinnerId).join(' '), function(ev) {
                    if (!spinning) {
                        return;
                    }

                    ev.preventDefault();
                    stopSpin();
                });

                originalinput.on('mousewheel DOMMouseScroll', function(ev) {
                    if (!settings.mousewheel || !originalinput.is(':focus')) {
                        return;
                    }

                    var delta = ev.originalEvent.wheelDelta || -ev.originalEvent.deltaY || -ev.originalEvent.detail;

                    ev.stopPropagation();
                    ev.preventDefault();

                    if (delta < 0) {
                        downOnce();
                    }
                    else {
                        upOnce();
                    }
                });
            }

            function _bindEventsInterface() {
                originalinput.on('touchspin.uponce', function() {
                    stopSpin();
                    upOnce();
                });

                originalinput.on('touchspin.downonce', function() {
                    stopSpin();
                    downOnce();
                });

                originalinput.on('touchspin.startupspin', function() {
                    startUpSpin();
                });

                originalinput.on('touchspin.startdownspin', function() {
                    startDownSpin();
                });

                originalinput.on('touchspin.stopspin', function() {
                    stopSpin();
                });

                originalinput.on('touchspin.updatesettings', function(e, newsettings) {
                    changeSettings(newsettings);
                });
            }

            function _forcestepdivisibility(value) {
                switch (settings.forcestepdivisibility) {
                    case 'round':
                        return (Math.round(value / settings.step) * settings.step).toFixed(settings.decimals);
                    case 'floor':
                        return (Math.floor(value / settings.step) * settings.step).toFixed(settings.decimals);
                    case 'ceil':
                        return (Math.ceil(value / settings.step) * settings.step).toFixed(settings.decimals);
                    default:
                        return value;
                }
            }

            function _checkValue() {
                var val, parsedval, returnval;

                val = originalinput.val().replace(',', '');

                if (val === '') {
                    if (settings.replacementval !== '') {
                        originalinput.val(settings.replacementval);
                        originalinput.trigger('change');
                    }
                    return;
                }

                if (settings.decimals > 0 && val === '.') {
                    return;
                }

                parsedval = parseFloat(val);

                if (isNaN(parsedval)) {
                    if (settings.replacementval !== '') {
                        parsedval = settings.replacementval;
                    }
                    else {
                        parsedval = 0;
                    }
                }

                returnval = parsedval;

                if (parsedval.toString() !== val) {
                    returnval = parsedval;
                }

                if (parsedval < settings.min) {
                    returnval = settings.min;
                }

                if (parsedval > settings.max) {
                    returnval = settings.max;
                }

                returnval = _forcestepdivisibility(returnval);

                if (Number(val).toString() !== returnval.toString()) {
                    //originalinput.val(returnval);
                    originalinput.val(returnval.toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",")); // Added Format back
                    originalinput.trigger('change');
                }
            }

            function _getBoostedStep() {
                if (!settings.booster) {
                    return settings.step;
                }
                else {
                    var boosted = Math.pow(2, Math.floor(spincount / settings.boostat)) * settings.step;

                    if (settings.maxboostedstep) {
                        if (boosted > settings.maxboostedstep) {
                            boosted = settings.maxboostedstep;
                            value = Math.round((value / boosted)) * boosted;
                        }
                    }

                    return Math.max(settings.step, boosted);
                }
            }

            function upOnce() {
                _checkValue();

                //value = parseFloat(elements.input.val());
                value = parseFloat(elements.input.val().replace(',',''));
                if (isNaN(value)) {
                    value = 0;
                }

                var initvalue = value,
                    boostedstep = _getBoostedStep();

                value = value + boostedstep;

                if (value > settings.max) {
                    value = settings.max;
                    originalinput.trigger('touchspin.on.max');
                    stopSpin();
                }

                elements.input.val(Number(value).toFixed(settings.decimals).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ","));

                if (initvalue !== value) {
                    originalinput.trigger('change');
                }
            }

            function downOnce() {
                _checkValue();

                //value = parseFloat(elements.input.val());
                value = parseFloat(elements.input.val().replace(',', ''));
                if (isNaN(value)) {
                    value = 0;
                }

                var initvalue = value,
                    boostedstep = _getBoostedStep();

                value = value - boostedstep;

                if (value < settings.min) {
                    value = settings.min;
                    originalinput.trigger('touchspin.on.min');
                    stopSpin();
                }

                elements.input.val(value.toFixed(settings.decimals).toString().replace(/,/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ","));

                if (initvalue !== value) {
                    originalinput.trigger('change');
                }
            }

            function startDownSpin() {
                stopSpin();

                spincount = 0;
                spinning = 'down';

                originalinput.trigger('touchspin.on.startspin');
                originalinput.trigger('touchspin.on.startdownspin');

                downDelayTimeout = setTimeout(function() {
                    downSpinTimer = setInterval(function() {
                        spincount++;
                        downOnce();
                    }, settings.stepinterval);
                }, settings.stepintervaldelay);
            }

            function startUpSpin() {
                stopSpin();

                spincount = 0;
                spinning = 'up';

                originalinput.trigger('touchspin.on.startspin');
                originalinput.trigger('touchspin.on.startupspin');

                upDelayTimeout = setTimeout(function() {
                    upSpinTimer = setInterval(function() {
                        spincount++;
                        upOnce();
                    }, settings.stepinterval);
                }, settings.stepintervaldelay);
            }

            function stopSpin() {
                clearTimeout(downDelayTimeout);
                clearTimeout(upDelayTimeout);
                clearInterval(downSpinTimer);
                clearInterval(upSpinTimer);

                switch (spinning) {
                    case 'up':
                        originalinput.trigger('touchspin.on.stopupspin');
                        originalinput.trigger('touchspin.on.stopspin');
                        break;
                    case 'down':
                        originalinput.trigger('touchspin.on.stopdownspin');
                        originalinput.trigger('touchspin.on.stopspin');
                        break;
                }

                spincount = 0;
                spinning = false;
            }

        });

    };

})(jQuery);


function formatNumber(nStr) {
    //check for blank, use jquery trim for ie8 compat
    if ("" === $.trim(nStr)) {
        return 0;
    }

    // Check if it is a number
    if (!$.isNumeric(nStr)) {
        return nStr;
    }

    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    return x1 + x2;
}

function initCommas() {
    // Cache document for better performance
    var $document = $(document);

    $document.on('blur', '.comma-format', function() {
        // Format and place back into text
        $(this).val(formatNumber($(this).val()));
    });
}

$('.dollar-spin').TouchSpin({
        min: 1,
        max: 100,
        step: 1,
        forcestepdivisibility: 'round',
        replacementval: 0
});
$(function () {
  //this formats the number if it was typed in manually -- the spin code is in the modified bootstrap-touchspin script
  initCommas();
});

$('.moreless-button').click(function() {
  $('.moretext').slideToggle();
  if ($('.moreless-button').text() == "Read more") {
    $(this).text("Read less")
  } else {
    $(this).text("Read more")
  }
});

$('#facetfilterNavigation .dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});
