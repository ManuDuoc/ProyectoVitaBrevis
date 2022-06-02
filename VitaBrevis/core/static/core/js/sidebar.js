const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
let sidebar = document.querySelector("#sidebar");

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#content').toggleClass('active');
    });
    
     $('.more-button,.body-overlay').on('click', function () {
        $('#sidebar,.body-overlay').toggleClass('show-nav');
    });
    
});