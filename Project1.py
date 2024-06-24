print("Welcome to the Garden Planning tool!")

length = float(input("Please enter the length of your garden area (in feet): "))
width = float(input("Please enter the width of your garden area (in feet): "))

totalGardenAmount = length * width
gardenArea = 0.0
totalGarden = 0.0

while True:
    print("\nLet's choose some plants for your garden: \n\n"
        "1. Roses - $2.50 per square foot \n" +
        "2. Tulips - $1.75 per square foot \n" +
        "3. Daisies - $1.00 per square foot \n\n")

    plantWanted = int(input("Enter the number corresponding to the plant you'd want, or 0 to finish : "))

    if plantWanted == 1:
        plantName = "Roses"
        plantPrice = 2.50
    elif plantWanted == 2:
        plantName = "Tulips"
        plantPrice = 1.75
    elif plantWanted == 3:
        plantName = "Daisies"
        plantPrice = 1.00
    elif plantWanted == 0:
        break
    else:
        print("Incorrect value entered. Program will end.")
        exit()


    plantAmount = float(input(f"How many square feet of {plantName} would you like to plant? "))

    if gardenArea + plantAmount > totalGardenAmount:
        print("Sorry, you do not have enough space for that many plants.")
        print(f"You have {totalGardenAmount - gardenArea:.2f} square feet of garden remaining.")
        continue

    gardenArea += plantAmount
    totalCost = plantAmount * plantPrice
    totalGarden += totalCost

    print(f"\nThe total cost of {plantAmount} square feet of {plantName} is ${totalCost:.2f}.")
    print(f"\nYou have {totalGardenAmount - gardenArea:.2f} square feet of garden space remaining.")


print(f"Summary:\n\nTotal garden area used: {gardenArea:.2f} square feet out of {totalGardenAmount:.2f} square feet\nTotal cost for the entire garden: ${totalGarden:.2f}")