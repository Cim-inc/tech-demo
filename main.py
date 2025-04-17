import time
import random
import os

# Fake company data
companies = {
    "NovaDyne Systems (1963)": {
        "desc": "A Cold War-era military lab specializing in satellite AI and encryption.",
        "roles": ["Junior Cryptographer", "Radio Technician", "Security Auditor"]
    },
    "AetherCorp (1977)": {
        "desc": "A deep-physics research group developing quantum computing interfaces.",
        "roles": ["Quantum Analyst", "Containment Specialist", "System Operator"]
    },
    "Kronos Initiative (1986)": {
        "desc": "Think tank working on AI, time perception, and black-box simulations.",
        "roles": ["AI Observer", "Cognitive Engineer", "BlackBox Maintainer"]
    },
    "HelixPoint Technologies (1994)": {
        "desc": "Late-90s multimedia lab experimenting with simulated GUIs and virtual labs.",
        "roles": ["SysAdmin", "Interface Designer", "Data Analyst"]
    }
}

# ASCII intro banner
def banner():
    print("\n" + "="*60)
    print("   ██████╗ ███████╗██████╗ ██╗   ██╗███████╗")
    print("   ██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝")
    print("   ██████╔╝█████╗  ██████╔╝██║   ██║█████╗  ")
    print("   ██╔═══╝ ██╔══╝  ██╔═══╝ ██║   ██║██╔══╝  ")
    print("   ██║     ███████╗██║     ╚██████╔╝███████╗")
    print("   ╚═╝     ╚══════╝╚═╝      ╚═════╝ ╚══════╝")
    print("      TERMINAL SIMULATION - SCIENCE OPS v0.1")
    print("="*60 + "\n")

# Login simulation
def login_sim():
    username = input("LOGIN > Enter your employee ID: ")
    print("Verifying credentials...")
    time.sleep(1)
    print(f"ACCESS GRANTED: Welcome, {username.upper()}.\n")
    return username

# Simulate system interface
def terminal_loop(username, company, role):
    print(f"Logged into {company} as {role}.\n")
    print("Type `help` to see available commands.\n")

    while True:
        cmd = input(f"{company.split()[0]}::{role.lower().replace(' ', '_')} $ ").strip().lower()
        
        if cmd == "help":
            print("\nAvailable Commands:")
            print(" - help        : Show this help menu")
            print(" - status      : View system and user status")
            print(" - clearance   : Attempt to elevate access level")
            print(" - exit        : Log out\n")

        elif cmd == "status":
            print("\n--- SYSTEM STATUS ---")
            print(f"User: {username}")
            print(f"Role: {role}")
            print(f"System Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
            print("Security Level: CLASSIFIED")
            print("Pending Logs: 2 unread memos")
            print("----------------------\n")

        elif cmd == "clearance":
            print("Requesting elevated clearance...")
            time.sleep(1)
            if random.random() > 0.6:
                print("Access Granted: LEVEL 4 Clearance Unlocked.")
                print("New command available: `read_memos` (coming soon)\n")
            else:
                print("Access Denied: Clearance request flagged.\n")

        elif cmd == "exit":
            print("Logging out...")
            break

        else:
            print("Unknown command. Type `help`.\n")

# Role and company selection
def select_company():
    print("Available Companies:\n")
    for idx, name in enumerate(companies.keys(), 1):
        print(f"{idx}. {name}")
    choice = int(input("\nChoose your company [1-4]: ")) - 1
    selected_company = list(companies.keys())[choice]
    print(f"\n{selected_company}: {companies[selected_company]['desc']}\n")

    roles = companies[selected_company]["roles"]
    for idx, role in enumerate(roles, 1):
        print(f"{idx}. {role}")
    role_choice = int(input("\nSelect your job title [1-3]: ")) - 1
    return selected_company, roles[role_choice]

# Entry point
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    company, role = select_company()
    username = login_sim()
    terminal_loop(username, company, role)

if __name__ == "__main__":
    main()
