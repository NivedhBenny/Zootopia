// Get the necessary elements
const decreaseButton = document.getElementById('decreaseButton');
const increaseButton = document.getElementById('increaseButton');
const quantityElement = document.getElementById('quantity');

// Set initial quantity
let quantity = 1;
quantityElement.textContent = quantity;

// Add event listeners to the buttons
decreaseButton.addEventListener('click', decreaseQuantity);
increaseButton.addEventListener('click', increaseQuantity);

// Function to decrease the quantity
function decreaseQuantity() {
  if (quantity > 0) {
    quantity--;
    quantityElement.textContent = quantity;
  }
}

// Function to increase the quantity
function increaseQuantity() {
  quantity++;
  quantityElement.textContent = quantity;
}
