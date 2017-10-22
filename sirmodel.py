# infection.py (infectorSimulation)

import numpy as npy
from scipy.integrate import odeint
import matplotlib.pyplot as ppt 

# Call target population, inital infected, initial vaccinated, and write derivative equations

# Initialization of visualization parameters and constants
# N is target population (UNIT: units)
# I0 is target infected population (UNIT: units)
# V0 is target vaccinated population (UNIT: units)
# R0 is target recovered population (UNIT: units)
# S0 is target susceptible population (UNIT: units)
# t is elapsed time (always starts at zero) (UNIT: days)
N, I0, V0, R0, S0, t = 0
beta, gamma = 0
t = npy.linspace(0, 200, 200)  # Sets x-label limits

def derivSIR(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * (S * I/N)
    dIdt = beta * (S * I/N) - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions for SIR diffEq
y0 = S0, I0, R0

# Integrate SIR equations over t (time)
integSIR = odeint(derivSIR, y0, t, args=(N, beta, gamma))
S, I, R = integSIR.T

# Plot data on three separate f(t)-t curves: S(t), I(t), and R(t)
fig = ppt.figure(facecolor="w")
axis = fig.add_subplot(111, axis_bgcolor="#DDDDDD", axisbelow=True)
axis.plot(t, S/1000, "b", alpha=0.5, lw=2, label="Susceptible Persons")  # Plotting Susceptible persons
axis.plot(t, I/1000, "g", alpha=0.5, lw=2, label="Infected Persons")  # Plotting Infected persons
axis.plot(t, R/1000, "r", alpha=0.5, lw=2, label="Recovered Persons (with Immunity)")  # Plotting Recovered persons (Immune)
axis.set_xlabel("Time (days)")  # Set x-label
axis.set_ylabel("Number of persons (1000s)")  # Set y-label
axis.set_ylim(0, 2)  # Set limit to y-label (x-label is already set by linspace command above)
axis.xaxis.set_tick_params(length=0)  # Disable x-axis axial tick marks
axis.yaxis.set_tick_params(length=0)  # Disable y-axis axial tick marks
axis.grid(b=True, which="major", c="w", lw=2, ls="-")  # Sets some grid parameters
legend = axis.legend()
legend.get_frame().set_alpha(0.5)
for spine in ("top", "right", "bottom", "left"):
    axis.spines[spine].set_visible(False)
ppt.show()  # Displays graph using MatPlotLib
