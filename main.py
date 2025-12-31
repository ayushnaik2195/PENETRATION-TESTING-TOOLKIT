from port_scanner import port_scanner
from brute_forcer import brute_forcer
from banner_grabber import banner_grabber

def menu():
    print("\n--- PENETRATION TESTING TOOLKIT ---")
    print("1. Port Scanner")
    print("2. Brute Force Login")
    print("3. Banner Grabbing")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        target = input("Enter target IP: ")
        port_scanner(target)

    elif choice == "2":
        url = input("Enter login URL: ")
        brute_forcer(url)

    elif choice == "3":
        target = input("Enter target IP: ")
        port = int(input("Enter port: "))
        banner_grabber(target, port)

    elif choice == "4":
        exit()
    else:
        print("Invalid choice!")

menu()
