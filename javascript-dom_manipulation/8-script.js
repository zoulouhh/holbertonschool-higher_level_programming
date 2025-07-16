// Wait for the DOM to be fully loaded before executing
document.addEventListener('DOMContentLoaded', function() {
  // Select the HTML element with id "hello"
  const helloElement = document.getElementById('hello');
  
  // Fetch data from the Hello API with French language parameter
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      // Parse the JSON response
      return response.json();
    })
    .then(data => {
      // Extract the hello value from the data
      const helloText = data.hello;
      
      // Display the hello text in the HTML element
      helloElement.textContent = helloText;
    })
    .catch(error => {
      // Handle any errors that occurred during fetch
      console.error('Error fetching hello data:', error);
      helloElement.textContent = 'Error loading greeting';
    });
});