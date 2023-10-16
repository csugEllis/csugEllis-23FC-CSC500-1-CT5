# Initialize variables
total_months = 0
total_rainfall = 0.0

# Get the number of years
num_years = int(input("Enter the number of years: "))

# Validate the input
if num_years <= 0:
    print("Invalid number of years. Please enter a positive number.")
else:
    # Loop for each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}")
        # Loop for each month
        for month in range(1, 13):
            # Get monthly rainfall
            monthly_rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            # Validate the input
            if monthly_rainfall < 0:
                print("Invalid rainfall. Please enter a non-negative number.")
                break
            # Update total rainfall and total months
            total_rainfall += monthly_rainfall
            total_months += 1
    
    # Calculate the average rainfall per month
    average_rainfall = total_rainfall / total_months if total_months != 0 else 0
    
    # Display results
    print(f"\nTotal number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")
