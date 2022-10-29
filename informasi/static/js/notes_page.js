const notesBox = document.getElementById('notes-box')
const spinnerBox = document.getElementById('spinner-box')

const noteForm = document.getElementById('note-form')
const lokasi = document.getElementById('id_lokasi')
const tanggal = document.getElementById('id_tanggal')
const waktu = document.getElementById('id_waktu')
const kapasitas_balita = document.getElementById('id_kapasitas_balita')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const alertBox = document.getElementById('alert-box')

const addButton = document.getElementById('add_info')





function updateTable(){
    // clear table
    var itemCount = $(".table > tbody").children().length;
    for(var i = itemCount; i >= 2; i--){ // remove data dari 2, karena 1 uuntuk header
        $(".table > tbody > tr:nth-child(" + i + ")").remove();
    }
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

        var buttonDelete = document.createElement("button");
        var linkDelete = document.createElement('a');
        linkDelete.append(buttonDelete);
        linkDelete.setAttribute("href", `/periksa/delete/${data[i].pk}`)
        buttonDelete.innerText = "Delete             ";

        var buttonEdit = document.createElement("button");
        var linkEdit = document.createElement('b');
        linkEdit.append(buttonEdit);
        buttonEdit.setAttribute(`data-bs-toggle`, "modal")
        buttonEdit.setAttribute(`data-bs-target`, "#editModal")
        buttonEdit.innerText = "Edit";

        // append data ke cell
        cellLokasi.append(data[i].fields.lokasi);
        cellTanggal.append(data[i].fields.tanggal);
        cellWaktu.append(data[i].fields.waktu);
        cellKapasitasBalita.append(data[i].fields.kapasitas_balita);
        cellDelete.append(linkDelete);
        cellDelete.append(linkEdit);
        
        // append cell ke row
        tr.append(cellLokasi);
        tr.append(cellTanggal);
        tr.append(cellWaktu);
        tr.append(cellKapasitasBalita);
        tr.append(cellDelete);
        
        // add ke tabel
        $(".table").append(tr);
        }
    });
}

$(document).ready(function(){
  updateTable()
  
  $('#add_info').click(function(){
      alert('clicked');
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
          console.log("add success");
          updateTable();
          $("#id_lokasi").val("");
          $("#id_tanggal").val("");
          $("#id_waktu").val("");
          $("#id_kapasitas_balita").val("");
      });
  })
})

