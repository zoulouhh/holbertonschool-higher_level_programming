// 3-script.js

// Sélectionne l’élément qui déclenche le changement
const toggleHeader = document.querySelector('#toggle_header');

// Ajoute un écouteur d’événement "click"
toggleHeader.addEventListener('click', function () {
  const header = document.querySelector('header');

  // Si le header a la classe "red", on la remplace par "green"
  if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  } 
  // Sinon, on remplace "green" par "red"
  else {
    header.classList.replace('green', 'red');
  }
});
