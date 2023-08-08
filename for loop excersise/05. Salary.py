# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.

tabs = int(input())
salary = int(input())

for i in range(tabs):
    social_media = input()
    if social_media == "Facebook":
        salary -= 150
    elif social_media == "Instagram":
        salary -= 100
    elif social_media == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary." )
        break
else:
    print(int(salary))
