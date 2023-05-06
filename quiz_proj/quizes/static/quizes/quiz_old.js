console.log('Hello world')
const url = window.location.href

const quizBox = document.getElementById('quiz-box')
// let data

$.ajax({
    type: 'GET',
    // url: url,
    url: `${url}data`,
//мы берем текущую страницу квиза, задаем маршрут из урлов
    success: function (response){
        // console.log(response)
        const data = response.data
//        тут можно задать конст потому что в JS свойства менять можно
//свойство дата содержит массив вопросов и ответов к ним
//а выводится этот массив по гет запросы на опеределенный квиз
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                // console.log(question)
                // console.log(answers)
                quizBox.innerHTML += `
<!--здесь мы ставим += потому что выводится несколько вопросов-->
                <hr>
                <div class="mb-2">
                     <b>${question}</b>
                </div>
                `
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                      <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <label for="${question}">${answer}</label>
<!--аттрибут for в label связан с айти в input
    !!! чувствительно к регистру
если не задать label то тест ответов выводиться не будет
Атрибут name (HTML тега <input>) задает имя для элемента.-->
                      </div>
                    `
                })
            }
//Object.entries возвращает многомерный массив с парами ключ значение
        });
    },
    error: function (error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-from')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
//Скрытое поле формы с именем csrfmiddlewaretoken, присутствует во всех
// исходящих формах POST. Значение этого поля, опять же, является значением
// секрета с маской, которая добавляется к нему и используется для
// его шифрования.
// const elements = [...document.getElementsByClassName('ans')]

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    //тут у нас в элементах вопросы и ответы
    const data = {}
    //объявление словаря данных
    data['csrfmiddlewaretoken'] = csrf[0].value
    //здесь мы берем значение токена (хз зачем но надо)
    elements.forEach(el=>{
        if (el.checked) {
            //условие если ответ был выбран
            data[el.name] = el.value
        //    сохранение в виде вопрос: выбранный ответ
        } else {
            if (!data[el.name]) {
        // если у нас нет вопроса
                data[el.name] = null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
//здесь обязательно надо слэш поставить иначе будет ошибка
        data: data,
        success: function (response){
            //здесь идёт обработка самого запроса
            console.log(response)
        },
        error: function (error){
            console.log(error)
    }
    })
}

quizForm.addEventListener('submit', e=>{
    //тип submit срабатывает при отправке валидной формы
    e.preventDefault()
// preventDefault() — метод события. Этот метод отменяет поведение браузера
//     по умолчанию, которое происходит при обработке события.
// Например, при нажатии на ссылку, мы переходим по адресу этой ссылки.
//         Вызов preventDefault() отменит это поведение.

    sendData()
})
