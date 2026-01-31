function icon() {
    let bar = document.getElementById('bar');
    let tablet = document.getElementById('tablet').style.display = '';
    let nav1 = document.getElementById('navbar').style.display = 'block';
    let nav = document.getElementById('navbar').style.right = '0px';
}

function closei() {
    let nav1 = document.getElementById('navbar').style.display = 'none';
    let tablet = document.getElementById('tablet').style.display = 'block';
}

function oneImg() {
    let oneimg = document.getElementById('mainImg').src = '../static/Images/products/f1.jpg';
}

function twoImg() {
    let oneimg = document.getElementById('mainImg').src = '../static/Images/products/f2.jpg';
}

function threeImg() {
    let oneimg = document.getElementById('mainImg').src = "../static/Images/products/f3.jpg";
}

function fourImg() {
    let oneimg = document.getElementById('mainImg').src = '../static/Images/products/f4.jpg';
}

function submit() {
    let form = document.getElementById('formvalidate');
    let print = document.getElementById('print');
    form.style.display = 'none';
    print.innerHTML = "Thank you";
}

