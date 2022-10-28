const getData = (data) => {
	let content = "";
	data.forEach((item) => {
		let artikel = item.fields;
		// let readMore = "";
		let isi = artikel.isi;
		if (artikel.isi.length > 200) {
			// readMore = "read more";
			isi = artikel.isi.substring(0, 200) + "...";
		}
		content += `
            <div class="w-[50rem] bg-[#CFB997] p-5 m-2 rounded-xl border-2 border-red-400 hover:scale-105 duration-200">
                <h1 class="font-bold text-lg">${artikel.judul}</h1>
                <p>${isi}</p>
                <a target="_blank" href="/artikel-kesehatan/artikel/${item.pk}" class="hover:cursor-pointer"><button class="bg-blue-500 hover:bg-blue-700 my-2 py-2 px-4 text-white rounded-lg">Read More</button></a>
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
