$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const language = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://fourtonfish.com/hellosalut/?lang=' + language,
      type: 'GET',
      dataType: 'json'
    }).done(function (json) {
      $('DIV#hello').text(json.hello);
    });
  });
});
