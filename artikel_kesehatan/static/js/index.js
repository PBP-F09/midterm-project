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
				<a target="_blank" href="/artikel-kesehatan/artikel/${item.pk}" class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
					Read more
					<svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
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
