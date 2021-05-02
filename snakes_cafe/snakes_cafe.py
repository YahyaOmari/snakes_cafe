# Head of the menu
print("*"*38)
print ("**    Welcome to the Snakes Cafe!   **")
print ("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type ""quit"" **")
print("*"*38)

# Appetizers -------------------
print("Appetizers")
print("----------")
wings = 'Wings'
counter_wings = 0
print("Wings")

cookies = 'Cookies'
counter_cookies = 0
print("Cookies")

spring_rolls = 'Spring Rolls' 
counter_spring_rolls = 0
print("Spring Rolls \n")

# Entrees -------------------
print("Entrees")
print("-------")
salmon = 'Salmon'
counter_salmon = 0
print("Salmon")

steak = 'Steak'
counter_steak = 0
print("Steak")

meat_tornado = 'Meat Tornado'
print("Meat Tornado")
counter_meat_tornado = 0

a_literal_garden = 'A Literal Garden'
counter_a_literal_garden = 0
print("A Literal Garden\n")

# Desserts -------------------
print("Desserts")
print("--------")
ice_cream = 'Ice Cream'
counter_ice_cream = 0
print("Ice Cream")

cake = 'Cake'
counter_cake = 0
print("Cake")

pie = 'Pie'
counter_pie = 0
print("Pie\n")

# Drinks -------------------
print("Drinks")
print("------")
coffee = 'Coffee'
counter_coffee = 0
print("Coffee")

tea = 'Tea'
counter_tea = 0
print("Tea")

unicorn_tears = 'Unicorn Tears'
counter_unicorn_tears = 0
print("Unicorn Tears\n")

# Bottom of the menu
print("*"*35)
print("** What would you like to order? **")
print("*"*35)
print("\n")


n = 10

while n > 0:
    costumer_input = input('> ')
    if costumer_input == 'quit':
        quit()
    elif costumer_input == wings:
        counter_wings +=1
        print(f'** {counter_wings} order of {costumer_input} have been added to your meal **')
    elif costumer_input == cookies:
        counter_cookies += 1
        print(f'** {counter_cookies} order of {costumer_input} have been added to your meal **')
    elif costumer_input == spring_rolls:
        counter_spring_rolls += 1
        print(f'** {counter_spring_rolls} order of {costumer_input} have been added to your meal **')
    elif costumer_input == salmon:
        counter_salmon += 1
        print(f'** {counter_salmon} order of {costumer_input} have been added to your meal **')
    elif costumer_input == steak:
        counter_steak += 1
        print(f'** {counter_steak} order of {costumer_input} have been added to your meal **')
    elif costumer_input == meat_tornado:
        counter_meat_tornado += 1
        print(f'** {counter_meat_tornado} order of {costumer_input} have been added to your meal **')
    elif costumer_input == a_literal_garden:
        counter_a_literal_garden += 1
        print(f'** {counter_a_literal_garden} order of {costumer_input} have been added to your meal **')
    elif costumer_input == ice_cream:
        counter_ice_cream += 1
        print(f'** {counter_ice_cream} order of {costumer_input} have been added to your meal **')
    elif costumer_input == cake:
        counter_cake += 1
        print(f'** {counter_cake} order of {costumer_input} have been added to your meal **')
    elif costumer_input == pie:
        counter_pie += 1
        print(f'** {counter_pie} order of {costumer_input} have been added to your meal **')
    elif costumer_input == coffee:
        counter_coffee += 1
        print(f'** {counter_coffee} order of {costumer_input} have been added to your meal **')
    elif costumer_input == tea:
        counter_tea += 1
        print(f'** {counter_tea} order of {costumer_input} have been added to your meal **')
    elif costumer_input == unicorn_tears:
        counter_unicorn_tears += 1
        print(f'** {counter_unicorn_tears} order of {costumer_input} have been added to your meal **')
    else:
        print("Choose one of the items from the menu")