customers = int(input())
Back = 0
Chest = 0
Legs = 0
Abs = 0
Protein_shake = 0
Protein_bar = 0

for _ in range(customers):
    act = input()
    if act == "Back":
        Back += 1
    elif act == "Chest":
        Chest += 1
    elif act == "Legs":
        Legs += 1
    elif act == "Abs":
        Abs += 1
    elif act == "Protein shake":
        Protein_shake += 1
    elif act == "Protein bar":
        Protein_bar += 1

print(f"{Back} - back")
print(f"{Chest} - chest")
print(f"{Legs} - legs")
print(f"{Abs} - abs")
print(f"{Protein_shake} - protein shake")
print(f"{Protein_bar} - protein bar")
print(f"{(Back+Chest+Legs+Abs)/customers*100:.2f}% - work out")
print(f"{(Protein_bar+Protein_shake)/customers*100:.2f}% - protein")
