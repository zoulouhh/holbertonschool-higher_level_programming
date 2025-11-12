// 1-script.js

// Sélectionne le tag avec l'id 'red_header'
const redHeader = document.querySelector('#red_header');

// Ajoute un écouteur d'événement "click" sur cet élément
redHeader.addEventListener('click', function () {
  // Quand on clique, change la couleur du texte du header en rouge
  document.querySelector('header').style.color = '#FF0000';
});
