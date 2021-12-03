#!/usr/bin/env python3
#!/usr/bin/env python2

import argparse
import motordriver as mot
import os


def main(command):
    print("Parsing string...")

    command_string = ""
    spec_string = ""

    seperator_count = 0
    spec_count = 0
    command_count = 3

    for element in command:
        if element == '"':
            seperator_count += 1
            spec_count = 0
        elif element == ':' and seperator_count == command_count:
            spec_count = 1
        elif seperator_count == command_count and not spec_count:
            command_string += element
        elif spec_count:
            spec_string += element

    # os.system('python main.py')

    # check if mission is running
    if any(os.scandir("mission_live/")):
        return

    stp = mot.stamp()
    stp.init()

    if command_string == "command_WAGON_RIGHT":
        print("Wagen fährt " + spec_string + " Schritt(e) nach rechts...")
        # TODO: call function to move wagon right
    elif command_string == "command_WAGON_LEFT":
        print("Wagen fährt " + spec_string + " Schritt(e) nach links...")
        # TODO: call function to move wagon left
    elif command_string == "command_WAGON_HOME":
        print("Wagen fährt auf die Ausgangsposition...")
        # TODO: call function to send wagon home
    elif command_string == "command_STAMP_UP_DOWN":
        print("Hubkolben fährt auf " + spec_string + " Prozent...")
        percentage = int(spec_string)
        stp.control(percentage)
    elif command_string == "command_STAMP_RIGHT":
        print("Stempel fährt " + spec_string + " Schritt(e) nach rechts...")
        # TODO: call function to move stamp right
    elif command_string == "command_STAMP_LEFT":
        print("Stempel fährt " + spec_string + " Schritt(e) nach links...")
        # TODO: call function to move stamp left
    elif command_string == "command_STAMP_HOME":
        print("Stempel fährt auf die Ausgangsposition...")
        stp.control(0)
    elif command_string == "stop_engine":
        print("Motoren werden vom Strom getrennt...")
        # TODO: call function to stop the engines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Callback for Live Mission Commands')
    parser.add_argument('MissionParams', help='')
    args = parser.parse_args()
    main(args.MissionParams)



