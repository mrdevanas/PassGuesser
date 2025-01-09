import os

# Define some colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def show_info():
    print(f"{Colors.OKGREEN}info :{Colors.ENDC}")
    print(f"{Colors.OKBLUE}v-tools : 1.0{Colors.ENDC}")
    print(f"{Colors.OKBLUE}created by  : mrdevanas{Colors.ENDC}")

def main():
    print(f"{Colors.HEADER}Choose a number :{Colors.ENDC}")
    print(f"{Colors.OKGREEN}1-{Colors.ENDC} Creat ps1")
    print(f"{Colors.OKGREEN}2-{Colors.ENDC} Creat ps2")
    print(f"{Colors.OKGREEN}3-{Colors.ENDC} Creat ps3")
    print(f"{Colors.OKGREEN}4-{Colors.ENDC} Info")
    
    choice = input("=> ")

    if choice == "1":
        os.system('python gp.py') 

    elif choice == "2":
        os.system('python gp2.py') 
        
    elif choice == "3":
        os.system('python fn.py')
        
        
    elif choice == "4":
        show_info()
        
    else:
        print(f"{Colors.FAIL}Choose the correct number!{Colors.ENDC}")

if __name__ == "__main__":
    main()
