# Voice Assistant Program
# main.py
# Author: Thomas Good - 13/02/22

import os
import sys
import query

def printMenu():
    print("Welcome to Voice Assistance Application");
    print("Please select an option from the menu");
    print("1. Text-based assistance (enabled for dev)");
    print("2. Voice assistance");
    print("3. Quit");

def readQuery():
    expression = input("How can I help? ");
    response = query.scan(expression);
    print(response);

printMenu();

option = input("Option: ");

if option == "1":
    print("You picked Text-based assistance.");
    readQuery();
elif option == "2":
    print("You picked Voice-based assistance.");
elif option == "3":
    print("Goodbye!");
else:
    print("Invalid option.");
    printMenu();

