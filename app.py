import shutil
import random
import sys
def start_program(): #стартовая функция с общей информацией
    columns = shutil.get_terminal_size().columns + 40
    print("\n" + "Игра быки и коровы".center(columns))
    print("""Для управления игровым процессом у тебя есть следующие команды:
     СТАРТ - для начала новой игры
     ПРАВИЛА - для вывода правил
     СТОП - полностью завершает игровой процесс""")
    user_comands(input("Твоя команда: ").upper())

def end_program(): #конечная функция при выходе
    print("Ты завершил игровой процесс, до новых встреч!\n\n")
    sys.exit()

def game_rules(): #функция вывода правил игры
    print("""Правила очень просты: я загадываю четырёхзначное число, а тебе нужно его отгадать. После каждого твоего варианта я буду сообщать
тебе количество быков и коров, где БЫК — это цифра, которая есть в загаданном числе и находится на той же позиции, а КОРОВА — это цифра, 
которая так же есть в числе, но находится не на своём месте. Помни, что числа могут быть и такой записи: 0032""")

def user_comands(user_comand): #функция распознования введенных команд пользователем
    while user_comand != "СТОП":
        if user_comand == "СТАРТ":
            start_game()
        elif user_comand == "ПРАВИЛА":
            game_rules()
        else:
            print("Такой команды нет. Попробуй ещё раз.")
        user_comand = input("Твоя команда: ").upper()
    end_program()

def start_game(): #функция начала новой игры
    hidden_num = str("{:0>4}".format(random.randrange(1, 9999)))
    print("\nИтааак... Четырехзначное число загадано. Твои варианты?")
    use_num = check_input()
    while not use_num:
        use_num = check_input()
    steps_game(use_num, hidden_num)
    while (hidden_num != use_num):
        use_num = check_input()
        while not use_num:
            use_num = check_input()
        steps_game(use_num, hidden_num)
    print("Поздравляю. Ты победил!!!")
    user_comands(input("\nТвоя команда: ").upper())

def check_input(): #проверка ввода числа в рамках игры
    input_num = input("Твой ответ: ")
    try:
        input_num = int(input_num)
    except ValueError:
        if input_num.upper() in ("СТАРТ", "СТОП", "ПРАВИЛА"):
            print("Текущий игровой процесс прерван.\n")
            user_comands(input_num.upper())
        else:
            print("Ввод некорректен. Попробуй ещё раз.")
    else:
        input_num = str(input_num)
        if len(input_num) > 4:
            print("Слишком большое число. Загадано было не более 4 знаков")
        elif len(input_num) <= 4:
            input_num = "{:0>4}".format(input_num)
            return input_num
    return

def counting_cows(count_c): #функция, корректирующая вывод при подсчёте "коров"
    numbering_c = ["КОРОВ", "КОРОВА", "КОРОВЫ", "КОРОВЫ", "КОРОВЫ"]
    return numbering_c[count_c]

def counting_bulls(count_b): #функция, корректирующая вывод при подсчёте "быков"
    numbering_b = ["БЫКОВ", "БЫК", "БЫКА", "БЫКА", "БЫКА"]
    return numbering_b[count_b]

def steps_game(estimated_number, true_number): #функция подсчёта "коров" и "быков"
    bulls_count = 0
    cows_count = 0
    check_string = true_number
    for index, element in enumerate(estimated_number):
        if true_number[index] == element:
            bulls_count += 1
            check_string = check_string[:index] + '-' + check_string[index+1:]
    for index, element in enumerate(estimated_number):
        if element in check_string:
            cows_count += 1
    print(f"В твоём числе {estimated_number} {bulls_count} {counting_bulls(bulls_count)} и {cows_count} {counting_cows(cows_count)}")
start_program() #вызов стартовой функции

#конец программы
