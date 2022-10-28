const questionCard = (data) =>
            `<div class="flex" id="quest-${data.pk}">
                <div class="flex-shrink-0 mr-3">
                    <img class="mt-2 rounded-full w-8 h-8 sm:w-10 sm:h-10" src="https://cdn-icons-png.flaticon.com/512/709/709722.png" alt="">
                </div>
                <div class="flex-1 border rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed">
                    <div class="flex justify-between">
                        <span class="text-xs text-gray-400 mt-0">${data.fields.date}</span>
                        <ion-icon name="trash-outline" id="delete-icon" class="cursor-pointer" onclick="deleteQuestion(${data.pk})"></ion-icon>
                    </div>
                    <strong>${data.fields.user}</strong>
                    <p class="text-sm">${data.fields.text}</p>

                    <div class="flex justify-between items-center">
                        <form action="" method="POST" class="w-full">
                            {% csrf_token %}
                            {% if user.is_authenticated %}
                            <input type="text" name="title" id="input-answer-${data.pk}"
                            class="form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 my-3"
                            placeholder="Jawab di sini">
                            {% else %}
                            <input type="text" name="title" id="input-answer-${data.pk}" aria-label="disabled input"
                            class="form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 my-3"
                            placeholder="Login untuk menjawab" disabled>
                            {% endif %}
                        </form>
                    
                        {% if user.is_authenticated %}
                        <button type="submit" class="ml-1 inline-flex justify-center p-2 text-blue-600 rounded-full cursor-pointer hover:bg-blue-100" onclick="addAnswer(${data.pk})">
                            <svg aria-hidden="true" class="w-6 h-6 rotate-90" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"></path></svg>
                        </button>
                        {% endif %}
                    </div>
                    
                    <h4 class="my-5 uppercase tracking-wide text-gray-400 font-bold text-xs">Answers</h4>

                    <h6 class="text-sm" id='no-answer-${data.pk}'>No answer yet.</h6>

                    <div class="space-y-4" id='quest-answers-${data.pk}'></div>
            
                </div>
            </div>`
        
        const answerCard = (data) =>
            `<div class="flex" id='answer-${data.pk}'>
                <div class="flex-shrink-0 mr-3">
                    <img class="mt-3 rounded-full w-6 h-6 sm:w-8 sm:h-8"
                        src="https://cdn-icons-png.flaticon.com/512/709/709722.png" alt="">
                </div>
                <div class="flex-1 bg-gray-100 rounded-lg px-4 py-2 sm:px-6 sm:py-4 leading-relaxed">
                    <div class="flex justify-between">
                        <span class="text-xs text-gray-400">${data.fields.date}</span>
                        <ion-icon name="trash-outline" id="delete-icon" class="cursor-pointer" onclick="deleteAnswer(${data.pk})"></ion-icon>
                    </div>
                    <strong>${data.fields.user}</strong> 
                    <p class="text-xs sm:text-sm">${data.fields.text}</p>
                </div>
            </div>`