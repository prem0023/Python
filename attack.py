import random

playerhp = 360
enemyatkl = 20
enemyatkh = 50

while playerhp > 10:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg



    print("Enemy strikes for ", dmg, "points of damage. Current HP is ", playerhp)

    if playerhp <= 10:
        if playerhp<= 0:
            print("You are dead")
            break
        else:
            print("You have low health. Apply some first aid")
            break
