// navbar
function openNav() {
    document.getElementById("mySidebar").style.width = "350px"
}

function closeNav() {
    document.getElementById("mySidebar").style.width = "0"
}

document.getElementById('search-icon').addEventListener('click', function() {
    document.getElementById('search-form').submit()
});