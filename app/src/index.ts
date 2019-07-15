import Logrocket from 'logrocket'

Logrocket.init('lawtjy/thoth')


let getPage = () => {
    fetch('/page', {method: 'GET'})
        .then(response => response.json())
        .then(data => callBack(data))
        .catch(error => console.log(error))
}


let callBack = (data: any) => {
    document.body.innerHTML +=
        `<div class="paper">
             <h1>${data.title}</h1>
             <h2>${data.date}</h2>
             <p>${data.content}</p>
         </div>
         <div class="book-footing">
             <a href="#">&lt;&lt; Last</a> &verbar; <a href="#">Next &gt;&gt;</a>
         </div>
        `
}

window.addEventListener('DOMContentLoaded', (event) => {
    getPage()
})