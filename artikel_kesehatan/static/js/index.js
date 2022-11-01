const getData = (data) => {
	let content = "";
	data.forEach((item) => {
		let artikel = item.fields;
		let isi = artikel.isi;
		if (artikel.isi.length > 200) {
			isi = artikel.isi.substring(0, 200) + "...";
		}
		content += `
			<div class="p-6 w-96 m-2 hover:scale-105 duration-200 max-w-sm bg-cream-muda rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
				<a target="_blank" href="/artikel-kesehatan/artikel/${item.pk}">
					<h5 class="mb-2 text-lg lg:text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${artikel.judul}</h5>
				</a>
				<p class="mb-3 text-sm lg:text-md font-normal text-gray-700 dark:text-gray-400">${isi}</p>
				<div class="flex flex-row justify-between items-center">
					<a target="_blank" href="/artikel-kesehatan/artikel/${item.pk}" class="bg-merah-tua hover:bg-merah-muda w-fit text-white p-2 font-bold rounded-lg flex items-center justify-center">
						Read more
						<i class="fa fa-arrow-circle-right ml-2" style="font-size:20px;color:white"></i>
					</a>
					<a href="/artikel-kesehatan/hapus/${item.pk}" class="text-sm sm:text-md hover:cursor-pointer bg-merah-tua hover:bg-merah-muda hover:bg-light_blue text-blue font-semibold hover:text-blue py-2 px-2 border border-cream-tua hover:border-cream-tua rounded">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white" class="w-5 h-5">
							<path fill-rule="evenodd" d="M16.5 4.478v.227a48.816 48.816 0 013.878.512.75.75 0 11-.256 1.478l-.209-.035-1.005 13.07a3 3 0 01-2.991 2.77H8.084a3 3 0 01-2.991-2.77L4.087 6.66l-.209.035a.75.75 0 01-.256-1.478A48.567 48.567 0 017.5 4.705v-.227c0-1.564 1.213-2.9 2.816-2.951a52.662 52.662 0 013.369 0c1.603.051 2.815 1.387 2.815 2.951zm-6.136-1.452a51.196 51.196 0 013.273 0C14.39 3.05 15 3.684 15 4.478v.113a49.488 49.488 0 00-6 0v-.113c0-.794.609-1.428 1.364-1.452zm-.355 5.945a.75.75 0 10-1.5.058l.347 9a.75.75 0 101.499-.058l-.346-9zm5.48.058a.75.75 0 10-1.498-.058l-.347 9a.75.75 0 001.5.058l.345-9z" clip-rule="evenodd"/>
						</svg>
					</a> 
				</div>
			</div>
        `;
	});
	return content;
};

const postData = (judul, isi) => {
	let csrftoken = $("input[name=csrfmiddlewaretoken]").val();
	return $.post(
		"/artikel-kesehatan/tambah-artikel/",
		{
			judul: judul,
			isi: isi,
			csrfmiddlewaretoken: csrftoken,
		},
		function () {
			$.get("/artikel-kesehatan/json/", function (data, status) {
				let content = getData(data);
				$(".content").html(content);
			});
		}
	);
};
