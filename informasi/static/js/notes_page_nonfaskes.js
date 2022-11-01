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
        
        // append data ke cell
        cellLokasi.append(data[i].fields.lokasi);
        cellTanggal.append(data[i].fields.tanggal.split("T")[0]);
        cellWaktu.append(data[i].fields.waktu);
        cellKapasitasBalita.append(data[i].fields.kapasitas_balita);

        // append cell ke row
        tr.append(cellLokasi);
        tr.append(cellTanggal);
        tr.append(cellWaktu);
        tr.append(cellKapasitasBalita);
  
        // add ke tabel
        $(".table").append(tr);
        }
    });
}






