let userRegister = () => {
    document.body.innerHTML +=
        `
        <div id="login" class="paper">
          <form action="/register" method="post">
            <div class="login">
              <ul>
                <li><label for="username">Username:</label></li>
                <li><input type="text" id="username"></li>
                <li><label for="password">Password:</label></li>
                <li><input type="password" id="password"></li>
                <li><input type="button" id="register" value="Register"></li>
              </ul>
            </div>
          </form>
        </div>
        `

    let userCreate = (document.getElementById('register') as any).addEventListener('click', () => {
      let credentials = {
        'username': (document.getElementById('username') as any).value,
        'password': (document.getElementById('password') as any).value,
        'active': 1
      }
      
      fetch('/register', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
      })
        .then(resp=>resp.text)
        .then(text=> {
          console.log(text)
          /*
          if (text == 'success') {
            document.location.replace('/')
          } else {
            document.location.reload()
          }
          */
        })  
    })
}

window.addEventListener('DOMContentLoaded', (event) => {
    userRegister()
})