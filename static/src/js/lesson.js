/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $('#save_lesson').on('click', function () {
        var _data = {
            'name': $('#id_name_lesson').val(),
            'place': $('#id_place_lesson').val(),
            'description': $('#id_description_lesson').val(),
            'timeout': $('#id_timeout_lesson').val()
        };
        $.ajax({
            type: "POST",
            url: '/lesson/create/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(_data),
            success: function (_data) {
                console.log(_data);
            },
            error: function (_data) {
                console.log(_data);
            }
        });
    });
});

function update_lesson(id) {

    var _data = {
            'id': id ,
            'name': $('#id_name_lesson').val(),
            'description': $('#id_description_lesson').val(),
            'place': $('#id_place_lesson').val(),
            'timeout': $('#id_timeout_lesson').val()
        };

    $.ajax({
            type: "PUT",
            url: '/lesson/'+ id + '/edit/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(_data),
            success: function (respons) {
                console.log(respons);
            },
            error: function (err) {
                console.log(err);
            }
        });
}