// Select the HTML element with id "character"
const characterElement = document.getElementById('character');

// Fetch data from the Star Wars API
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    // Check if the response is successful
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Extract the character name from the data
    const characterName = data.name;
    
    // Display the character name in the HTML element
    characterElement.textContent = characterName;
  })
  .catch(error => {
    // Handle any errors that occurred during fetch
    console.error('Error fetching character data:', error);
    characterElement.textContent = 'Error loading character data';
  });