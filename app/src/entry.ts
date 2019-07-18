function getCookie(name: string) {
  let cookieValue = null
  if (document.cookie && document.cookie != '') {
    let cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
          break
      }
    }
  }
  return cookieValue
}

let createEntry = () => {
    document.body.innerHTML +=
       `
      <div id="entry" class="paper">
        <div class="entry">
          <form action="/entry/" method="post">
            <ul>
              <li><label for="title">Title:</label></li>
              <li><input type="text" id="title" size="80"></li>
              <li><label for="content">Content:</label></li>
              <li><textarea rows="25" cols="80" id="content"></textarea></li>
              <li><input type="button" id="write" value="Write"></li>
            </ul>
          </form>
        </div>
      </div>
        `
    let addEntry = (document.getElementById('write') as any).addEventListener('click', () => {
        let payload = {
            'title': (<HTMLInputElement>document.getElementById('title') as any).value,
            'content': (<HTMLInputElement>document.getElementById('content') as any).value
        }

        let requestHeaders: any = {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        }

        fetch('/entries/entry/', {
          method: 'POST',
          headers: requestHeaders,
          body: JSON.stringify(payload)
        })
          .then(resp=>resp.text)
          .then(text=>console.log(text))
    })
}

window.addEventListener('DOMContentLoaded', (event) => {
    createEntry()
})