$(document).ready(function () {
    if (context != "bumil") {
      $("#tambah-btn").hide();
      $("#bumil").hide();
    } else {
      $("#authorize-non").hide();
      $("#login").hide();
      $.get("/catatbund/json/", function (data) {
        console.log(data)
        for (i = 0; i < data.length; i++) {
          $("#row").append(getCard(data[i]))
        }
      })};

    $("#unggah-btn").click(function () {
      $.post("/catatbund/add/",
        $('#input-form').serialize(),
        function (res, status) {
          console.log(res)
          if(res.status == "error") {
            const toast = new bootstrap.Toast($('#liveToast'))
            toast.show()
          } else {
          $("#row").append(postCard(res))
          $(`.modal--${res.pk}`).modal("hide")
      $('#weight').val('')
      $('#height').val('')
    }
        })
    });

  });

function editCard(id) {
console.log("================ edit function");
    $.post(
    `/catatbund/edit/${id}`,
    {
        weight: $(`#input-weight-${id}`).val(),
        height: $(`#input-height-${id}`).val(),
    },
    function (data, status) {
        console.log("edit ")
        if (status == 'success') {
        $(`#weight-${id}`).text(`Berat badan(kg): ${data.fields.weight}`)
        $(`#height-${id}`).text(`Tinggi badan(m): ${data.fields.height}`)
        $(`#bmi-${id}`).text(`BMI: ${data.fields.bmi}`)
        $(`#bmi-${id}`).html(`<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">BMI: ${data.fields.bmi}</span>`)
        }
    },
    )
}