import os  # إضافة مكتبة os
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

    # طلب إدخال الأرقام
    while True:
        numbers_input = input(Fore.YELLOW + "Enter Numbers (like: 1_100 or 1__100): ")
        if numbers_input.strip():  # تحقق مما إذا كان الإدخال غير فارغ
            break
        else:
            print(Fore.RED + "Error: Please enter valid numbers." + Style.RESET_ALL)

    # توليد الأرقام وعرضها
    number_list = generate_numbers(numbers_input)  # تحويل الإدخال إلى قائمة أرقام
    if number_list:  # تأكد من أن القائمة ليست فارغة
        # طلب اسم ملف wordlist
        while True:
            wordlist_name = input(Fore.YELLOW + "Enter Name of word list (like: numbers_list): ")
            if wordlist_name.strip():
                break
            else:
                print(Fore.RED + "Error: Please enter a valid word list name." + Style.RESET_ALL)

        # حفظ الأرقام في ملف
        with open(f"{wordlist_name}.txt", "w") as file:
            # عرض التقدم أثناء الكتابة باستخدام tqdm
            for number in tqdm.tqdm(number_list, desc="Saving numbers", unit="number"):
                file.write(f"{number}\n")
        print(Fore.GREEN + f"Number list saved in {wordlist_name}.txt" + Style.RESET_ALL)

        # بعد إتمام العملية، استخدام sys.exit للخروج بشكل صحيح
        print(Fore.GREEN + "Exiting..." + Style.RESET_ALL)
        sys.exit()  # إنهاء البرنامج

if __name__ == "__main__":
    main()
