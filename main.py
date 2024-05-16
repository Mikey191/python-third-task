#// data = {'todo1': 'Поиграть в футбол', 'todo2': 'купить хлеб'}

# Открытие файла data.js и чтение его содержимого
with open(r'data.js', 'r', encoding="utf-8") as file:
    content = file.read()

# Получение строки только с данными без data =
start = content.find('{')
end = content.rfind('}')
data_str = content[start+1:end]
print(data_str)

# Создание списка старых дел
lst_data = data_str.split(", ")
# Создание словаря старых дел
todo_dict_data = dict()
# Добавление обработанных данных (без ковычик " или ') в словарь
for todo in lst_data:
    temp = todo.split(":")
    key = ""
    value = ""
    #Этот цикл обрабатывает строку так, что бы осталось содержимое без " или '
    for i in range(0, len(temp)):
        str_result = temp[i].strip()
        if str_result.startswith("\"") or str_result.endswith("\"") or str_result.startswith("\'") or str_result.endswith("\'"):
            str_result = str_result[1:-1]
        if i == 0:
            key = str_result
        if i == 1:
            value = str_result
    todo_dict_data[key] = value

print(todo_dict_data)

# Добавление нового дела
new_todo = input("Введите новое дело: ")
todo_dict_data[f"todo{len(todo_dict_data) + 1}"] = new_todo
print(todo_dict_data)

# Запись нового дела в список
with open(r"data.js", "w", encoding="utf-8") as result:
    result.write(
        f"data = {todo_dict_data}"
    )
