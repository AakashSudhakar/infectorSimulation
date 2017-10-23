# logger.py

class Logger(object):


    def __init__(self, file_name):
        self.file_name = file_name


    def write_data(self, total_population, persons_vaccinated, virus_type, mortality_rate, reproduction_rate):
        file = open("./" + self.file_name, "w")
        data = ("{}\t{}\t{}\t{}\t{}\n").format(total_population, persons_vaccinated, virus_type, mortality_rate, reproduction_rate)

        file.write(data) 
        file.close()


    def write_log_interact(self, person_sick, person_subject, infection_occur=None, person_subject_is_vaccinated=None, person_subject_is_sick=None):
        log_interact = "{}\t{}\t{}\t{}\t{}\n".format(person_sick._id, person_subject._id, infection_occur, person_subject_is_vaccinated, person_subject_is_sick)

        with open("./" + self.file_name, "a") as log_file:
            log_file.write(log_interact)


    def write_log_survival(self, person_subject, survive_infection):
        e = ""

        if not survive_infection:
            e = "succumbed to the infection and died."
        else:
            e = "survived the infection."

        survival_status = "{} {}\n".format(person_subject, e)

        with open("./" + self.file_name, "a") as log_file:
            log_file.write(survival_status)

    
    def write_log_time_step(self, time_step_num):
        with open("./" + self.file_name, "a") as log_file:
            log_file.write("Current time step #{} has ended. \nStarting time step #{}...\n".format(time_step_num, time_step_num + 1))