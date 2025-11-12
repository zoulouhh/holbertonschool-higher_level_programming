// 4-script.js

// Sélectionne le bouton ou div qui déclenche l’action
const addItem = document.querySelector('#add_item');

// Ajoute un écouteur d’événement "click"
addItem.addEventListener('click', function () {
  // Sélectionne la liste <ul> avec la classe "my_list"
  const myList = document.querySelector('.my_list');

  // Crée un nouvel élément <li>
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';

  // Ajoute le nouvel élément à la liste
  myList.appendChild(newItem);
});
