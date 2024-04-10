window.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    if (window.scrollY > 300) {
        navbar.classList.add('blue');
        navbar.classList.remove('transparent');
    } else {
        navbar.classList.remove('blue');
        navbar.classList.add('transparent');
    }
});
