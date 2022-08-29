var search_bar = document.getElementById('search-bar');
var query = document.getElementById('query');

search_bar.addEventListener('keydown', (event) => {
    if (event.code == 'Enter') {
        if (enable()) {
            search();
        }
        clear();
    }
 });

function enable() {
    if (query.value <= 0) {
        return false;
    }
    return true;
}

function search() {
    var url = 'https://www.google.com/search?client=raspberry&q=' + query.value;
    window.open(url, "_SELF");
}

function clear() {
    return query.value = '';
}

var appsButton = document.getElementById('apps-button');
var menu = document.getElementById('apps-menu');

appsButton.addEventListener('click', () => {
    if (menu.style.display == 'none') {
        menu.style.display = 'flex';
        menu.style.flexWrap = 'wrap';
        menu.style.justifyContent = 'end';        
    } else {
        menu.style.display = 'none';
    }
});

