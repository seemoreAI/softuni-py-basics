wish_height = int(input())
plank_height = wish_height - 30
done = False
jumps = 0
while True:
    if done:
        print(f"Tihomir succeeded, he jumped over {plank_height}cm after {jumps} jumps.")
        break
    for _ in range(3):
        jumper_height = int(input())
        jumps += 1
        if jumper_height > plank_height:
            if plank_height >= wish_height:
                done = True
                break
            plank_height += 5
            break
    else:
        print(f"Tihomir failed at {plank_height}cm after {jumps} jumps.")
        break



