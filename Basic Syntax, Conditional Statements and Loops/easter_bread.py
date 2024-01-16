budget = float (input())
price_per_kilo_flour = float (input())
price_per_pack_of_eggs = 0.75 * price_per_kilo_flour
price_per_liter_milk = 1.25 * price_per_kilo_flour
total_price_per_bread = price_per_kilo_flour + price_per_pack_of_eggs + 0.25 * price_per_liter_milk
colored_eggs = 0
number_of_loaves = 0


while budget >= 0 :
    if total_price_per_bread > budget:
        break
    budget -= total_price_per_bread
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3== 0:
        colored_eggs -= (number_of_loaves) - 2
        if colored_eggs < 0:
            break
    budget
print (f" You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


