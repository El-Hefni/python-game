import random
coins = random.random(4, 400)

while coins:
    print("Coins left:",  coins)
    coins_range = int(((coins)**0.5) // 1)
    p1 = int(input(f"Player 1 choose a number {[i**2 for i in range(1, coins_range + 1)]} : "))
    if p1 not in [i**2 for i in range(1, coins_range + 1)]:
        print("please next time enter squared number!")
    else:
        coins -= p1
    if not coins:
        print("Player 1 won")
        break
    coins_range = int(((coins)**0.5) // 1)
    print("Coins left:",  coins)
    p2 = int(input(f"Player 2 choose a number {[i**2 for i in range(1, coins_range + 1)]} : "))
    if p2 not in [i**2 for i in range(1, coins_range + 1)]:
        print("please next time enter squared number!")
    else:
        coins -= p2
    if not coins:
        print("Player 2 won")
        break
