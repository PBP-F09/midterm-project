function menu(e){
    let list = document.getElementById('list-navbar');
    e.name === 'menu' ? (e.name = "close", list.classList.remove('hidden')) :( e.name = "menu", list.classList.add('hidden'))
}