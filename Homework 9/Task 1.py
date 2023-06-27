# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
import re

# Считываем оригинальный файл
with open("test_file/task1_data.txt", "r", encoding="utf-8") as file:
    text = file.readlines()

# Записываем в новый файл строки из оригинального, заменив в них все числа (используя регулярные выражения)
with open("test_file/task1_answer.txt", "w", encoding="utf-8") as result:
    for raw in text:
        result.write(re.sub(r"\d+", r"", raw))


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", "r", encoding="utf-8") as file1:
    with open("test_file/task1_ethalon.txt", "r", encoding="utf-8") as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
