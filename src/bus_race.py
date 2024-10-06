import time
import random
import os

def clear_console():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_buses(bus1_position, bus2_position):
    bus1 = " " * bus1_position + "==BUS1=>"
    bus2 = " " * bus2_position + "==BUS2=>"
    print(bus1)
    print(bus2)
        
def bus_race():
    bus1_position = 0
    bus2_position = 0
    finish_line = 50  # Adjust the finish line as needed

    while bus1_position < finish_line and bus2_position < finish_line:
        clear_console()

        bus1_position += random.randint(0, 2)
        bus2_position += random.randint(0, 2)

        print_buses(bus1_position, bus2_position)

        time.sleep(0.2)

    clear_console()
    print_buses(bus1_position, bus2_position)

    # Determine the winner
    if bus1_position >= finish_line and bus2_position >= finish_line:
        print("Draw!")
    elif bus1_position >= finish_line:
        print("BUS 1 WINS!")
    else:
        print("BUS 2 WINS!")

if __name__ == "__main__":
    bus_race()
