const getData = (data) => {
	let content = "";
	data.forEach((item) => {
		let artikel = item.fields;
		let isi = artikel.isi;
		if (artikel.isi.length > 200) {
			isi = artikel.isi.substring(0, 200) + "...";
		}
		content += `
			<div class="p-6 w-[50rem] m-2 hover:scale-105 duration-200 max-w-sm bg-cream-muda rounded-lg border border-gray-200 shadow-md dark:bg-gray-800 dark:border-gray-700">
				<a target="_blank" href="/artikel-kesehatan/artikel/${item.pk}">
					<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">${artikel.judul}</h5>
				</a>
				<p class="mb-3 font-normal text-gray-700 dark:text-gray-400">${isi}</p>
				<a target="_blank" href="/artikel-kesehatan/artikel/${item.pk}" class="bg-merah-tua hover:bg-merah-muda w-fit text-white p-2 font-bold rounded-lg flex items-center justify-center">
					Read more
					<i class="fa fa-arrow-circle-right ml-2" style="font-size:20px;color:white"></i>
				</a>
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
