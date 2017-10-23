# subject.py (infectorSimulation)

# import main

class Person(object):

    def __init__(self, _id, is_vaccinated, infected=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.infected = infected
        self.is_alive = True

    
    def infection_occurrence(self, infection_id):
        self.infected = infection_id


    def person_survives_infection(self):
        if not self.is_vaccinated:
            rand = random()

            if rand < self.infected.mortality_rate:
                self.is_alive = False
                return False
        return True