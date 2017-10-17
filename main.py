# main.py (infectorSimulation)

import random, sys


# Function that takes no inputs from command-line but starts game
def simulation_start():
    play_counter = 0

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n\nWelcome to the Infector Simulation.\n\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")

    prompt_intro()

    # Uncomment to utilize the 'Multiple Viruses' stretch challenge
    """
    if self.play_counter < 1:
        # Simply select a virus and continue through simulation        
    elif:
        # Ask user if they want to run simulation again with same virus or pick a new virus
    """

    population_size = int(input("\nHow large is the target population?\n> "))
    vaccinated_percentage = float(input("\nWhat percentage of the target population is vaccinated against the selected virus?\n> "))
    virus_name = str(input("What is the name/type of the target virus?\n> "))


# Function that prompts the user to display or skip the introductory message
def prompt_intro():
    intro_choice = str(input("Would you like to read the Infector Simulation introduction? (y/n)\n>"))

    if (intro_choice.lower() == "y"):
        print("\nUser input is valid. Displaying introduction...\n")
        display_intro()
    elif (intro_choice.lower() == "n"):
        print("\nUser input is valid. Skipping introduction...\n")
    else:
        print("\nUser input is invalid. Please try again.\n")
        prompt_intro()


# Function that accepts the user's choice to display the introduction
def display_intro():
    print("The Infector Simulation allows a user to manipulate a target population with a potentially deadly virus.\n")
    print("With the Infector Simulation, you as the user can adjust a target population's size, immunity, and vulnerability\n to a hazardous virus/contagion under pseudo-stochastic parameters.\n")
    print("You will now be prompted to select population and virus-characteristic parameters and run the simulation.\n\n")
    
    input(">> Press any key to continue...\n")

    print("NOTE: Once parameters are selected, they cannot be altered. Please confirm each parameter before running simulation.\n")
    
    input(">> Press any key to continue...\n")


# Function that accepts simulation_start parameters and plays the game while initializing all user inputs
def simulation_play():
    pass