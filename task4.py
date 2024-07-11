def remove_strings_without_russian_letters(массив):
    russian_letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    def есть_минимум_две_русские_буквы(string):
        кол_русских_букв = sum(1 for letter in string if letter.lower() in russian_letters)
        return кол_русских_букв >= 2

    отфильтрованный_массив = [string for string in массив if есть_минимум_две_русские_буквы(string)]

    return отфильтрованный_массив


# Пример использования функции
массив_строк = ['Привет', 'Hello', '123', 'аа', 'бб', 'Всем пока!','world', 'абд','к','у','beauty']
результат = remove_strings_without_russian_letters(массив_строк)
print(результат)
