const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggler = document.querySelector(".theme-toggler");

menuBtn.addEventListener('click',() =>{
    sideMenu.style.display = 'block';

});

closeBtn.addEventListener('click',() =>{
    sideMenu.style.display = 'none';
});

// cambio color
themeToggler.addEventListener('click', () =>{
    document.body.classList.toggle('dark-theme-variables')

    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})

Orders.forEach(order =>{
    const tr = document.createElement('tr')
    const trContent = `
                        <td>${order.productName}</td>
                        <td>${order.productNumber}</td>
                        <td>${order.formaPago}</td>
                        <td>${order.precioJuego}</td>
                        <td class="${order.paymentStatus === 'Cancelado' ? 'danger' : order.paymentStatus === 'Pendiente' ? 'warning' : 'success'}">${order.paymentStatus}</td>
                        <td class="primary">Detalles</td>
                        `;
    tr.innerHTML = trContent;
    document.querySelector('table tbody').appendChild(tr);                   
})