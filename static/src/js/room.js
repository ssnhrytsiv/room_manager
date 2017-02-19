/**
 * Created by Nazar on 18.02.2017.
 */

$(document).ready(function () {
    $('#save_room').on('click', function () {
        var _data = {
            'name': $('#id_name_room').val(),
            'type': $('#id_type_room').val(),
            'description': $('#id_description_room').val(),
            'size': $('#id_size_room').val()
        };
        $.ajax({
            type: "POST",
            url: '/room/create/',
            contentType: 'application/json; charset=utf-8',
            data: JSON.stringify(_data),
            async: false,
            success: function (_data) {
                console.log(_data);
            },
            error: function (_data) {
                console.log(_data);
            }
        });
    });
});

function update_room(id) {

    var _data = {
            'id': id ,
            'name': $('#id_name_room').val(),
            'type': $('#id_type_room').val(),
            'description': $('#id_description_room').val(),
            'size': $('#id_size_room').val()
        };

    $.ajax({
            type: "PUT",
            url: '/room/'+ id +'/edit/',
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

