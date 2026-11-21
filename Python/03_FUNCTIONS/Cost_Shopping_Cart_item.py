def calculate_cost(cart):
    total_cost = 0
    
    for item in cart:
        total_cost += item['price'] * item['quantity']
        
    return total_cost

cart = [
    {'item' : 'fruits', 'price' : 50, 'quantity' : 5 },
    {'item' : 'Chair', 'price' : 250, 'quantity': 4}
]    
print(calculate_cost(cart))