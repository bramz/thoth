class Journal {
    data: string
    constructor(public id: number, public date: string, public title: string, public name: string) {
        this.data = id + " " + date+ " " + title + " " + name
    }
}

interface Page {
    id: number
    date: string
    title: string
    name: string
}

function display(page: Page) {
    return "ID: " + page.id + " Date: " + page.date + " Title: " + page.title + " Name: " + page.name
}

let journal = new Journal(1, "0000-00-00", "page title", "test journal")

document.body.innerHTML = display(journal)
