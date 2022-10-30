function useAlert() {
  const toast = new bootstrap.Toast($('#toastAlert')[0])
  toast.show()
}

function useSuccess() {
  const toast = new bootstrap.Toast($('#toastSuccess')[0])
  toast.show()
}

function editDiary(id) {
  $.post(`/diarybund/edit/${id}`,
    {
      title : $(`#title--${id}`).val(), 
      description : $(`#description--${id}`).val(), 
      abstract : $(`#abstract--${id}`).val(), 
      emotion : $(`#emotion--${id}`).val()
    },
    function (data, status) {
      if (data.hasOwnProperty('error')) {
        useAlert()
      } else {
        useSuccess()
        for (let i = 0; i < 2; i++) {
          $(`#${id}--title${i}`).text(`${data.fields.title}`)
          $(`#${id}--abstract${i}`).text(`${data.fields.abstract}`)
          $(`#${id}--description${i}`).text(`${data.fields.description}`)
          if (data.fields.emotion == 1) {
            $(`#${id}--emotion${i}`).text(`Senang`)
          } else if (data.fields.emotion == 2) {
            $(`#${id}--emotion${i}`).text(`Biasa`)
          } else if (data.fields.emotion == 3) {
            $(`#${id}--emotion${i}`).text(`Sedih`)
          } else {
            $(`#${id}--emotion${i}`).text(`Marah`)
          }
        }
        $(`#modalUbah--${data.pk}`).modal('hide')
      }
    },
  )
}

hapusTugas = (idTugas) => {
  $.ajax({
    url: `/diarybund/delete/${idTugas}`,
    type: 'DELETE',
    success: function(response){
      $(`#${idTugas}--tugas`).remove()
    }
  })
}

parseDate = (d) => {
  let date = new Date(d);        
  var mm = date.getMonth() + 1; // getMonth() adalah zero-based
  var dd = date.getDate();

  let newdate = [date.getFullYear() + '-',
                (mm>9 ? '' : '0') + mm + '-',
                (dd>9 ? '' : '0') + dd,
                ].join('');
  return newdate;
}

function cardDiary(id) {
      $('#diarybund').append(
        `<div id = "${id.pk}--tugas" class = "rounded-lg pl-6 pr-6 py-5 bg-cream-muda shadow-md hover:shadow-xl">
          <div>
            <h1 class = "font-semibold text-grey text-sm">${parseDate(id.fields.date)}</h1>
            <h1 id = "${id.pk}--title0" class = "text-lg font-bold">${id.fields.title}</h1>
            <p id = "${id.pk}--abstract0" class="text-merah-muda text-base mb-4">
              ${id.fields.abstract}
            </p>
          </div>
    
          <div class="flex justify-between">
            ${id.fields.emotion == 1 ?
                `<span id = "${id.pk}--emotion0" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Senang</span>` : ``
            }
            ${id.fields.emotion == 2 ?
                `<span id = "${id.pk}--emotion0" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Biasa</span>` : ``
            }
            ${id.fields.emotion == 3 ?
                `<span id = "${id.pk}--emotion0" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Sedih</span>` : ``
            }
            ${id.fields.emotion == 4 ?
                `<span id = "${id.pk}--emotion0" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Marah</span>` : ``
            }
            <div>
              <td><button id="baca" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-2 border border-cream-tua hover:border-cream-tua rounded" data-bs-toggle="modal" data-bs-target="#modalBaca--${id.pk}">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
                  <path d="M12 15a3 3 0 100-6 3 3 0 000 6z" />
                  <path fill-rule="evenodd" d="M1.323 11.447C2.811 6.976 7.028 3.75 12.001 3.75c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113-1.487 4.471-5.705 7.697-10.677 7.697-4.97 0-9.186-3.223-10.675-7.69a1.762 1.762 0 010-1.113zM17.25 12a5.25 5.25 0 11-10.5 0 5.25 5.25 0 0110.5 0z" clip-rule="evenodd" />
                </svg>                      
              </button></td>
              <td><button id="edit" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-2 border border-cream-tua hover:border-cream-tua rounded" data-bs-toggle="modal" data-bs-target="#modalUbah--${id.pk}">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
                  <path d="M21.731 2.269a2.625 2.625 0 00-3.712 0l-1.157 1.157 3.712 3.712 1.157-1.157a2.625 2.625 0 000-3.712zM19.513 8.199l-3.712-3.712-12.15 12.15a5.25 5.25 0 00-1.32 2.214l-.8 2.685a.75.75 0 00.933.933l2.685-.8a5.25 5.25 0 002.214-1.32L19.513 8.2z" />
                </svg>                      
              </button></td>
              <td><button class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-2 border border-cream-tua hover:border-cream-tua rounded" onclick="hapusTugas(${id.pk})">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-5 h-5">
                  <path fill-rule="evenodd" d="M16.5 4.478v.227a48.816 48.816 0 013.878.512.75.75 0 11-.256 1.478l-.209-.035-1.005 13.07a3 3 0 01-2.991 2.77H8.084a3 3 0 01-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 01-.256-1.478A48.567 48.567 0 017.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 013.369 0c1.603.051 2.815 1.387 2.815 2.951zm-6.136-1.452a51.196 51.196 0 013.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 00-6 0v-.113c0-.794.609-1.428 1.364-1.452zm-.355 5.945a.75.75 0 10-1.5.058l.347 9a.75.75 0 101.499-.058l-.346-9zm5.48.058a.75.75 0 10-1.498-.058l-.347 9a.75.75 0 001.5.058l.345-9z" clip-rule="evenodd" />
                </svg>
              </button></td>
            </div>
          </div>
        </div>
        
        <!-- Modal Baca -->
        <div class="modal fade" id="modalBaca--${id.pk}" tabindex="-1" role="dialog" aria-labelledby="createTaskModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg modalCenter">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class = "font-semibold text-grey text-sm">${parseDate(id.fields.date)}</h1>
                <h5 id = "${id.pk}--title1" class="modal-title text-black font-bold" id="createTaskModalLabel">${id.fields.title}</h5>
                <div class="flex justify-between">
                  ${id.fields.emotion == 1 ?
                      `<span id = "${id.pk}--emotion1" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Senang</span>` : ``
                  }
                  ${id.fields.emotion == 2 ?
                      `<span id = "${id.pk}--emotion1" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Biasa</span>` : ``
                  }
                  ${id.fields.emotion == 3 ?
                      `<span id = "${id.pk}--emotion1" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Sedih</span>` : ``
                  }
                  ${id.fields.emotion == 4 ?
                      `<span id = "${id.pk}--emotion1" class = "text-sm sm:text-md bg-cream-tua font-semibold text-merah-tua py-2 px-3 sm: px-3 rounded-full">Marah</span>` : ``
                  }
                </div>
              </div>
              <div class="modal-body">
                <p id = "${id.pk}--abstract1" class="text-merah-muda font-semibold text-base mb-4">
                  ${id.fields.abstract}
                </p>
    
                <p id = "${id.pk}--description1" class="text-black text-base mb-4">
                  ${id.fields.description}
                </p>
              </div>
              <div class="modal-footer">
                <button type="button" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" data-bs-dismiss="modal">Tutup</button>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Modal Ubah -->
        <div class="modal fade" id="modalUbah--${id.pk}" tabindex="-1" role="dialog" aria-labelledby="createTaskModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg modalCenter">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title text-black font-bold" id="createTaskModalLabel">Tambah Diary</h5>
              </div>
              <div class="modal-body">
                <form>
                  <div class="mb-3">
                    <label for="title" class="col-form-label">Judul:</label>
                    <input type="text" class="form-control" id="title--${id.pk}" value="${id.fields.title}">
                  </div>
                  <div class="mb-3">
                    <label for="abstract" class="col-form-label">Deskripsi Singkat:</label>
                    <input type="text" class="form-control" id="abstract--${id.pk}" value="${id.fields.abstract}">
                  </div>
                  <div class="mb-3">
                    <label for="description" class="col-form-label">Deskripsi Lengkap:</label>
                    <textarea class="form-control" id="description--${id.pk}">${id.fields.description}</textarea>
                  </div>
                  <div class="mb-3">
                    <label for="emotion">Emosi Si Kecil:</label>
                    <select name="emotion" id="emotion--${id.pk}" value="${id.fields.emotion}" class="form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none">
                      <option value="1">Senang</option>
                      <option value="2">Biasa</option>
                      <option value="3">Sedih</option>
                      <option value="4">Marah</option>
                    </select>
                  </div>
                </form>
              </div>
              <div class="modal-footer">
                <button type="button" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" data-bs-dismiss="modal">Cancel</button>
                <button id="simpan" type="button" class="text-sm sm:text-md bg-transparent hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-3 border border-blue hover:border-blue rounded" onClick="editDiary(${id.pk})">Simpan</button>
              </div>
            </div>
          </div>
        </div>`
      );
    }