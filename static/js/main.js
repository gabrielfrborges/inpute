function verify(_this){
    $.ajax({
        url: _this,
        type: "POST",
        data: { },
        success: function(json) {
            console.log(json.btn_id);
            console.log($(json.btn_id).attr('class'));
            $(json.btn_id).attr('class', json.btn_class);

            $(json.btn_id).html(json.btn_text);
        },

    });
}

$('.btn-verify').on('submit', function(event){
    event.preventDefault();
    var action = $(this)[0].action;
    verify(action);
});

// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

