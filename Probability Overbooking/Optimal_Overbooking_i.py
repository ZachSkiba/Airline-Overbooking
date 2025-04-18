import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_flights = 100  # Total flights per day
seats_per_flight = 400  # Seats available per flight
no_show_rate = 0.075  # Base no-show rate
num_simulations = 10000  # Number of Monte Carlo trials

# Range of overbooked seats to test
booking_levels = range(420, 450)  

best_overbooking_rate = None
best_prob_within_range = 0
best_avg_overbooking_rate = 0


results = {}

for booked_per_flight in booking_levels:
    overbooked_passengers_per_day = []
    
    #Monte Carlo simulation
    for _ in range(num_simulations):
        show_up = np.random.binomial(booked_per_flight, 1 - no_show_rate, num_flights) #passanger show-up count
        overbooked = np.maximum(0, show_up - seats_per_flight) # number of overbooked passangers
        overbooked_passengers_per_day.append(np.sum(overbooked)) #add overbooked to list
    
    # Convert to NumPy array
    overbooked_passengers_per_day = np.array(overbooked_passengers_per_day)
    total_passengers_per_day = num_flights * booked_per_flight
    overbooking_rate_per_passenger = overbooked_passengers_per_day / total_passengers_per_day * 100
    
    # Define and calculate acceptable range
    lower_bound, upper_bound = 0.05, 0.15  
    prob_within_range = np.mean((overbooking_rate_per_passenger >= lower_bound) & (overbooking_rate_per_passenger <= upper_bound))
    prob_above_range = np.mean(overbooking_rate_per_passenger > upper_bound)
    prob_below_range = np.mean(overbooking_rate_per_passenger < lower_bound)
    avg_overbooking_rate = np.mean(overbooking_rate_per_passenger)
    
    # Store results
    results[booked_per_flight] = {
        "prob_within_range": prob_within_range * 100,
        "prob_above_range": prob_above_range * 100,
        "prob_below_range": prob_below_range * 100,
        "avg_overbooking_rate": avg_overbooking_rate,
    }
    
    # Determine best overbooking rate
    if prob_within_range > best_prob_within_range:
        best_prob_within_range = prob_within_range
        best_overbooking_rate = booked_per_flight
        best_avg_overbooking_rate = avg_overbooking_rate

# Plot results
fig, ax = plt.subplots(figsize=(10, 5))
overbooking_rates = [results[b]["avg_overbooking_rate"] for b in booking_levels]
ax.plot(booking_levels, overbooking_rates, marker='o', linestyle='-')
ax.set_xlabel("Passangers Per Flight out of 400")
ax.set_ylabel("Average Overbooking Rate (%)")
ax.set_title("Optimizing Overbooking Levels (0.1% Getting Overbooked)")
plt.axvline(best_overbooking_rate, color='r', linestyle='--', label=f'Best: {best_overbooking_rate} passangers \n {best_avg_overbooking_rate:.4f}% getting overbooked ')
plt.legend()
plt.grid()
plt.show()


print(f"Best overbooking level: {best_overbooking_rate} passengers per flight with an average overbooking rate of {best_avg_overbooking_rate:.4f}%")