gigi_store = [
    {
        'id': 1,
        'item_name': 'forceps',
        'unit_price': 10,
        'quantity': 5
    },
    {
        'id': 2,
        'item_name': 'suture',
        'unit_price': 10,
        'quantity': 5
    },
    { 
        'id': 3,
        'item_name': 'gloves',
        'unit_price': 10,
        'quantity': 5
    },
    {
        'id': 4,
        'item_name': 'scalpel',
        'unit_price': 10,
        'quantity': 5
    },
    {
        'id': 5,
        'item_name': 'saline',
        'unit_price': 10,
        'quantity': 5
    }
]

 
print(f'Welcome to the store.\nHere are the goods in stock:\n{gigi_store}', end=" ")
print()
print('''----------------------------''')
print('''íd | item_name |unit_price |''')
print('''----------------------------''')
print('''1  | forceps   | 10        |''')
print('''2  | suture    | 10        |''')
print('''3  | gloves    | 10        |''')
print('''4  | scalpel   | 10        |''')
print('''5  | saline    | 10        |''')
print('''----------------------------''')
print()


# Initialize an empty cart
cart = []

while True:
    try:
        cart_item = int(input("Select item with it's id (or 0 to checkout): "))
        if cart_item == 0:
            break  # Exit the loop if the user enters 0 to stop adding items
        quantity = int(input('Enter the quantity of items: '))

        checkItem = False  

        for items in gigi_store:
            if cart_item == items['id']:
                if quantity > items['quantity']:
                    print(f"Item unavailable. Only {items['quantity']} {items['item_name']} left in stock. Kindly contact support")
                else:
                    price = items['unit_price']
                    total_cost = price * quantity
                    cart.append({
                        'id': items['id'],
                        'item_name': items['item_name'],
                        'quantity': quantity,
                        'unit_price': price,
                        'total_cost': total_cost
                    })
                    items['quantity'] -= quantity
                    checkItem = True
                break

        if not checkItem:
            print('Item not found in stock.')
        else:
            print(f'Added {quantity} {items["item_name"]} to the cart.')
    except ValueError:
        print('Error: Invalid input. Please enter a valid number.')

# # Display the cart contents
# print('\nItems in your cart:')
total = 0

for item in cart:
    # print(f"Item: {item['item_name']}\tQuantity: {item['quantity']}\tUnit Price: {item['unit_price']}\tTotal Cost: {item['total_cost']}")
    print(f"Id: {item['id']}\tItem: {item['item_name']}\tUnit Price: {item['unit_price']}\t Subtotal Cost: {item['total_cost']}")
    total+=item['total_cost']    

print("Sum total of goods purchased is",total)