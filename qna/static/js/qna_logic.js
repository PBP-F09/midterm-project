$(document).ready(function () {
    loadData();

    $('#add-questions').click(function () {
        $.post(
            '/qna/add/',
            {
                text: $('#text').val(),
                role_user: $('#role_user').val(),
            },
            function (data, status) {
                if (status == 'success') {
                    $(`#quest`).prepend(questionCard(data))
                    $('#text').val('')
                    const toast = new bootstrap.Toast($('#liveToast2'))
                    toast.show()

                }
            },
        )
    })
});

function useToast() {
    const toast = new bootstrap.Toast($('#liveToast')[0])
    toast.show()
}

function deleteQuestion(id) {
    $.ajax({
        url: `/qna/delete/${id}`,
        type: 'DELETE',
        success: function (result) {
            $(`#quest-${id}`).addClass("animate-scale-down-center")
            setTimeout(function () { $(`#quest-${id}`).remove(); }, 225)
        },
        error: function useToast() {
            const toast = new bootstrap.Toast($('#liveToast'))
            toast.show()
        }
    });
}

function showAnswer(id) {
    $(`#all-answers-${id}`).removeClass('hidden');
}

function deleteAnswer(id) {
    $.ajax({
        url: `/qna/delete2/${id}`,
        type: 'DELETE',
        success: function (result) {
            $(`#answer-${id}`).remove()
            if ($(`#quest-answers-${result.id}`).children().length == 0){
                $(`#no-answer-${result.id}`).text('No answer yet.')
            }
            $(`#total-answers-${result.id}`).text(result.total_answer)

        },
        error: function useToast() {
            const toast = new bootstrap.Toast($('#liveToast'))
            toast.show()
        }
    });
}

function addAnswer(id, role_user) {
    $.post(
        `/qna/answer/${id}`,
        {
            text: $(`#input-answer-${id}`).val(),
            role_user: $('#role_user2').text(),
        },
        function (data, status) {
            if (status == 'success') {
                $(`#quest-answers-${id}`).append(answerCard(data))
                $(`#no-answer-${id}`).text('')
                $(`#total-answers-${id}`).text(data.fields.total_answer)
                $(`#input-answer-${id}`).val('')
            }
        },
    )
}

async function loadData() {
    await $.get(`/qna/json`, function (data) {
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

function likeQuestion(id) {
    $.ajax({
        url: `/qna/like/${id}`,
        type: 'PATCH',
        success: function (data) {
            $(`#total-likes-${id}`).text(data.total_like)
        }
    });
}