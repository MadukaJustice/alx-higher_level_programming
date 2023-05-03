$(document).ready(function () {
    $('#btn_translate').click(() => {
        showHelloIn($('#language_code').val());
    });
    $('#language_code').keydown((e) => {
        if (e.which == 13) showHelloIn($('#language_code').val());
    });
});

function showHelloIn(lang) {
    $.get(
        `https://fourtonfish.com/hellosalut/?lang=${lang}`,
        (data, status) => {
            $('#hello').text(data['hello']);
        }
    );
}
