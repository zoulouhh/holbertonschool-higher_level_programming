// 5-script.js

// Sélectionne l’élément déclencheur
const updateHeader = document.querySelector('#update_header');

// Ajoute un écouteur d’événement "click"
updateHeader.addEventListener('click', function () {
  // Sélectionne le header et change son contenu texte
  document.querySelector('header').textContent = 'New Header!!!';
});
