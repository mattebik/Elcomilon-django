let cart = [];
let total = 0;

function addToCart(product, price, image) {
    cart.push({ product, price, image });
    total += price;
    updateCart();
}

function updateCart() {
    const cartItems = document.getElementById('cart-items');
    const totalPrice = document.getElementById('total-price');
    
    cartItems.innerHTML = '';
    cart.forEach((item, index) => {
        const li = document.createElement('li');
        
        const img = document.createElement('img');
        img.src = item.image;
        img.alt = item.product;
        
        const text = document.createTextNode(`${item.product} - $${item.price}`);
        
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Eliminar';
        removeButton.onclick = () => removeFromCart(index);
        
        li.appendChild(img);
        li.appendChild(text);
        li.appendChild(removeButton);
        
        cartItems.appendChild(li);
    });
    
    totalPrice.textContent = total.toFixed(2);
}

function removeFromCart(index) {
    total -= cart[index].price;
    cart.splice(index, 1);
    updateCart();
}

function checkout() {
    if (cart.length === 0) {
        alert('El carrito está vacío');
        return;
    }
    alert(`Has pagado $${total.toFixed(2)}. Gracias por tu compra!`);
    cart = [];
    total = 0;
    updateCart();
}
