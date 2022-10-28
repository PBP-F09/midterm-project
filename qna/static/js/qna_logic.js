$(document).ready(function () {
    loadData();

    $('#add-question').click(function () {
        $.post(
            '/qna/add/',
            {
                text: $('#text').val(),
            },
            function (data, status) {
                if (status == 'success') {
                    $(`#quest`).append(questionCard(data))
                    $('#text').val('')
                }
            },
        )
    })
});

function deleteQuestion(id) {
    $.ajax({
        url: `/qna/delete/${id}`,
        type: 'DELETE',
        success: function (result) {
            $(`#quest-${id}`).remove()
        },
        error: function (result){
            alert("Tidak dapat menghapus post orang lain!")
        }
    });
}

function deleteAnswer(id) {
    $.ajax({
        url: `/qna/delete2/${id}`,
        type: 'DELETE',
        success: function (result) {
            $(`#answer-${id}`).remove()
            if ($(`#quest-answers-${result}`).children().length == 0){
                $(`#no-answer-${result}`).text('No answer yet.')
            }

        },
        error: function (result){
            alert("Tidak dapat menghapus post orang lain!")
        }
    });
}

function addAnswer(id) {
    $.post(
        `/qna/answer/${id}`,
        {
            text: $(`#input-answer-${id}`).val(),
        },
        function (data, status) {
            if (status == 'success') {
                $(`#quest-answers-${id}`).append(answerCard(data))
                $(`#no-answer-${id}`).text('')
                $(`#input-answer-${id}`).val('')
            }
        },
    )
}

function loadData() {
    $.get(`/qna/json`, function (data) {
        for (var i = 0; i < data.length; i++) {
            $(`#quest`).append(questionCard(data[i]));
        }
    });
    $.get(`/qna/json2`, function (data) {
        for (var i = 0; i < data.length; i++) {
            $(`#no-answer-${data[i].fields.question}`).text('')
            $(`#quest-answers-${data[i].fields.question}`).append(answerCard(data[i]));
        }
    });
}