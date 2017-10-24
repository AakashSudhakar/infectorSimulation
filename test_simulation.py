# test_simulation.py (infectorSimulation)

import os
from RUN_FROM_HERE_simulation import Simulation

def test_simulation_run():
    assert Simulation(1000, 0.10, "KashKiller", 0.50, 1.25, 1)

def test_simulation_operation():
    os.system("python ./RUN_FROM_HERE_simulation.py 1000 0.10 KashKiller 0.50 1.25 1")
