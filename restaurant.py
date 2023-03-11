import random

text_dishes = input("--Кафе 'У Монті'--\nЗамовляйте страви\n") 
dishes = text_dishes.split(",") 
total_sum = 0 
for dish in dishes:
    dish_price = round(random.random() * 100, 2)
    total_sum += dish_price
    print(dish.strip() + "......." + str(dish_price) + " грн")
print(".................")
print("Всього........" + str(round(total_sum, 2)) + " грн") 
