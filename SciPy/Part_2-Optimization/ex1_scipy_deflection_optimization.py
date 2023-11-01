from scipy.optimize import minimize

# Constants
P = 10  # kN
L = 5  # meters
E = 200_000  # kN/m^2
I_min = 1e-6  # m^4

# Objective function: Max deflection to be minimized
def max_deflection(I):
    return (P * L ** 3) / (48 * E * I)

# Constraint: I should be >= I_min
constraints = ({'type': 'ineq', 'fun': lambda I: I - I_min})

# Initial guess
I_initial = 2e-6  # m^4

# Optimization
result = minimize(max_deflection, I_initial, constraints=constraints)

# Extract optimized value of I
I_optimized = result.x[0]

print(f"Optimized Moment of Inertia: {I_optimized:.3e} m^4")