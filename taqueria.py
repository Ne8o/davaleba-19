
#list
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
} 

total = 0
while True:
    try:
        write_key = input("Item: ").title()
        total_p = menu[write_key]
        if  write_key in menu :
            total = int(total) + int(menu[write_key])
            print(f"Total: {total:.2f} $")
            continue
        if write_key not in menu :
            continue
    except(KeyError, KeyError) :
        break
