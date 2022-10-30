$(document).ready(function () {
    console.log("shafa")

    updateTable();
    
    $('#add_info').click(function(){
        var lokasi = $("#id_lokasi").val();
        var tanggal = $("#id_tanggal").val();
        var waktu = $("#id_waktu").val();
        var kapasitas_balita = $("#id_kapasitas_balita").val();

        $.post('/periksa/ajax/submit/',{
            lokasi,
            tanggal,
            waktu,
            kapasitas_balita,
        },
        function(data, status){
            alert('Sukses menambahkan informasi!');
            updateTable();
            $("#id_lokasi").val("");
            $("#id_tanggal").val("");
            $("#id_waktu").val("");
            $("#id_kapasitas_balita").val("");
        });
    })
})

function updateTable(){
    // fill table
    $.get('/periksa/json/', function(data) {
        for(var i = 0; i < data.length; i++){
        // buat row
        var tr = document.createElement("tr");

        // buat cell
        var cellLokasi = document.createElement("td");
        var cellTanggal = document.createElement("td");
        var cellWaktu = document.createElement("td");
        var cellKapasitasBalita = document.createElement("td");
        
        var cellDelete = document.createElement("td");
        var cellEdit = document.createElement("td");
        
        // var hiddenInput = document.createElement("input");
        // hiddenInput.setAttribute("type", "hidden");
        // hiddenInput.setAttribute("class", `buat-get-${id}`);
        // hiddenInput.setAttribute("value", data[i].pk);

        var buttonDelete = document.createElement("button");
        var linkDelete = document.createElement('a');
        linkDelete.append(buttonDelete);
        linkDelete.setAttribute("href", `/periksa/delete/${data[i].pk}`)
        linkDelete.setAttribute("class", `bg-merah-tua w-fit text-white p-1 font-bold rounded-lg flex items-center justify-center`)
        buttonDelete.innerText = "Delete";

        var buttonEdit = document.createElement("button");
        var linkEdit = document.createElement('a');

        linkEdit.append(buttonEdit);
        // linkEdit.setAttribute("href", `/periksa/edit/${data[i].pk}`)
        buttonEdit.setAttribute(`data-bs-toggle`, "modal")
        buttonEdit.setAttribute(`data-bs-target`, "#editModal")
        buttonEdit.innerText = "Edit";

        // append data ke cell
        cellLokasi.append(data[i].fields.lokasi);
        cellTanggal.append(data[i].fields.tanggal.split("T")[0]);
        cellWaktu.append(data[i].fields.waktu);
        cellKapasitasBalita.append(data[i].fields.kapasitas_balita);
        cellDelete.append(linkDelete);
        cellEdit.append(linkEdit);
        
        // append cell ke row
        tr.append(cellLokasi);
        tr.append(cellTanggal);
        tr.append(cellWaktu);
        tr.append(cellKapasitasBalita);
        tr.append(cellDelete);
        tr.append(cellEdit);  
        // tr.append(hiddenInput);
        
        // add ke tabel
        $(".table").append(tr);
        }
    });
}
