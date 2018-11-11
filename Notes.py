back = "b"
while back == "b":
    print('Доступные файлы: "my" и "facts"')
    file_selected = input("Файл, который вы хотите открыть для чтения: ")
    print("")

    if file_selected == "my":
        with open("My.txt", "r") as my_file_1:
            text = my_file_1.read()
            print(text,"\n")
            text_copy = input('Введите текст, который вы хотите добавить в "facts": ')


# Возможность возврата к списку доступных файлов
            back = input('Если хотите вернуться к выбору файла введите "b": ')
            print("")




    elif file_selected == "facts":
        with open("facts.txt", "r") as my_file_2:
            text = my_file_2.read()
            print(text)
            print(text, "\n")
            text_copy = input('Введите текст, который вы хотите добавить в "my": ')
            back = input('Если хотите вернуться к выбору файла введите "b": ')
            print("")
