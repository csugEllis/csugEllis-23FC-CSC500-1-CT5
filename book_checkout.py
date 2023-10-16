# Get the number of books purchased
num_books = int(input("Enter the number of books purchased this month: "))

# Validate the input
if num_books < 0:
    print("Invalid number of books. Please enter a non-negative number.")
else:
    # Determine the number of points awarded
    if num_books >= 8:
        points = 60
    elif num_books >= 6:
        points = 30
    elif num_books >= 4:
        points = 15
    elif num_books >= 2:
        points = 5
    else:
        points = 0
    
    # Display the number of points awarded
    print(f"You have been awarded {points} points.")
