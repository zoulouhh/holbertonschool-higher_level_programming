// Select the element with id "update_header" and the header element
const updateHeaderButton = document.getElementById('update_header');
const header = document.querySelector('header');

// Add a click event listener to the update_header element
updateHeaderButton.addEventListener('click', function() {
  // Update the text content of the header element
  header.textContent = 'New Header!!!';
});