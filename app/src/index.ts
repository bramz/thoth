let get_page = () => {
    fetch('/page', {method: 'GET'})
        .then(response => response.json())
        .then(data => callback(data))
        .catch(error => console.log(error))
}

let callback = (data: any) => {
    console.log(data)
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
    get_page()
})