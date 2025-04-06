import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 
# Set Seaborn style
sns.set_theme(style="whitegrid")

# Simulation parameters
num_flights = 1000  # Total flights per day
seats_per_flight = 200  # Seats per flight
no_show_rate = 0.04  # No-show rate
num_simulations = 1000  # Number of Monte Carlo trials

compensation_per_passenger = 1020  # Compensation for bumped passengers


economy_price = 400
business_price = 4 * economy_price
first_price = 6 * economy_price

# Helper function to simulate revenue for either scenario
def run_simulation(booked_per_flight, seats, economy_tickets, business_tickets, first_tickets):
    net_revenues = []
    
    for _ in range(num_simulations):
        # Show-up count per flight
        show_up = np.random.binomial(booked_per_flight, 1 - no_show_rate, num_flights)
        
        # Number of passengers overbooked per flight
        overbooked = np.maximum(0, show_up - seats)
        
        # Daily total bookings and total number of overbooked passengers
        total_booked_passengers = num_flights * booked_per_flight
        total_overbooked_passengers = np.sum(overbooked)
        
        # Revenue per class
        economy_revenue = economy_tickets * economy_price * num_flights
        business_revenue = business_tickets * business_price * num_flights
        first_revenue = first_tickets * first_price * num_flights
        total_revenue = economy_revenue + business_revenue + first_revenue

        # Total revenue and compensation costs
        revenue = total_revenue
        compensation_cost = compensation_per_passenger * total_overbooked_passengers
        net_revenue = revenue - compensation_cost

        net_revenues.append(net_revenue)

    return np.mean(net_revenues), np.mean(overbooked)

# Simulation for domestic Flight Strategies
def simulate_domestic_flights(models):
    results = {}
    
    for strategy, params in models.items():
        seats = params["seats"]
        booked_per_flight = params["sold"]

        base_economy = int(0.85 * seats)
        base_business = int(0.1 * seats)
        base_first = int(0.05 * seats)
    
        # Extra overbooked seats allocation
        extra_seats = booked_per_flight - seats
        extra_economy = int(0.75 * extra_seats)
        extra_business = int(0.25 * extra_seats)
        extra_first = 0 
        
        economy_tickets = base_economy + extra_economy
        business_tickets = base_business + extra_business
        first_tickets = base_first + extra_first

        avg_net_revenue, _ = run_simulation(booked_per_flight, seats, economy_tickets, business_tickets, first_tickets)
        results[strategy] = avg_net_revenue

    # Plot Domestic Flight Results
    fig, ax = plt.subplots(figsize=(10, 7))
    strategies = list(results.keys())
    revenues = list(results.values())
    sns.barplot(x=strategies, y=revenues, palette='crest', hue=revenues, legend=False, ax=ax)
    
    for i, revenue in enumerate(revenues):
        ax.text(i, revenue + (0.02 * revenue), f"${revenue:,.0f}", ha='center', fontsize=10, fontweight='bold')

    ax.set_xlabel("Overbooking Strategy", fontsize=12)
    ax.set_ylabel("Average Net Revenue ($)", fontsize=12)
    ax.set_title(f"Domestic Flight: Overbooking Strategy Comparison", fontsize=14)
    plt.xticks(rotation=15)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Print Results
    print()
    for strategy, revenue in results.items():
        print(f"{strategy}: ${revenue:,.2f}")

    plt.show()

# Simulation for Booking Levels Optimization
def simulate_booking_levels(booking_levels):
    best_booking_level = None
    max_net_revenue = float('-inf')
    results = {}

    for booked_per_flight in booking_levels:
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
        
        avg_net_revenue, avg_overbooked_passengers = run_simulation(booked_per_flight, seats_per_flight, economy_tickets, business_tickets, first_tickets)
        results[booked_per_flight] = {
            "avg_overbooked_passengers": avg_overbooked_passengers,
            "avg_net_revenue": avg_net_revenue,
        }

        if avg_net_revenue > max_net_revenue:
            max_net_revenue = avg_net_revenue
            best_booking_level = booked_per_flight

    # Plot Booking Level Results
    fig, ax = plt.subplots(figsize=(10, 7))
    net_revenues = [results[b]["avg_net_revenue"] for b in booking_levels]
    ax.plot(booking_levels, net_revenues, color='b', marker='o', linestyle='-', label="Net Revenue")

    best_line = plt.axvline(best_booking_level, color='r', linestyle='--', label=f"Best: {best_booking_level} seats")

    best_booking_percentage = ((best_booking_level - seats_per_flight)/ seats_per_flight) * 100
    best_revenue = results[best_booking_level]["avg_net_revenue"]

    ax.annotate(f"${best_revenue:,.2f}",
                xy=(best_booking_level, best_revenue), color= 'red',
                xytext=(best_booking_level + 1, best_revenue + 1.02))

    # Highlight points from domestic_models
    strategy_points = {
        "Conservative(0%)": 200,
        "Moderate(3%)": 206,
        "Aggressive(5%)": 210,
        "Extra Aggressive(10%)": 220,
    }
    colors = ['orange', 'green', 'purple', 'black']
    
    for i, (label, x_val) in enumerate(strategy_points.items()):
        y_val = results[x_val]["avg_net_revenue"]
        ax.scatter(x_val, y_val, color=colors[i], s=85, label=label, zorder=5)


    ax.grid(True, which='both', axis='both', linestyle='--', alpha=0.7)

    ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
    ax.set_xlabel(f"Passengers per Flight out of 200 \n({best_booking_percentage}% Overbooked - ${compensation_per_passenger} Compensation Per Overbooked Passenger)")
    ax.set_ylabel("Average Net Revenue ($)")
    ax.set_title(f"Optimizing Overbooking for Maximum Revenue")
    plt.tight_layout()


    print(f"\nOptimal overbooking level: {best_booking_level} passengers per flight ({best_booking_percentage}% overbooked) with the revenue being ${best_revenue:,.2f}\n")
    plt.show()
# Define models and booking levels
domestic_models = {
    "Conservative(0%)": {"seats": 200, "sold": 200, "economy": 170, "business": 20, "first": 10},
    "Moderate(3%)": {"seats": 200, "sold": 206, "economy": 174, "business": 22, "first": 10},
    "Aggressive(5%)": {"seats": 200, "sold": 210, "economy": 178, "business": 22, "first": 10},
    "Extra Aggressive(10%)": {"seats": 200, "sold": 220, "economy": 185, "business": 25, "first": 10},
}

booking_levels = range(200, 230)

# Run both simulations
simulate_domestic_flights(domestic_models)  # Domestic overbooking strategy simulation
simulate_booking_levels(booking_levels)  # Booking level optimization simulation
