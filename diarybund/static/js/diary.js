$(document).ready(function(){
    let context = "{{user_type}}";
    if (context != "bumil") {
      $("#tulisDiary").hide();
    } else {
      $.get( "/diarybund/json/", function( data ) {
        console.log(data)
        for (let i = 0; i < data.length; i++) {
          $('#diarybund').append(
            `<div id = "${data[i].pk}--tugas" class = "rounded-lg pl-10 pr-6 py-5 bg-white shadow-md hover:shadow-xl">
              <div>
                <h1 class = "font-semibold text-grey text-sm">${data[i].fields.date}</h1>
                <h1 class = "text-lg font-bold">${data[i].fields.title}</h1>
                <p class="text-gray-700 text-base mb-4">
                  ${data[i].fields.abstract}
                </p>
              </div>
      
              <div class="flex justify-between">
                ${data[i].fields.emotion == 1 ?
                    `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Senang</span>` :
                    ``
                }
                ${data[i].fields.emotion == 2 ?
                    `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Biasa</span>` :
                    ``
                }
                ${data[i].fields.emotion == 3 ?
                    `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Sedih</span>` :
                    ``
                }
                ${data[i].fields.emotion == 4 ?
                    `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Marah</span>` :
                    ``
                }
                <div>
                  <td><button id="baca" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" data-bs-toggle="modal" data-bs-target="#modalBaca--${data[i].pk}">Baca</button></td>
                  <td><button class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" onclick="hapusTugas(${data[i].pk})"><i class="bi bi-trash-fill"></i>Hapus</button></td>
                </div>
              </div>
            </div>
            
            <div class="modal fade" id="modalBaca--${data[i].pk}" tabindex="-1" role="dialog" aria-labelledby="createTaskModalLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class = "font-semibold text-grey text-sm">${data[i].fields.date}</h1>
                    <h5 class="modal-title text-black font-bold" id="createTaskModalLabel">${data[i].fields.title}</h5>
                    <div class="flex justify-between">
                      ${data[i].fields.emotion == 1 ?
                          `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Senang</span>` :
                          ``
                      }
                      ${data[i].fields.emotion == 2 ?
                          `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Biasa</span>` :
                          ``
                      }
                      ${data[i].fields.emotion == 3 ?
                          `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Sedih</span>` :
                          ``
                      }
                      ${data[i].fields.emotion == 4 ?
                          `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Marah</span>` :
                          ``
                      }
                    </div>
                  </div>
                  <div class="modal-body">
                    <p class="text-gray-700 text-base mb-4">
                      ${data[i].fields.abstract}
                    </p>

                    <p class="text-black text-base mb-4">
                      ${data[i].fields.description}
                    </p>
                  </div>
                </div>
              </div>
            </div>`
          );
        }
      });

      $("#tambah").click(function(){
        $.post( "/diarybund/create-ajax/", {title : $("#title").val(), description : $("#description").val(), abstract : $("#abstract").val(), emotion : $("#emotion").val()}, function(data, status) {
          if (status == "success") {
            $('#diarybund').append(
              `<div id = "${data.pk}--tugas" class = "rounded-lg pl-10 pr-6 py-5 bg-white shadow-md hover:shadow-xl">
                <div>
                  <h1 class = "font-semibold text-grey text-sm">${data.fields.date}</h1>
                  <h1 class = "text-lg font-bold">${data.fields.title}</h1>
                  <p class="text-gray-700 text-base mb-4">
                    ${data.fields.abstract}
                  </p>
                </div>
        
                <div class="flex justify-between">
                  ${data.fields.emotion == 1 ?
                      `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Senang</span>` :
                      ``
                  }
                  ${data.fields.emotion == 2 ?
                      `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Biasa</span>` :
                      ``
                  }
                  ${data.fields.emotion == 3 ?
                      `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Sedih</span>` :
                      ``
                  }
                  ${data.fields.emotion == 4 ?
                      `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Marah</span>` :
                      ``
                  }
                  <div>
                    <td><button id="baca" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" data-bs-toggle="modal" data-bs-target="#modalBaca--${data.pk}">Baca</button></td>
                    <td><button class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" onclick="hapusTugas(${data.pk})"><i class="bi bi-trash-fill"></i>Hapus</button></td>
                  </div>
                </div>
              </div>
              
              <!-- Modal Baca Selengkapnya -->
              <div class="modal fade" id="modalBaca--${data.pk}" tabindex="-1" role="dialog" aria-labelledby="createTaskModalLabel" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h1 class = "font-semibold text-grey text-sm">${data.fields.date}</h1>
                      <h5 class="modal-title text-black font-bold" id="createTaskModalLabel">${data.fields.title}</h5>
                      <div class="flex justify-between">
                        ${data.fields.emotion == 1 ?
                            `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Senang</span>` :
                            ``
                        }
                        ${data.fields.emotion == 2 ?
                            `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Biasa</span>` :
                            ``
                        }
                        ${data.fields.emotion == 3 ?
                            `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Sedih</span>` :
                            ``
                        }
                        ${data.fields.emotion == 4 ?
                            `<span class = "text-sm sm:text-md bg-black text-white py-2 px-3 sm: px-3 rounded-full">Marah</span>` :
                            ``
                        }
                      </div>
                    </div>
                    <div class="modal-body">
                      <p class="text-gray-700 text-base mb-4">
                        ${data.fields.abstract}
                      </p>

                      <p class="text-black text-base mb-4">
                        ${data.fields.description}
                      </p>
                    </div>
                  </div>
                </div>
              </div>`
            )
            $('#title').val('')
            $('#description').val('')
            $('#abstract').val('')
          }
        })
      })

      hapusTugas = (idTugas) => {
        $.ajax({
          url: `/diarybund/delete/${idTugas}`,
          type: 'DELETE',
          success: function(response){
            $(`#${idTugas}--tugas`).remove()
          }
        })
      }
    }
  });