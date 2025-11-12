// 2-script.js

// Sélectionne le tag avec l'id 'red_header'
const redHeader = document.querySelector('#red_header');

// Ajoute un écouteur d'événement "click" sur cet élément
redHeader.addEventListener('click', function () {
  // Quand on clique, ajoute la classe 'red' au header
  document.querySelector('header').classList.add('red');
});
