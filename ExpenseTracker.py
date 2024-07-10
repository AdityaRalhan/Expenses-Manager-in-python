import json

# expenses_list is a list and it has multiple dictionaries with each dictionary about a specific purchase
budget = 10000

def load_data():
    try:
        with open('Expenses.txt', 'r') as file:
            f = json.load(file)
            # print(test)
            return f # it will go in file, load wtv data is there and also convert it from string into json. THIS IS NOT A LIST
    
    except FileNotFoundError:
        return [] # agar file he nahi mili then return empty list


# helper method to save data
def save_data(expense_list):
    with open('Expenses.txt','w') as file:
        json.dump(expense_list, file)

def add_expense(expense_list):
    type_of_item = input ("Enter type : \n Outside Food(f), \n Groceries(g), \n House items(h), \n shopping(s) \n - ")
    item = input("Item : ")
    quantity = input("quantity : ")
    cost = int(input("cost (₹): "))    

    expense_list.append({'item' : item, 'quantity' : 'x'+quantity, 'cost' : cost, 'section' : type_of_item })
    # print(expense_list)
    save_data(expense_list)

def delete_expense(expense_list):
    view_list(expense_list)
    index = int(input("Enter the number you wish to delete : "))

    if 1<= index <= len(expense_list):
        del expense_list[index - 1]
        save_data(expense_list)

    else :
        print("Video index does not exist")

def edit_expense(expense_list):
    view_list(expense_list)
    index = int(input("Enter the number you wish to edit : "))

    if 1<= index <= len(expense_list):
        type_of_item = input ("Enter new type : \n Food(f), \n Groceries(g), \n House items(h), \n shopping(s) \n - ")
        item = input("new item : ")
        quantity = input("it's quantity : ")
        cost = int(input("it's cost (₹) : "))

        expense_list[index - 1] = {'item' : item, 'quantity' : quantity, 'cost' : cost, 'section' : type_of_item }

        save_data(expense_list)

    else:
        print("Invalid index")



def total_spent(expense_list):
    total_spent = 0
    print()
    for expense in expense_list:
        print(f"{expense['item']} - {expense['cost']}")
        int_cost = int(expense['cost'])
        int_qty = int(expense['quantity'])
        print(int_qty)
        total_cost = int_cost * int_qty
        total_spent += total_cost


    print(f"total spent is : ₹{total_spent}")
    budget_left = budget - total_spent
    print(f"\nbudget left is : {budget_left}")



def view_list(expense_list):
    print("\n")
    print("*" * 70)
    print("\n")

    for index, expense in enumerate(expense_list, start = 1):
        print(f"{index}. {expense['section']} - {expense['item']}, {expense['quantity']}, for ₹{expense['cost']}")

    print("\n")
    print("*" * 70)


def category_wise_spent(expense_list):
    food_cost = 0
    groceries_cost = 0
    house_items_cost = 0
    shopping_cost = 0
    for expense in expense_list:
        for key,value in expense.items():
            if value == "f":
                food_cost += (expense['cost'] * int(expense['quantity']))
            
            elif value == "g" :
                groceries_cost += (expense['cost'] * int(expense['quantity']))

            elif value == "h" :
                house_items_cost += (expense['cost'] * int(expense['quantity']))
            
            elif value == "s" :
                shopping_cost += (expense['cost'] * int(expense['quantity']))
    
    print(f"cost for outside food is {food_cost}")
    print(f"cost for groceries is {groceries_cost}")
    print(f"cost for house_items is {house_items_cost}")
    print(f"cost for shopping is {shopping_cost}")



def main():
    print("\n Seems like u have made some purchases")
    expense_list = load_data()

    while True:
        print('\n Expense Tracker | choose an option')
        print('\n 1. add something')
        print('\n 2. delete an existing expense')
        print('\n 3. edit an existing expense')
        print('\n 4. total spent and remaining budget')
        print('\n 5. see existing list')
        print('\n 6. category wise expense')
        print('\n 7. exit')


        choice = input("\n Enter choice - ")


        match choice:

            case '1': 
                add_expense(expense_list)

            case '2':
                delete_expense(expense_list)

            case '3':
                edit_expense(expense_list)

            case '4':
                total_spent(expense_list)

            case '5':
                view_list(expense_list)

            case '6':
                category_wise_spent(expense_list)

            case '7':
                break

            case _:
                print("enter from 1 to 5")

if __name__ == "__main__":
    main()



