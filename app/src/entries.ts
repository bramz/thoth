let getEntries = () => {
    fetch('/entries', {method: 'GET'})
        .then(response => response.json())
        .then(data => showEntries(data))
        .catch(error => console.log(error))
}

let showEntries = (data: any) => {
    document.body.innerHTML +=
        `<div class="paper">
           <ul>
             <li>${data.id}&colon; <a href="#">${data.title}</a></li>
         </div>
         <div class="book-footing">
             <a href="#">&lt;&lt; Last</a> &verbar; <a href="#">Next &gt;&gt;</a>
         </div>
        `
}

window.addEventListener('DOMContentLoaded', (event) => {
    getEntries()
})