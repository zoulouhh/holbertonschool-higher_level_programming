// 7-script.js

// URL de l'API SWAPI pour la liste des films
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Utilisation de la Fetch API
fetch(url)
  .then(response => response.json()) // Convertit la réponse en JSON
  .then(data => {
    // Sélectionne la liste <ul id="list_movies">
    const movieList = document.querySelector('#list_movies');

    // Parcourt chaque film reçu et crée un élément <li> avec le titre
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  })
  .catch(error => console.error('Erreur :', error)); // Gère les erreurs
