// $(document).ready(function () {
//         $.ajax({
//             url: "http://localhost:8000/api/v1/vpn-subscription/",
//             dataType: 'json',
//             type: 'get',
//             cache: false,
//             success: function (data) {
//                 /*console.log(data);*/
//                 var event_data = '';
//                 $.each(data, function (index, value) {
//                     /*console.log(value);*/
//                     event_data += '<tr>';
//                     event_data += '<td>' + value.discount + '</td>';
//                     event_data += '<td>' + value.pkid + '</td>';
//                     event_data += '</tr>';
//                 });
//                 $("#list_table_json").append(event_data);
//             },
//             error: function (d) {
//                 /*console.log("error");*/
//                 alert("404. Please wait until the File is Loaded.");
//             }
//         });
//     });

    // function doPoll() {
    //     const elem = document.getElementById('element_id');

    //     if (elem !== null && typeof elem !== null && elem !== 'undefined') {
    //         console.log('Set new value')
    //         elem.textContent = new Date().toLocaleString();
    //     }
    //     setTimeout(doPoll, 2000)

    //     //    $.post('<api_endpoint_here>', function(data) {}

    //     doPoll();
    // }



    function insert() {
        let blocks = document.querySelector(".blocks")
        
        let block = document.createElement('div');
        block.className="table-block"

        for (let i = 0; i < 5; i++) {
            let cell = document.createElement('div')
            cell.className="div-sup_six"
            cell.innerHTML="<p class=\"page-info\">Text</p>"
            block.appendChild(cell)
          } 
        blocks.appendChild(block)
        //   subheadPage.insertAfter(block)
    }

    insert()