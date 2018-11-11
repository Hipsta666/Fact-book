back = "н"
while back == "н":
    print('Доступные файлы: "Мне нравится" и "Факты"')
    file_selected = input("Файл, который вы хотите открыть для чтения: ")
    print("")
    if file_selected != "Мне нравится" and file_selected != "Факты":
        print("Такого файла не существует, выбирайте из доступных.")

    try:
        if file_selected == "Мне нравится" and "мне нравится":
            with open("My.txt", "r+") as my_file_1:
                text_1 = my_file_1.read()
                print(text_1, "\n")
                text_copy_1 = input('Введите текст, который '
                'вы хотите добавить в "Факты": ')
                text_copy_1 = text_copy_1 + "\n"
                if text_copy_1 not in text_1:
                    print("Такого текста тут нет.")
                else:
                    if len(text_copy_1) > 90:
                        print("Извините, но текст слишком длинный для "
                              "добавления")
                    else:
                        with open("facts.txt", "a+") as f_21:
                            record = f_21.write(text_copy_1)
                        print('Текст добавлен в файл "Факты"')
                        print("")
                back = input('Если хотите вернуться к выбору файла '
                             'введите "н",если нет, то что угодно: ')
                print("")

        elif file_selected == "Факты":
            with open("facts.txt", "r+") as my_file_2:
                text_2 = my_file_2.read()
                print(text_2, "\n")
                text_copy_2 = input('Введите текст, который вы хотите '
                                    'добавить в "Мне нравится": ')
                text_copy_2 = text_copy_2 + "\n"
                if text_copy_2 not in text_2:
                    print("Такого текста тут нет.")
                else:
                    if len(text_copy_2) > 90:
                        print("Извините, но текст слишком длинный "
                              "для добавления")
                    else:
                        with open("My.txt", "a+") as f_12:
                            record = f_12.write(text_copy_2)
                        print('Текст добавлен в файл "Мне нравится"')
                        print("")
                back = input('Если хотите вернуться к выбору '
                             'файла введите "н",если нет, то что угодно: ')
                print("")
    except UnicodeDecodeError:
        print("К сожалению, текст, который вы хотели добавить, оказался с"
              " не той кодировкой.")
print("До скорого.")
