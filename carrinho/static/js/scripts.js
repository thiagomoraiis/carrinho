/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
// pega os elementos HTML
const decrementButton = document.querySelector('#decrement');
const incrementButton = document.querySelector('#increment');
const countInput = document.querySelector('#count');

// adiciona o comportamento de decremento ao botão de decremento
numero = 1;

function less() {
  numero--;
  setValue(numero);
}

function more() {
  numero++;
  setValue(numero);
}

function setValue(value) {
  document.getElementById('num').value = value;
}

setValue(numero);