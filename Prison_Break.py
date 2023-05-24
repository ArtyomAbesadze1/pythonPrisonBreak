import random

print("Prison Break! ")
print(""" You have just escaped prison and the cops are chasing you! 

The cops are right behind you, but not all hope is lost, you have some water and friends along the way. But be careful, there might be roadblocks ahead! """)

# variables
distanceCovered = 0
hydration = 0
fatigue = 0
copsDistance = -20
waterBottles = 3
end = False
hideout = False
roadblock = False

# start main loop
while not end:
    # Random events
    if random.random() < 0.10:  # 10% chance for hideout
        hideout = True
        print("\nYou've found a hideout! You can rest and replenish your water supply.")
        waterBottles = 3
        hydration = 0
        fatigue = 0
    if random.random() < 0.10:  # 10% chance for roadblock
        roadblock = True
        print("\nA roadblock! Your movement speed is reduced.")

    copsBehind = distanceCovered - copsDistance
    sprintSpeed = random.randrange(10, 21)
    steadySpeed = random.randrange(5, 13)
    print("""
    A. Drink from your water bottle.
    B. Continue at steady speed.
    C. Run at full speed.
    D. Stop to rest.
    E. Status check.
    Q. Give up.""")
    print()
    userInput = input("Your choice? ")
    if userInput.lower() == "q":
        end = True
        print("You gave up, thanks for playing!")
    # check status
    elif userInput.lower() == "e":
        print("Distance covered: ", distanceCovered)
        print("Water bottles left: ", waterBottles)
        print("Your fatigue level is ", fatigue)
        print("The cops are ", copsBehind, "meters behind you.")
    # Stop to rest
    elif userInput.lower() == "d":
        fatigue = 0
        print("You feel refreshed and ready to move. Your fatigue is now ", fatigue)
        copsDistance += random.randrange(7, 15)
    # move at sprint speed
    elif userInput.lower() == "c":
        print("You decided to sprint.")
        if roadblock:
            print("However, a roadblock slowed you down.")
            distanceCovered += max(0, sprintSpeed - 3)  # Ensure that the speed doesn't go below 0
            roadblock = False
        else:
            distanceCovered += sprintSpeed
        hydration += 1
        fatigue += random.randrange(1, 4)
        copsDistance += random.randrange(7, 15)
    # move at steady speed
    elif userInput.lower() == "b":
        print("You decided to move at a steady speed.")
        if roadblock:
            print("However, a roadblock slowed you down.")
            distanceCovered += max(0, steadySpeed - 3)  # Ensure that the speed doesn't go below 0
            roadblock = False
        else:
            distanceCovered += steadySpeed
        hydration += 1
        fatigue += 1
        copsDistance += random.randrange(7, 15)
    # drink water
    elif userInput.lower() == "a":
        if waterBottles == 0:
            print("You're out of water.")
        else:
            waterBottles -= 1
            hydration = 0
            print("You have ", waterBottles, "water bottles left and you are no longer dehydrated.")

    # not done check
    if copsBehind <= 15:
        print("The cops are drawing near!")
    if distanceCovered >= 200 and not end:
        print("You have successfully escaped, you win!")
        end = True
    if copsDistance >= distanceCovered:
        print("The cops have caught and arrested you.")
        print("You're back in jail!")
        end = True
    if hydration > 4 and hydration <= 6 and not end:
        print("You are dehydrated")
    if hydration > 6:
        print("You passed out from dehydration!")
        end = True
    if fatigue > 5 and fatigue <= 8 and not end:
        print("You are getting tired.")
    if fatigue > 8:
        print("You passed out from exhaustion.")
        end = True
