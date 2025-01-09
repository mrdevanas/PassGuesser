import sys
import time
import tqdm
from colorama import Fore, Style, init

# تهيئة colorama
init(autoreset=True)

def generate_numbers(number_input):
    """Generate a list of numbers from input while keeping leading zeros if needed."""
    numbers = []

    for part in number_input.split(','):
        part = part.strip()
        if '_' in part:
            try:
                num_underscores = part.count('_')
                if num_underscores == 1:
                    start, end = part.split('_')
                    start, end = int(start), int(end)
                    numbers.extend([str(i) for i in range(start, end + 1)])
                elif num_underscores == 2:
                    start, end = part.split('__')
                    start, end = int(start), int(end)
                    if start > end:
                        raise ValueError("Start number must be less than or equal to end number.")
                    width = len(str(end))
                    numbers.extend([f"{i:0{width}}" for i in range(start, end + 1)])
                else:
                    print(Fore.RED + "Error: Invalid format. Use 'start_end' or 'start__end'." + Style.RESET_ALL)
                    return []
            except ValueError as ve:
                print(Fore.RED + f"Error: {ve}. Please enter a valid range." + Style.RESET_ALL)
        else:
            if part.isdigit() or part.startswith('0'):
                numbers.append(f"{int(part):0{len(part)}}")
            else:
                print(Fore.RED + f"Error: '{part}' is not a valid number." + Style.RESET_ALL)

    return numbers

def main():
    print(Fore.GREEN + "Welcome to the Wordlist Generator!")

    # طلب الأرقام
    while True:
        numbers_input = input(Fore.YELLOW + "Enter Numbers (like: 1_100 or 1__100): ")
        if numbers_input.strip():
            if numbers_input.strip() == "-6":
                print(Fore.RED + "Exiting the program..." + Style.RESET_ALL)
                sys.exit()
            break
        else:
            print(Fore.RED + "Error: Please enter valid numbers." + Style.RESET_ALL)

    # طلب الأسماء
    while True:
        user_input = input(Fore.YELLOW + "Enter Name (or more names, separated by commas, like: Mohamed, Ayman): ")
        if user_input.strip():
            if user_input.strip() == "-6":
                print(Fore.RED + "Exiting the program..." + Style.RESET_ALL)
                sys.exit()
            if not all(part.isdigit() for part in user_input.split(',')):
                break
            else:
                print(Fore.RED + "Error: Please enter valid names (cannot be numbers only)." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Error: Please enter valid names." + Style.RESET_ALL)

    # طلب اسم ملف wordlist
    while True:
        wordlist_name = input(Fore.YELLOW + "Enter Name of word list (like: tst): ")
        if wordlist_name.strip():
            break
        else:
            print(Fore.RED + "Error: Please enter a valid file name." + Style.RESET_ALL)

    print(Fore.GREEN + "Generating wordlist...")

    # توليد الأرقام والقائمة
    number_list = generate_numbers(numbers_input)
    names = user_input.split(',')
    output_lines = []

    # عرض التقدم أثناء عملية الإنشاء
    for number in tqdm.tqdm(number_list, desc="Processing Numbers", unit="number"):
        for name in names:
            name = name.strip()
            output_lines.append(f"{number}{name}")
            output_lines.append(f"{number}{name.capitalize()}")
            output_lines.append(f"{number} {name}")
            output_lines.append(f"{number} {name.capitalize()}")

    # حفظ النتيجة في ملف
    with open(f"{wordlist_name}.txt", "w") as file:
        file.write("\n".join(output_lines))

    print(Fore.GREEN + f"Wordlist saved in {wordlist_name}.txt (Time taken: {time.process_time()} seconds)" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
