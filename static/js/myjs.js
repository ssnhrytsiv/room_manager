 function del(id){
   var _data = {
        'id': id,
        'name': name
   };
    $.ajax({
          type: "DELETE",
          url: "delete/",
          dataType: 'json',
          data: JSON.stringify(_data),
          success:
          function(response){
            console.log(response);
          }



    });
}