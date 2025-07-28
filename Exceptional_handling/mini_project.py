
# Content for Sample 1 of the project
purchase_content_1 = """Chocolate 50
Biscuit 35
Icecream 50

Discount 5
"""
with open('Purchase-1.txt', 'w') as f:
    f.write(purchase_content_1)

# Content for Sample 2 of the project
purchase_content_2 = """Chocolate 50
Biscuit 35
Icecream 50
Rice 100
Chicken 250

Perfume Free
Soup Free

Discount 80
"""

# Project 1: Supermarket Purchase Calculator
print("--- Project 1: Supermarket Purchase Calculator ---")
try:
    file_name = input("Enter the file name (e.g., Purchase-1.txt or Purchase-2.txt): ")
    
    with open(file_name, 'r') as f:
        lines = f.readlines()
        
        items_purchased = 0
        free_items = 0
        amount_to_pay = 0
        discount = 0
        
        for line in lines:
            parts = line.strip().split()
            if not parts: # Skip blank lines
                continue
            
            item_name = parts[0]
            
            if item_name.lower() == 'discount':
                discount = int(parts[1])
            else:
                price = parts[1]
                if price.lower() == 'free':
                    free_items += 1
                else:
                    items_purchased += 1
                    amount_to_pay += int(price)

        final_amount = amount_to_pay - discount
        
        print(f"No of items purchased: {items_purchased}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {amount_to_pay}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except (ValueError, IndexError):
    print("Error: The file is not formatted correctly. Please check the data.")
print("-" * 20, "\n")
