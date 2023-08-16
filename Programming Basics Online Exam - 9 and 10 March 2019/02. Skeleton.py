target_time = int(input()) * 60 + int(input())
distance = float(input())
sec_per_100_m = int(input())

lowering_time = distance / 120 * 2.5
martins_time = distance / 100 * sec_per_100_m - lowering_time

if martins_time <= target_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {martins_time:.3f}.")
else:
    print(f"No, Marin failed! He was {martins_time - target_time:.3f} second slower.")



