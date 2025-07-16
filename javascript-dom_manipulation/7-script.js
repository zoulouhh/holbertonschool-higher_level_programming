// Select the HTML ul element with id "list_movies"
const listMoviesElement = document.getElementById('list_movies');

// Fetch data from the Star Wars API films endpoint
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    // Check if the response is successful
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    // Parse the JSON response
    return response.json();
  })
  .then(data => {
    // Extract the results array containing the movies
    const movies = data.results;
    
    // Loop through each movie and create a list item for its title
    movies.forEach(movie => {
      // Create a new li element
      const listItem = document.createElement('li');
      
      // Set the text content to the movie title
      listItem.textContent = movie.title;
      
      // Append the list item to the ul element
      listMoviesElement.appendChild(listItem);
    });
  })
  .catch(error => {
    // Handle any errors that occurred during fetch
    console.error('Error fetching movie data:', error);
    
    // Display error message in the list
    const errorItem = document.createElement('li');
    errorItem.textContent = 'Error loading movie data';
    listMoviesElement.appendChild(errorItem);
  });