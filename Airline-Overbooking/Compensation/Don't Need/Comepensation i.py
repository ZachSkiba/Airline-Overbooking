import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

# Set Seaborn style
sns.set_theme(style="whitegrid")

# Simulation parameters
num_flights = 100  # Total flights per day
no_show_rate = 0.075  # No-show rate
num_simulations = 1000  # Number of Monte Carlo simulation trials


compensation_per_passenger = 4000  # Compensation for bumped passenger

# Define models for International flights
international_models = {
    "Conservative(0%)": {"seats": 400, "sold": 400, "economy": 360, "business": 30, "first": 10,},
    "Moderate(5%)": {"seats": 400, "sold": 420, "economy": 375, "business": 35, "first": 10},
    "Aggressive(10%)": {"seats": 400, "sold": 440, "economy": 390, "business": 40, "first": 10},
    "Extra Aggressive(15%)": {"seats": 400, "sold": 460, "economy": 405, "business": 45, "first": 10},
}

# Function to simulate revenue
def simulate_revenue(models):
    results = {}
    for strategy, params in models.items():
        seats = params["seats"]
        booked_per_flight = params["sold"]
        
        economy_tickets = params["economy"]
        business_tickets = params["business"]
        first_tickets = params["first"]

        # Ticket prices
        economy_price = 1200
        business_price = 4 * economy_price  
        first_price = 6 * economy_price 
        
        net_revenues = []
        
        for _ in range(num_simulations):
            #show-up rate per flight
            show_up = np.random.binomial(booked_per_flight, 1 - no_show_rate, num_flights)
            overbooked = np.maximum(0, show_up - seats)
            
            total_booked_passengers = num_flights * booked_per_flight
            total_overbooked_passengers = np.sum(overbooked)
            
            #revenue per class
            economy_revenue = economy_tickets * economy_price * num_flights
            business_revenue = business_tickets * business_price * num_flights
            first_revenue = first_tickets * first_price * num_flights
            total_revenue = economy_revenue + business_revenue + first_revenue

            revenue = total_revenue
            compensation_cost = compensation_per_passenger * total_overbooked_passengers
            net_revenue = revenue - compensation_cost
            
            net_revenues.append(net_revenue)
        
        # Store results
        avg_net_revenue = np.mean(net_revenues)
        results[strategy] = avg_net_revenue
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 7))
    strategies = list(results.keys())
    revenues = list(results.values())

    sns.barplot(x=strategies, y=revenues, palette='crest', hue= revenues,legend=False, ax=ax)
    
    # Add labels on top of bars
    for i, revenue in enumerate(revenues):
        ax.text(i, revenue + (0.02 * revenue), f"${revenue:,.0f}", ha='center', fontsize=10, fontweight='bold')


    ax.set_xlabel("Overbooking Strategy", fontsize=12)
    ax.set_ylabel("Average Net Revenue ($)", fontsize=12)
    ax.set_title(f"International Flight: Overbooking Strategy Comparison", fontsize=14)
    
    plt.xticks(rotation=15)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    
    
    # Print results
    print(f"International Flight Results:\n")
    for strategy, revenue in results.items():
        print(f"  {strategy}: ${revenue:,.2f}")
    print()

    plt.show()

# Run simulation for International flights
simulate_revenue(international_models)
