# simulation.py (infectorSimulation)

import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):

    def __init__(self, total_population, persons_vaccinated, virus_type, mortality_rate, reproduction_rate, initial_infected=1):
        self.total_population = total_population
        self.pop = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.persons_vaccinated = persons_vaccinated
        self.virus_type = virus_type
        self.mortality_rate = mortality_rate
        self.reproduction_rate = reproduction_rate

        self.file_name = "{}_simulation-{}-{}-{}".format(virus_type, total_population, persons_vaccinated, initial_infected)
        self._virus = Virus(virus_type, mortality_rate, reproduction_rate)

        self.logger = Logger(self.file_name)

        self.new_infected = []

        self.population = self._make_population(total_population, initial_infected, persons_vaccinated)


    def _make_population(self, population_size, initial_infected, persons_vaccinated):
        pop = []
        infected_pop = 0
        make_id = 0

        while len(population) != population_size:
            make_id = len(pop)

            if infected_pop != initial_infected:
                pop.append( Person(make_id, False, self._virus) )
                infected_pop += 1
            else:
                if random.random() < persons_vaccinated:
                    pop.append( Person(make_id, True) )
                else:
                    pop.append( Person(make_id, False) )

        return pop


    def simulation_should_continue(self):
        for person in self.pop:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False


    def simulation_run()