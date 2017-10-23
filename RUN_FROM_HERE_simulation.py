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

        self.population = self.make_population(total_population, initial_infected, persons_vaccinated)


    def make_population(self, population_size, initial_infected, persons_vaccinated):
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


    def simulation_run(self):
        self.logger.write_data(self.total_population, self.persons_vaccinated, self.virus_type, self.mortality_rate, self.reproduction_rate)
        time_step_count = 0

        is_continue = self.simulation_should_continue()

        while is_continue:
            self.time_step()
            is_continue = self.simulation_should_continue()
            time_step_count += 1
            self.logger.write_log_time_step(time_step_count)

        print("After {} continuous time steps (cycles), this simulation has concluded."+format(time_step_count))

    def time_step(self):
        interact_count = 0

        while interact_count < 100:
            for person in self.pop:
                if person.infected and person.is_alive:
                    iterate = True

                    while iterate:
                        rand_person_id = random.randint(0, self.total_population - 1)
                        rand_person = self.pop(rand_person_id)

                        if rand_person.is_alive:
                            self.log_interact(person, rand_person)
                            interact_count += 1
                            iterate = False
        
        self.infect_new_infected()

        for person in self.pop:
            if person.person_survives_infection():
                self.logger.write_log_survival(person._id, True)
            else:
                self.logger.write_log_survival(person._id, False)


    def infect_new_infected(self):
        for person in self.new_infected:
            person.infect(self._virus)

        self.new_infected = []


    def interact(self, person, rand_person):
        assert person.is_alive = True
        assert rand_person.is_alive = True

        if rand_person.is_vaccinated:
            self.logger.write_log_interact(person, rand_person, None, "VACCINATED")
        
        if rand_person.infected:
            self.logger.write_log_interact(person, rand_person, None, "INITIALLY INFECTED")

        roll = random.random()
        if roll < self.reproduction_rate:
            self.new_infected.append(rand_person)
            self.logger.write_log_interact(person, rand_person, "DID INFECT")


if __name__ = "__main__":
    params = sys.argv[1:]
    total_population = int(params[0])
    persons_vaccinated = float(params[1])
    virus_type = str(params[2])
    mortality_rate = float(params[3])
    reproduction_rate = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(total_population, persons_vaccinated, virus_type, mortality_rate, reproduction_rate, initial_infected)
    simulation.run()