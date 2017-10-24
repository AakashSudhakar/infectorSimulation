# test_person.py (infectorSimulation)

import pytest
from person import Person
from virus import Virus

def test_person_survives_infection():
    i = 0

    test_virus = Virus("Kash Krunk Killer", 0.5)

    for i in range(1000):
        aakash = Person("Aakash", False, test_virus)
        aakash.person_survives_infection()
        if aakash.is_alive:
            i += 1

    assert i > 490 and i < 510