let createEntry = () => {
    document.body.innerHTML +=
       `
      <div id="entry" class="paper">
        <div class="entry">
          <form action="/entry" method="POST">
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
        console.log(JSON.stringify(payload))
        fetch('/entry', {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(payload)
        })
          .then(resp=>resp.text)
          .then(text=>console.log(text))
    })
}

window.addEventListener('DOMContentLoaded', (event) => {
    createEntry()
})