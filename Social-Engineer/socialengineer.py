from Mailer.mass_mailer import mass_mailer
from Mailer.mailer import mailer
from websitecloner.testrun import main
from websitecloner.cloners.webmodcloner import clone_website
from emailHarvester.email_harvester import main_menu
import pyfiglet

def run():
    while True:  # Start of the loop
        try:
            print(pyfiglet.figlet_format("SOCIAL ENGINEER"))
            print("Welcome to the Social Engineer")
            print("1. Web Cloner")
            print("2. Email Harvester")
            print('3. Credential Harvester')
            print("4. Single Mailer")
            print("5. Mass Mailer")
            print("99. Exit")
            option = input('Which type of service do you require?: ')
            
            if option == "1":
                clone_website()
            elif option == "2":
                main_menu()      
            elif option == "3":
                main()
            elif option == "4":
                mailer()
            elif option == "5":
                mass_mailer()
            elif option == "99":
                print("Exiting program...")
                break  # Exit the while loop to end the program
            else:
                print("Wrong input")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")
            input("Press Enter to continue...")
     
run()
