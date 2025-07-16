// Select the element with id "toggle_header" and the header element
const toggleButton = document.getElementById('toggle_header');
const header = document.querySelector('header');

// Add a click event listener to the toggle_header element
toggleButton.addEventListener('click', function() {
  // Check if the header has the 'red' class
  if (header.classList.contains('red')) {
    // If it has 'red', remove it and add 'green'
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    // If it doesn't have 'red' (which means it has 'green'), remove 'green' and add 'red'
    header.classList.remove('green');
    header.classList.add('red');
  }
});