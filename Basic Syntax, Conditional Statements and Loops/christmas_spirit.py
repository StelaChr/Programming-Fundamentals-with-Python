qty_of_decorations = int(input())
days_until_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
total_cost = 0
gained_spirit = 0

for current_day in range (1, days_until_christmas + 1):
    if current_day % 11==0:
        qty_of_decorations += 2
    if current_day %2 == 0:
        total_cost += qty_of_decorations * ornament_set_price
        gained_spirit += 5
    if current_day %3 ==0:
        total_cost += qty_of_decorations * tree_skirt_price + qty_of_decorations * tree_garland_price
        gained_spirit+= 3+ 10
    if current_day %5 == 0:
        total_cost += qty_of_decorations * tree_lights_price
        gained_spirit += 17
        if current_day % 3 == 0:
            gained_spirit += 30
    if current_day % 10 == 0:
        gained_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price
if days_until_christmas %10 == 0:
    gained_spirit -= 30
print (f'Total cost: {total_cost}')
print (f"Total spirit: {gained_spirit}")
