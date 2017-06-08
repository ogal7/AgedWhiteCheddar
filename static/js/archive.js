$(function() {
    $('#year').click(function() {
        $.ajax({
            url: '/seeit/',
            data: $('form').serialize(),
            type: 'POST',
            success: function(data) {
                $('#table-body').html('');
                for (Mentry in data) {
                for (entry in data[Mentry]) {
                    $('#table-body').append(
                    "<tr>" +
                    "<td>" + Mentry + "</td>" +
                    "<td>" + data[Mentry][entry][3] + "</td>" +
                    "<td>" + data[Mentry][entry][0] + "</td>" +
                    "<td>" + data[Mentry][entry][1] + "</td>" +
                    "</tr>");
                };

                };
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
