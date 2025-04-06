import numpy as np

# Simulation parameters
num_flights = 100  # Total flights per day
seats_per_flight = 400  # Seats available per flight
no_show_rate = 0.075  # No-show rate
num_simulations = 1000  # Number of Monte Carlo trials

# Different overbooking strategies
booking_levels = {
    "Conservative": 400,  # 0% overbooking
    "Moderate": 420,      # 5% overbooking
    "Aggressive": 440,    # 10% overbooking
    "Extra Aggressive": 460  # 15% overbooking
}


lower_bound, upper_bound = .05, .15


# Store results for each strategy
results = {}

for strategy, booked_per_flight in booking_levels.items():
    overbooked_passengers_per_day = []
    
    # Monte Carlo simulation
    for _ in range(num_simulations):
        total_overbooked = 0
        
        for _ in range(num_flights):
            show_up = np.random.binomial(booked_per_flight, 1 - no_show_rate)  # Passengers who show up
            overbooked = max(0, show_up - seats_per_flight)  # Count of overbooked passengers
            total_overbooked += overbooked
        
        overbooked_passengers_per_day.append(total_overbooked)
    
    # Convert list to NumPy array
    overbooked_passengers_per_day = np.array(overbooked_passengers_per_day)
    
    # Total passengers per day
    total_passengers_per_day = num_flights * booked_per_flight
    
    # Overbooking rate per passenger
    overbooking_rate_per_passenger = overbooked_passengers_per_day / total_passengers_per_day * 100
    
    # Calculate probabilities
    prob_within_range = np.mean((overbooking_rate_per_passenger >= lower_bound) & (overbooking_rate_per_passenger <= upper_bound))
    prob_above_range = np.mean(overbooking_rate_per_passenger > upper_bound)
    prob_below_range = np.mean(overbooking_rate_per_passenger < lower_bound)
    
    # Convert to percentages
    prob_within_range_pct = prob_within_range * 100
    prob_above_range_pct = prob_above_range * 100
    prob_below_range_pct = prob_below_range * 100
    
    avg_overbooking_rate = np.mean(overbooking_rate_per_passenger)
    
    if avg_overbooking_rate > 0:
        one_in_x_passengers = round(1 / (avg_overbooking_rate / 100))
        
    else:
        one_in_x_passengers = None
        
    lower_bound_people = round(.0005* num_flights * seats_per_flight)
    upper_bound_people = round(.0015* num_flights * seats_per_flight) 

    # Store results
    results[strategy] = {
    f"P of overbooking between {lower_bound_people} - {upper_bound_people} passengers": f"\t\t{prob_within_range_pct:.2f}%",
    f"P of overbooking > {upper_bound_people} passengers": f"\t\t\t{prob_above_range_pct:.2f}%",
    f"P of overbooking < {lower_bound_people} passengers": f"\t\t\t{prob_below_range_pct:.2f}%",
    "Estimated overbooking rate per passenger": f"\t\t{avg_overbooking_rate:.3f}%",
    f"\nOverbooking likelihood": f"1 in {one_in_x_passengers} passengers get overbooked." if one_in_x_passengers else "No overbookings"
}

# Print results
for strategy, result in results.items():
    print(f"\n{strategy} Strategy:")
    for key, value in result.items():
        print(f"{key}: {value}")
