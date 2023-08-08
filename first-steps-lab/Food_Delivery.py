chicken_menu = 10.35
fish_menu = 12.4
vegan_menu = 8.15
delivery = 2.5

chicken_menu_count=int(input())
fish_menu_count=int(input())
vegan_menu_count=int(input())

chicken_menu_sum=chicken_menu_count*chicken_menu
fish_menu_sum=fish_menu_count*fish_menu
vegan_menu_sum=vegan_menu*vegan_menu_count
food_sum = vegan_menu_sum+fish_menu_sum+chicken_menu_sum
desert=food_sum * 0.2
total_sum=food_sum+desert+delivery

print(total_sum)