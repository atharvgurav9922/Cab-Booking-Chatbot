
import random

# Predefined cab rates
cab_rates = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

# Predefined routes
routes = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Swargate", "Kothrud", 8),
    3: ("Hinjawadi", "Wakad", 10)
}

# Main menu loop
while True:
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    # Exit option
    if choice == "2":
        print("Thank you for using Cab Booking Chatbot!")
        print("Goodbye!")
        break

    # Book ride option
    elif choice == "1":

        # Choose cab type
        print("\nSelect Cab Type:")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab_choice = input("Enter cab choice: ")

        if cab_choice not in ["1", "2", "3"]:
            print("Invalid cab choice. Please try again.")
            continue

        cab_type, rate = cab_rates[int(cab_choice)]

        # Choose route
        print("\nSelect Route:")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        route_choice = input("Enter route choice: ")

        if route_choice not in ["1", "2", "3"]:
            print("Invalid route choice. Please try again.")
            continue

        source, destination, distance = routes[int(route_choice)]

        # Calculate fare
        fare = rate * distance

        print("\n========== RIDE DETAILS ==========")
        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "/km")
        print("Total Fare: Rs.", fare)

        # Confirm or cancel before sharing OTP
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm_choice = input("Enter your choice: ")

        if confirm_choice == "2":
            print("Ride cancelled successfully.")
            print("No OTP has been shared.")
            continue

        elif confirm_choice == "1":
            # Generate a 4-digit OTP
            otp = random.randint(1000, 9999)

            print("\nYour booking OTP is:", otp)
            print("OTP has been shared with the user.")
            print("Cancellation is not allowed after OTP sharing.")
            print("Ride booking confirmed successfully!")

        else:
            print("Invalid confirmation choice.")
            print("Returning to the main menu.")

    else:
        print("Invalid menu choice. Please select 1 or 2.")
