import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_flights = 1000  # Total flights per day
seats_per_flight = 200  # Seats per flight
no_show_rate = 0.04  # no-show rate
num_simulations = 100  # Number of Monte Carlo trials

# Range of overbooked seats to test
booking_levels = range(200, 250)


compensation_per_passenger = 800  # Compensation for bumped passengers

#Ticket Prices
economy_price = 400 
business_price = 4 * economy_price  
first_price = 6 * economy_price  



best_booking_level = None
max_net_revenue = float('-inf')


results = {}

# Iterate over different booking levels
for booked_per_flight in booking_levels:
    overbooked_passengers_per_day = []
    net_revenues = []

    # Base seat allocation before overbooking
    base_economy = int(0.85 * seats_per_flight)
    base_business = int(0.1 * seats_per_flight)
    base_first = int(0.05 * seats_per_flight)
    
    # Extra overbooked seats allocation
    extra_seats = booked_per_flight - seats_per_flight
    extra_economy = int(0.75 * extra_seats)
    extra_business = int(0.25 * extra_seats)
    extra_first = 0  
    
    
    economy_tickets = base_economy + extra_economy
    business_tickets = base_business + extra_business
    first_tickets = base_first + extra_first

    # Monte Carlo simulations
    for _ in range(num_simulations):
        # show-up count per flight
        show_up = np.random.binomial(booked_per_flight, 1 - no_show_rate, num_flights)

        # number of passengers overbooked per flight 
        overbooked = np.maximum(0, show_up - seats_per_flight)

        #daily total bookings and total number of overbooked passengers
        total_booked_passengers = num_flights * booked_per_flight
        total_overbooked_passengers = np.sum(overbooked)

        #revenue per class
        economy_revenue = economy_tickets * economy_price * num_flights
        business_revenue = business_tickets * business_price * num_flights
        first_revenue = first_tickets * first_price * num_flights
        total_revenue = economy_revenue + business_revenue + first_revenue

        #total revenue and compensation costs
        revenue = total_revenue
        compensation_cost = compensation_per_passenger * total_overbooked_passengers
        net_revenue = revenue - compensation_cost

        
        overbooked_passengers_per_day.append(total_overbooked_passengers)
        net_revenues.append(net_revenue)

    #  average net revenue for this booking level
    avg_net_revenue = np.mean(net_revenues)

    
    results[booked_per_flight] = {
        "avg_overbooked_passengers": np.mean(overbooked_passengers_per_day),
        "avg_net_revenue": avg_net_revenue,
    }

    # Update best booking level if a higher net revenue is found
    if avg_net_revenue > max_net_revenue:
        max_net_revenue = avg_net_revenue
        best_booking_level = booked_per_flight



fig, ax = plt.subplots(figsize=(10, 5))
net_revenues = [results[b]["avg_net_revenue"] for b in booking_levels]

#net revenue curve
net_revenue_plot, = ax.plot(booking_levels, net_revenues, color='b', marker='o', linestyle='-', label="Net Revenue")

# Optimal booking level on the plot
best_line = plt.axvline(best_booking_level, color='r', linestyle='--', label=f"Best: {best_booking_level} seats")

#best booking percent     
best_booking_percentage = ((best_booking_level - seats_per_flight)/ seats_per_flight) * 100

#annotation at the best booking level
best_revenue = results[best_booking_level]["avg_net_revenue"]
ax.annotate(f"${best_revenue:,.2f}",
            xy=(best_booking_level, best_revenue), color= 'red',
            xytext=(best_booking_level + 1, best_revenue + 1.02))  


ax.legend(loc='upper left', bbox_to_anchor=(1, 1))


ax.set_xlabel(f"Passengers per Flight out of 200 \n({best_booking_percentage}% Overbooked - ${compensation_per_passenger} Compensation Per Overbooked Passenger)")
ax.set_ylabel("Average Net Revenue ($)")
ax.set_title(f"Optimizing Overbooking for Maximum Revenue")

plt.tight_layout()
plt.grid()



print(f"Optimal overbooking level: {best_booking_level} passengers per flight ({best_booking_percentage} % overbooked) with the revenue being ${best_revenue:,.2f}")

plt.show()