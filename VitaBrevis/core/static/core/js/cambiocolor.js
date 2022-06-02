const themeToggler = document.querySelector(".theme-toggler");
const themeToggler2 = document.querySelector(".theme-toggler2");
themeToggler.addEventListener('click', () =>{
    document.body.classList.toggle('dark-theme-variables')

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})




themeToggler2.addEventListener('click', () =>{
    document.body.classList.toggle('dark-theme-variables')

    themeToggler2.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler2.querySelector('span:nth-child(2)').classList.toggle('active');
})
