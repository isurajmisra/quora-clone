let answers = document.querySelectorAll(".comment-btn")
answers.forEach(element => {

    element.addEventListener('click', showAnswerBox)

    function showAnswerBox(event) {
        event.preventDefault();
        document.querySelector('.form-div').style.display = 'block'
        document.querySelector('#save').addEventListener('click', postForm)
    }
    // function showAnswerBox(event) {
    //     event.preventDefault();
    //     element.style.display = "none"
    //     const comment_div = element.nextElementSibling
    //     const form_field = document.createElement("form")
    //     const text_field = document.createElement("textarea")
    //     text_field.setAttribute('id', 'comment-area')
    //     const submit = document.createElement("button")
    //     submit.addEventListener('click', postForm)
    //     submit.setAttribute('class', submit)
    //     submit.appendChild(document.createTextNode("Post"))
    //     const cancel = document.createElement("button")
    //     cancel.addEventListener('click', cancelPost)
    //     cancel.setAttribute('class', cancel)
    //     cancel.appendChild(document.createTextNode("cancel"))
    //     form_field.appendChild(text_field)
    //     form_field.appendChild(submit)
    //     form_field.appendChild(cancel)
    //     comment_div.appendChild(form_field)
    // }

    function postForm(event) {
        let form = document.querySelector('.post-form')
        let text = document.querySelector("#id_answer_text").value;
        let pk = document.querySelector('#pk').value;
        let csrf = form.firstElementChild.value
        $.ajax({
            type: 'POST',
            url: '/add-answer/',
            contentType: 'application/json;charset=UTF-8',
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            data: {
                'text': text,
                'pk': pk,
                'csrfmiddlewaretoken': csrf,
            },
        });

        form.style.display = 'none'
        document.location.reload(true)
    }

    // function cancelPost(event) {
    //     event.preventDefault();
    //     element.style.display = ""
    //     const comment_div = element.nextElementSibling
    //     comment_div.innerHTML = ""
    // }

})