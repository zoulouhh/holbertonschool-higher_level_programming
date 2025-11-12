// 6-script.js

// URL de l'API SWAPI pour le personnage 5 (Leia Organa)
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Utilise la Fetch API pour récupérer les données
fetch(url)
  .then(response => response.json()) // Convertit la réponse en JSON
  .then(data => {
    // Sélectionne la balise avec id "character"
    const characterElement = document.querySelector('#character');
    // Met à jour le texte avec le nom du personnage
    characterElement.textContent = data.name;
  })
  .catch(error => console.error('Erreur :', error)); // Gère les erreurs
