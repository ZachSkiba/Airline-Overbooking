import numpy as np
import matplotlib.pyplot as plt

# Triangular distribution parameters for delay by route type
tri_params = {
    'domestic': (1, 2, 6),
    'international': (4, 8, 24)
}

# Logistic loyalty loss function based on delay
def logistic_loyalty_loss(h, L, k, h0):
    return L / (1 + np.exp(-k * (h - h0)))

# Simulate delay and loyalty loss cost for a single passenger
def simulate_one_passenger(route_type, L, k, h0, clv):
    a, b, c = tri_params[route_type]
    delay = np.random.triangular(a, b, c)
    loss_rate = logistic_loyalty_loss(delay, L, k, h0)
    cost = clv * loss_rate
    return cost, delay, clv, loss_rate

# Run a simulation to estimate expected cost per bumped passenger
def simulate_expected_cost(n_passengers, route_type, L, k, h0, clv):
    costs = [simulate_one_passenger(route_type, L, k, h0, clv)[0] for _ in range(n_passengers)]
    return np.mean(costs), costs

# Parameters for each case
cases = {
    "Domestic - Involuntary":     {'route': 'domestic',     'L': 1, 'k': 0.5, 'h0': 0,  'clv': 2500},
    "Domestic - Voluntary":       {'route': 'domestic',     'L': 1, 'k': 0.5, 'h0': 4,  'clv': 2500},
    "International - Involuntary":{'route': 'international','L': 1, 'k': 0.3, 'h0': 0,  'clv': 7125},
    "International - Voluntary":  {'route': 'international','L': 1, 'k': 0.3, 'h0': 12, 'clv': 7125},
}

# Run simulations
results = {}
for label, params in cases.items():
    mean_cost, cost_list = simulate_expected_cost(100000, params['route'], params['L'], params['k'], params['h0'], params['clv'])
    results[label] = {
        'mean_cost': mean_cost,
        'costs': cost_list,
        'params': params
    }
    print(f"{label} -> Expected Cost: ${mean_cost:.2f}")

# Plot logistic loss curves
plt.figure(figsize=(10, 6))
h_vals = np.linspace(0, 24, 200)

for label, data in results.items():
    L, k, h0 = data['params']['L'], data['params']['k'], data['params']['h0']
    loss_rates = [logistic_loyalty_loss(h, L, k, h0) for h in h_vals]
    plt.plot(h_vals, loss_rates, label=label)

plt.title('Logistic Loyalty Loss Curves by Scenario')
plt.xlabel('Delay (hours)')
plt.ylabel('Loss Rate')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
