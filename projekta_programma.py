total = []

language = int(input("Choose the language: 1 - english, 2 - latviešu, 3 - русский: "))

if language == 1: # english
    langEnterName = "Please enter your name: "
    langQuestList = ", You have entered the list of guests invited to your holiday. Do you want to add a guest list? (1 - yes, 2 - no): "
    langQuestTotal = "How many guests there will be: "
    langQuestName = "Enter the name of the guest: "
    langQuestListSee = "Would you like to see the guest list? (1 - yes, 2 - no): "
    langComeHoliday = "Will come to the holiday: "
    langVacationPlace = "Do you want to choose a place to stay? (1 - yes, 2 - no): "
    langPlace = "Do you want to spend your vacation in the city or outside the city? (1 - in the city, 2 - outside the city): "
    langPlaceCity = "Choose a place: (1 - In a cafe or restaurant, 2 - in entertainment centers, 3 - at home): "
    langPlaceNature = "Choose a place: (1 - outdoors, 2 - in a bath, 3 - on a lake, river: "
    langThanks = "Thanks, we'll try!"
    langError = "The entered value is incorrect, go back to the beginning and be careful!"

if language == 2: # latvian
    langEnterName = "Lūdzu, ievadiet savu vārdu: "
    langQuestList = ", Jūs esat ievadījis viesu sarakstu, kas uzaicināti uz jūsu brīvdienām. Vai vēlaties pievienot viesu sarakstu? (1 - jā, 2 - nē): "
    langQuestTotal = "Cik viesu būs: "
    langQuestName = "Ievadiet viesa vārdu: "
    langQuestListSee = "Vai vēlaties redzēt viesu sarakstu? (1 - jā, 2 - nē): "
    langComeHoliday = "Nāks uz svētkiem: "
    langVacationPlace = "Vai vēlaties izvēlēties nakšņošanas vietu? (1 - jā, 2 - nē): "
    langPlace = "Vai vēlaties pavadīt atvaļinājumu pilsētā vai ārpus pilsētas? (1 - pilsētā, 2 - ārpus pilsētas): "
    langPlaceCity = "Izvēlieties vietu: (1 - kafejnīcā vai restorānā, 2 - izklaides centros, 3 - mājās): "
    langPlaceNature = "Izvēlieties vietu: (1 - ārā, 2 - vannā, 3 - ezerā, upē: "
    langThanks = "Paldies, mēs mēģināsim!"
    langError = "Ievadītā vērtība nav pareiza, atgriezieties sākumā un esiet uzmanīgs!"

if language == 3: # russian
    langEnterName = "Введите свое имя: "
    langQuestList = ", Вы зашли в список гостей, приглашенных на ваш праздник. Хотите добавить список гостей? (1 - да, 2 - нет): "
    langQuestTotal = "Сколько будет гостей: "
    langQuestName = "Введите имя гостя: "
    langQuestListSee = "Хотите ли увидеть список гостей? (1 - да , 2 - нет): "
    langComeHoliday = "На праздник придут: "
    langVacationPlace = "Хотите выбрать место для отдыха? (1 - да , 2 - нет): "
    langPlace = "Хотите провести отпуск в городе или за городом? (1 - в городе , 2 - за городом): "
    langPlaceCity = "Выберите место: (1 - В кафе или ресторане, 2 - в развлекательных центрах, 3 - дома): "
    langPlaceNature = "Выберите место: (1 - на открытом воздухе, 2 - в бане, 3 - на озере, реке: "
    langThanks = "Спасибо, постараемся!"
    langError = "Введено не верное значение, вернись в начало и будь внимательнее!"

#####################################################################

if language <= 3: # Проверяем наличие ввода правильного выбора языка
    print(input(langEnterName), end="" )
    questList = int(input(langQuestList))

    if questList == 1: # Добовляем гостей в список
        questTotal = int(input(langQuestTotal)) # Спрашиваем сколько будет гостей
        for i in range(1, questTotal + 1):
            questName = str(input(langQuestName)) # Узнаем имена гостей
            total.append(questName) # Записываем имена гостей в массив

        questListSee = int(input(langQuestListSee)) # Нужно ли показывать список гостей
        if questListSee == 1: # Показываем список гостей
            print((langComeHoliday), end="\r\n")
            for i in range(len(total)):
                print(total[i], end="\r\n") # Выводим имена гостей из массива и указываем 'разделитель'
            print('')
        elif questListSee == 2: # Не показываем список гостей
            print(end="")
        else:
            print(langError) # Вывод сообщения ошибки
#########################################################################################################################
        vacationPlace = int(input(langVacationPlace)) # Узнаем, нужно ли выберать место для отдыха
        if vacationPlace == 1: # Выбераем месть для отдыха
            place = int(input(langPlace)) #  Выбор между городом или за городом
            if place == 1: # Варианты мест отдыха в городе
                l = int(input(langPlaceCity))
                if 1 <= l <= 3:
                    print(langThanks) # Вывод благодарности
                else:
                    print(langError) # Вывод сообщения ошибки
            elif place == 2: # Варианты мест отдыха за городе
                k = int(input(langPlaceNature))
                if 1<= k <= 3:
                    print(langThanks) # Вывод сообщения благодарности
                else :
                    print(langError) # Вывод сообщения ошибки
            else: 
                print(langError)# Вывод сообщения ошибки
        elif vacationPlace == 2: # Не выбераем месть для отдыха
            print(langThanks) # Вывод сообщения благодарности
        else:
            print(langError)# Вывод сообщения ошибки
###############################################################################################################################
    elif questList == 2: # Не добовляем гостей в список
        vacationPlace = int(input(langVacationPlace)) # Узнаем, нужно ли выберать место для отдыха
        if vacationPlace == 1: # Выбераем месть для отдыха
            place = int(input(langPlace)) #  Выбор между городом или за городом
            if place == 1: # Варианты мест отдыха в городе
                l = int(input(langPlaceCity))
                if 1 <= l <= 3:
                    print(langThanks) # Вывод благодарности
                else:
                    print(langError) # Вывод сообщения ошибки
            elif place == 2: # Варианты мест отдыха за городе
                k = int(input(langPlaceNature))
                if 1<= k <= 3:
                    print(langThanks) # Вывод сообщения благодарности
                else :
                    print(langError) # Вывод сообщения ошибки
            else: 
                print(langError)# Вывод сообщения ошибки
        elif vacationPlace == 2: # Не выбераем месть для отдыха
            print(langThanks) # Вывод сообщения благодарности
        else:
            print(langError)# Вывод сообщения ошибки
    
    else: # Ошибка программы при вводе данных
        print(langError)# Вывод сообщения ошибки
else:
    print('"Non-existing language selected", "Выбран не существующий язык", "Atlasīta neesoša valoda"')