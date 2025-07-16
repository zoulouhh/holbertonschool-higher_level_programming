// Select the element with id "add_item" and the ul element with class "my_list"
const addItemButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');

// Add a click event listener to the add_item element
addItemButton.addEventListener('click', function() {
  // Create a new li element
  const newItem = document.createElement('li');
  
  // Set the text content of the new li element
  newItem.textContent = 'Item';
  
  // Append the new li element to the ul with class "my_list"
  myList.appendChild(newItem);
});