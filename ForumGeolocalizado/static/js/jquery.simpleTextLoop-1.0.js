/**
 * Created by higorsilvarosa on 17/11/14.
 */
/** codigogama.com.br */

(function ($) {
    $.fn.simpleTextLoop = function (time) {
        time = typeof time !== 'undefined' ? a : 3000;
        var i = 0;

        function nextText(list) {
            $(list).children("li").hide();
            first = $(list).children("li").first();
            $(list).children("li").first().remove();
            $(list).append(first);
            $(list).children("li").first().show();
        }
        this.each(function () {
            var list = this;
            $(list).children("li").hide();
            $(list).children("li").first().show();
            var loop = setInterval(function () {
                nextText(list);
            }, time);
        });
    }
}(jQuery));