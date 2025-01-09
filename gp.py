import os
import sys
from colorama import Fore, Style, init
import time
import tqdm

# تهيئة colorama
init(autoreset=True)

def generate_numbers(number_input):
    """Generate a list of numbers from input while keeping leading zeros if needed."""
    numbers = []  # قائمة للأرقام الناتجة

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

    while True:
        # طلب إدخال الأسماء
        while True:
            user_input = input(Fore.YELLOW + "Enter Name (or more names, separated by commas, like: Mohamed, Ayman): ")
            if user_input.strip():
                if user_input.strip() == "-6":  # تحقق إذا كان الإدخال هو -6 للخروج
                    print(Fore.RED + "Exiting the program..." + Style.RESET_ALL)
                    sys.exit()
                if not all(part.isdigit() for part in user_input.split(',')):  # التحقق من الأسماء
                    break
                else:
                    print(Fore.RED + "Error: Please enter a valid name (cannot be empty or numbers only)." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Error: Please enter a valid name (cannot be empty or numbers only)." + Style.RESET_ALL)

        # طلب إدخال الأرقام
        while True:
            numbers_input = input(Fore.YELLOW + "Enter Numbers (like: 1_100 or 1__100): ")
            if numbers_input.strip():  # تحقق مما إذا كان الإدخال غير فارغ
                if numbers_input.strip() == "-6":  # تحقق إذا كان الإدخال هو -6 للخروج
                    print(Fore.RED + "Exiting the program..." + Style.RESET_ALL)
                    sys.exit()
                break
            else:
                print(Fore.RED + "Error: Please enter valid numbers." + Style.RESET_ALL)

        # طلب اسم ملف القائمة
        while True:
            wordlist_name = input(Fore.YELLOW + "Enter Name of word list (like: tst): ")
            if wordlist_name.strip():  # تحقق مما إذا كان الإدخال غير فارغ
                if wordlist_name.strip() == "-6":  # تحقق إذا كان الإدخال هو -6 للخروج
                    print(Fore.RED + "Exiting the program..." + Style.RESET_ALL)
                    sys.exit()
                break
            else:
                print(Fore.RED + "Error: Please enter a valid file name." + Style.RESET_ALL)

        print(Fore.GREEN + "Generating wordlist...")

        # توليد الأرقام والقائمة
        number_list = generate_numbers(numbers_input)
        names = user_input.split(',')
        output_lines = []

        # عرض التقدم أثناء عملية الإنشاء
        for name in tqdm.tqdm(names, desc="Processing Names", unit="name"):
            name = name.strip()
            for number in number_list:
                output_lines.append(f"{name}{number}")
                output_lines.append(f"{name.capitalize()}{number}")
                output_lines.append(f"{name.capitalize()} {number}")
                output_lines.append(f"{name} {number}")

        # حفظ النتيجة في ملف
        with open(f"{wordlist_name}.txt", "w") as file:
            file.write("\n".join(output_lines))

        print(Fore.GREEN + f"Wordlist saved in {wordlist_name}.txt (Time taken: {time.process_time()} seconds)" + Style.RESET_ALL)

        # الخروج من البرنامج بعد إنشاء الملف
        print(Fore.RED + "Exiting the program..." + Style.RESET_ALL)
        sys.exit()

if __name__ == "__main__":
    main()
