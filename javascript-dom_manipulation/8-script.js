// 8-script.js

// Exécute le code uniquement quand le DOM est prêt
document.addEventListener('DOMContentLoaded', function () {
  // URL de l'API HelloSalut (français)
  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  // Utilisation de la Fetch API
  fetch(url)
    .then(response => response.json()) // Convertit la réponse en JSON
    .then(data => {
      // Sélectionne l'élément avec id="hello"
      const helloElement = document.querySelector('#hello');
      // Met le texte reçu dans la page
      helloElement.textContent = data.hello;
    })
    .catch(error => console.error('Erreur :', error)); // Gère les erreurs
});
