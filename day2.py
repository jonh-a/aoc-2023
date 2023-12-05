def main():
    games = open("./inputs/day2.txt").read().split("\n")

    score = 0

    for id, game in enumerate(games):
        id = id + 1
        game = game.split(":")[1]
        iterations = game.split(";")
        good = True
        for iteration in iterations:
            rolls = iteration.split(",")
            for roll in rolls:
                roll = roll.strip()
                count, color = roll.split(" ")
                if (
                    ("red" in color and int(count.strip()) > 12)
                    or ("green" in color and int(count.strip()) > 13)
                    or ("blue" in color and int(count.strip()) > 14)
                ):
                    good = False
        
        if good is True:
            score += id 
            
    return score

print(main())