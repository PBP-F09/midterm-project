function addAnswer(id) {
    $.post(
        `/qna/answer/${id}`,
        {
            text: $(`#input-answer-${id}`).val(),
        },
        function (data, status) {
            if (status == 'success') {
                $(`#quest-answers-${id}`).append(answerCard(data))
                $(`#input-answer-${id}`).val('')
            }
        },
    )
}