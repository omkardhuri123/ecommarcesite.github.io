// Main JavaScript file for Garden Bazaar

// Add to cart functionality
function addToCart(productId, quantity = 1) {
    // This would be implemented to interact with the backend
    console.log(`Added product ${productId} to cart with quantity ${quantity}`);
    
    // Show notification
    showNotification('Product added to cart successfully!');
}

// Notification system
function showNotification(message, type = 'success') {
    const notification = document.createElement('div');
    notification.className = `fixed bottom-4 right-4 p-4 rounded-md shadow-lg ${type === 'success' ? 'bg-green-500' : 'bg-red-500'} text-white max-w-xs z-50`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Remove notification after 3 seconds
    setTimeout(() => {
        notification.classList.add('opacity-0', 'transition-opacity', 'duration-300');
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// Initialize page-specific JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Product quantity controls
    const quantityInputs = document.querySelectorAll('input[type="number"]');
    quantityInputs.forEach(input => {
        const minusBtn = input.previousElementSibling;
        const plusBtn = input.nextElementSibling;
        
        if (minusBtn && plusBtn) {
            minusBtn.addEventListener('click', () => {
                if (input.value > parseInt(input.min || 1)) {
                    input.value = parseInt(input.value) - 1;
                }
            });
            
            plusBtn.addEventListener('click', () => {
                if (input.value < parseInt(input.max || 99)) {
                    input.value = parseInt(input.value) + 1;
                }
            });
        }
    });
    
    // Add to cart buttons
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            
            const productId = button.getAttribute('data-product-id');
            let quantity = 1;
            
            const quantityInput = button.closest('form') ? button.closest('form').querySelector('input[type="number"]') : null;
            if (quantityInput) {
                quantity = parseInt(quantityInput.value);
            }
            
            addToCart(productId, quantity);
        });
    });
});