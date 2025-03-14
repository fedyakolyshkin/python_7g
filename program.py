# Глобальные переменные для хранения состояния между играми
global_coins = {
    "Доллар США": 0,
    "Евро": 0,
    "Британский фунт стерлингов": 0,
    "Японская иена": 0
}

global_endings = []

def is_int(s):
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

def input_choice(title, variants, prompt):
    if title:
        print(title)
    for i in range(len(variants)):
        print(f"{i+1}: {variants[i]}")
    while True:
        choise = input(prompt)
        if is_int(choise):
            choise_int = int(choise)
            if choise_int > 0 and choise_int <= len(variants):
                return str(choise_int)
        print("Вы ввели неправильное значение. Повторите ввод")


def start_game():
    global global_coins, global_endings

    coins = global_coins
    endings = global_endings
    lockpicks = 4

    def collect_coin(coin_name, amount):
        if coin_name in coins:
            coins[coin_name] += amount

    def show_endings():
        print("Список концовок:")
        for i, ending in enumerate(endings, start=1):
            print(f"Концовка {i}: {ending}")

    def restart_game():
        print("Игра начнется заново.")
        start_game()

    choice = input_choice(
        "Вы играете за персонажа Токио. Вам не хватает денег на жизнь и вы решаете найти легкий способ заработка денег.",
        [
            "Пойти самой ограбить банк.",
            "Вступить в команду Профессора."
        ],
        "Ваш выбор: "
    )

    if choice == "1":
        weapons = [
            "HK-416",
            "Холодное оружие",
            "Автомат Калашникова",
            "UZI",
            "HK UMP",
            "QBZ-95",
            "Арбалет",
            "M60",
            "ДП-28",
            "Винтовка Мосина"
        ]
        weapon_choice = input_choice("Выберите оружие:", weapons, "Выбор оружия: ")
        print(f"Вы выбрали {weapons[int(weapon_choice) - 1]}.")

        hide_choice = input_choice("", [
            "Спрятать ружье под курткой.",
            "Спрятать в тубусе."
        ], "Ваш выбор: ")
        if hide_choice == "1":
            collect_coin("Доллар США", 1)
            print("Вы находите в куртке Доллар США, на нем написано маленькая цифра 5.")
            print("Неудача, вас заметили на входе и вызвали полицию(омон), вы проиграли.")
            endings.append("Вас заметили на входе и вызвали полицию.")
        elif hide_choice == "2":
            collect_coin("Евро", 1)
            print("На дне тубуса вы находите 1 Евро, сзади монетки кто-то выцарапал цифру 2.")
            print("Вы прошли сканер на входе, и охранник нажал тревожную кнопку, вас забрала полиция, вы проиграли.")
            endings.append("Вас забрала полиция на входе.")

        print("Вам удалось собрать монеты:")
        for coin, amount in coins.items():
            print(f"{coin}: {amount}")
        print("Введите 'пройти снова', чтобы начать заново, или 'посмотреть концовки', чтобы увидеть все концовки.")

        while True:
            command = input("Введите команду: ")
            if command == "пройти снова":
                restart_game()
                break
            elif command == "посмотреть концовки":
                show_endings()
                print("Введите 'пройти снова', чтобы начать заново.")

    elif choice == "2":
        conflict_choice = input_choice("Вы звоните профессору и предлагаете объединиться: вступить в команду профессора, вы знакомитесь с командой.", [
            "Промолчать.",
            "Отстоять себя."
        ], "Ваш выбор: ")
        if conflict_choice == "2":
            print("У вас теперь напряженные отношения с Берлином.")

        print("Вы приехали в Монетный Двор Испании и успешно захватили его вместе с заложниками.")

        costume_choice = input_choice("Вы с командой поставили заложников на колени и решаете:", [
            "Раздать им красные костюмы (такие же как у вас) и маски Сальвадора Дали.",
            "Не раздавать."
        ], "Ваш выбор: ")
        if costume_choice == "1":
            collect_coin("Британский фунт стерлингов", 1)
            print("Берлин дает вам Британский фунт стерлингов на краю купюры написано 4 красным карандашом.")
        elif costume_choice == "2":
            print("Вы узнаете, что полиция знает о вашей униформе (красные костюмы и маски) и проникает к вам через вентиляционную трубу.")
            print("Берлин настоятельно просит вас раздать костюмы и маски заложникам.")

            vent_choice = input_choice("", [
                "Согласиться.",
                "Отказать напрочь."
            ], "Ваш выбор: ")
            if vent_choice == "1":
                print("Полицейскому не удалось вычислить вас, ему не удалось проникнуть к вам.")
            elif vent_choice == "2":
                print("К вам проник полицейский и смог вычислить вас среди заложников. Полицейский успешно убивает вас. Игра окончена.")
                endings.append("Вас убил полицейский.")

                print("Собрание монет:")
                for coin, amount in coins.items():
                    print(f"{coin}: {amount}")
                print("Введите 'пройти снова', чтобы начать заново, или 'посмотреть концовки', чтобы увидеть все концовки.")

                while True:
                    command = input("Введите команду: ")
                    if command == "пройти снова":
                        restart_game()
                        break
                    elif command == "посмотреть концовки":
                        show_endings()
                        print("Введите 'пройти снова', чтобы начать заново.")

                return

        print("Новый акт: Полиция решает брать вас штурмом, но удача снова вам улыбается и штурм проваливается.")
        print("Однако, вас задела пуля и вы травмировали руку, вам необходимы бинты.")
        print("Вы заходите на склад и видите пять аптечек.")

        first_aid_kits = [
            "Бинтов нет, но в ней почему-то лежит Японская иена с номиналом 2.",
            "Тут нет ничего.",
            "Бинтов не видно.",
            "Агх, тут ничего нет.",
            "Нашлись, слава богу."
        ]

        while True:
            print("Выберите аптечку:")
            for i, kit in enumerate(first_aid_kits, start=1):
                print(f"Аптечка {i}")

            aid_choice = input("Ваш выбор (1-5): ")
            if aid_choice.isdigit() and 1 <= int(aid_choice) <= len(first_aid_kits):
                chosen_kit = first_aid_kits[int(aid_choice) - 1]
                print(chosen_kit)
                if "Японская иена" in chosen_kit:
                    collect_coin("Японская иена", 1)
                if "Нашлись, слава богу." in chosen_kit:
                    break
            else:
                print("Неверный выбор, попробуйте еще раз.")

        print("Вы успешно оказали себе первую помощь.")
        print("Пора приступить к основной задаче операции: взлом хранилища.")
        print("Вы спускаетесь на подземный этаж и думаете как взломать хранилище.")

        methods = ["взрывчатка", "лом", "электронный прибор", "отмычка", "выведать информацию у сотрудника банка"]
        while methods:
            method_choice = input_choice("Выберите метод взлома:", methods, "Ваш выбор: ")
            chosen_method = methods[int(method_choice) - 1]
            if chosen_method == "взрывчатка":
                print("Вам не удалось поджечь ее.")
                methods.remove("взрывчатка")
            elif chosen_method == "лом":
                print("Лом сломался от количества усилий, которые вы прилагали к нему.")
                methods.remove("лом")
            elif chosen_method == "электронный прибор":
                print("Из-за низкого заряда он разрядился быстрее, чем вы успели подойти к хранилищу.")
                methods.remove("электронный прибор")
            elif chosen_method == "отмычка":
                if lockpicks > 0:
                    lockpicks -= 1
                    print(f"Осталось попыток с отмычками: {lockpicks}")
                    if lockpicks == 0:
                        print("Все отмычки сломались.")
                        methods.remove("отмычка")
                    else:
                        print("Неудача, попробуйте еще раз.")
                else:
                    print("У вас больше нет отмычек.")
                    methods.remove("отмычка")
            elif chosen_method == "выведать информацию у сотрудника банка":
                print("Он в страхе убежал от вас и закрылся в туалете, вы решили не идти за ним.")
                methods.remove("выведать информацию у сотрудника банка")

        print("А что если напечатать деньги?")
        print_choice = input_choice("Вам необходимо запустить станок: Вы продолжаете выведывать информацию у сотрудника?", [
            "Да.",
            "Нет."
        ], "Ваш выбор: ")
        if print_choice == "1":
            print("У вас получается и вы запускаете станок. Вы напечатали деньги.")
        elif print_choice == "2":
            print("Неудача: у вас ничего не получается. Вы проиграли.")
            endings.append("Вы не смогли напечатать деньги.")

            print("Собрание монет:")
            for coin, amount in coins.items():
                print(f"{coin}: {amount}")
            print("Введите 'пройти снова', чтобы начать заново, или 'посмотреть концовки', чтобы увидеть все концовки.")

            while True:
                command = input("Введите команду: ")
                if command == "пройти снова":
                    restart_game()
                    break
                elif command == "посмотреть концовки":
                    show_endings()
                    print("Введите 'пройти снова', чтобы начать заново.")

        print("Третий акт: У вас заканчиваются патроны и продовольствие, отношения в команде становятся напряженными, поэтому вам необходимо совершить побег.")
        print("Профессор сообщил вам о тоннеле (подкоп), который находится в хранилище:")
        print("1: Попробовать снова взломать хранилище.")
        if lockpicks > 0:
            print("2: Попробовать использовать отмычки.")
        print("3: Пойти на сделку с полицией.")

        escape_choice = input("Ваш выбор: ")
        if escape_choice == "1":
            code = ""
            while code != "5242":
                code = input("Введите код для взлома хранилища: ")
            print("У вас получилось взломать хранилище. Вы успешно сбежали с деньгами. Вы выполнили миссию и прошли игру.")
            endings.append("Вы успешно сбежали с деньгами.")
        elif escape_choice == "2" and lockpicks > 0:
            if lockpicks > 0:
                lockpicks -= 1
                print(f"Осталось попыток с отмычками: {lockpicks}")
                if lockpicks == 0:
                    print("Все отмычки сломались.")
                else:
                    print("Неудача, попробуйте еще раз.")
            else:
                print("У вас больше нет отмычек.")
        elif escape_choice == "3":
            print("Полиция обвела вас вокруг пальца и вы проиграли.")
            endings.append("Полиция обвела вас вокруг пальца.")

        print("Собрание монет:")
        for coin, amount in coins.items():
            print(f"{coin}: {amount}")
        print("Введите 'пройти снова', чтобы начать заново, или 'посмотреть концовки', чтобы увидеть все концовки.")

        while True:
            command = input("Введите команду: ")
            if command == "пройти снова":
                restart_game()
                break
            elif command == "посмотреть концовки":
                show_endings()
                print("Введите 'пройти снова', чтобы начать заново.")

start_game()