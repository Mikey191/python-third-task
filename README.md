# Python.
# Третий урок.

### План на урок:
1. Словари в Python.
2. Методы словарей.
3. Работа с файлами в Python.


## Словари в Python.

В Python **словарь (dictionary)** - это **изменяемая структура данных**, которая представляет собой **коллекцию** пар **ключ-значение**.

### Основные особенности словаря в Python:
1. Ключи в словаре должны быть уникальными и неизменяемыми (например, строки, числа или кортежи), а значения могут быть любого типа данных.
2. Словари являются неупорядоченными, то есть элементы в словаре не имеют определенного порядка.
3. Словари в Python являются изменяемыми, поэтому можно добавлять, изменять и удалять элементы.

### Создание словаря:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
### Доступ к значениям по ключу:
```python
value = my_dict['key1']
```
### Изменение значения по ключу:
```python
my_dict['key2'] = 'new value'
```
### Добавление новой пары ключ-значение:
```python
my_dict['key4'] = 'value4'
```
### Удаление элемента по ключу:
```python
del my_dict['key3']
```
### Проверка наличия ключа в словаре:
```python
if 'key1' in my_dict:
    # код, выполняемый, если ключ присутствует в словаре
```
### Получение списка всех ключей и значений в словаре:
```python
keys = my_dict.keys()
values = my_dict.values()
```
### Итерация по словарю:
```python
for key, value in my_dict.items():
    # код, выполняемый для каждой пары ключ-значение
```

## Методы словаря и примеры их использования:

### clear(): удаляет все элементы из словаря.
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
my_dict.clear()
print(my_dict)  # Output: {}
```
### copy(): создает копию словаря.
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```
### get(key[, default]): возвращает значение по ключу. Если ключ не найден, возвращает значение по умолчанию (если указано).
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
value = my_dict.get('key1', 'Not Found')
print(value)  # Output: value1

value = my_dict.get('key4', 'Not Found')
print(value)  # Output: Not Found
```
### items(): возвращает список кортежей, содержащих пары ключ-значение.
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
items = my_dict.items()
print(items)  # Output: dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
```
### keys(): возвращает список всех ключей в словаре.
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['key1', 'key2', 'key3'])
```
### pop(key[, default]): удаляет элемент по ключу и возвращает его значение. Если ключ не найден, возвращает значение по умолчанию (если указано).
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
value = my_dict.pop('key2')
print(value)  # Output: value2

value = my_dict.pop('key4', 'Not Found')
print(value)  # Output: Not Found
```
### popitem(): удаляет и возвращает произвольную пару ключ-значение из словаря.
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
key, value = my_dict.popitem()
print(key, value)  # Output: key3 value3
```
### update(other): обновляет словарь, добавляя пары ключ-значение из другого словаря или итерируемого объекта.
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2'}
other_dict = {'key3': 'value3', 'key4': 'value4'}
my_dict.update(other_dict)
print(my_dict)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
```
### values(): возвращает список всех значений в словаре.
Пример использования:
```python
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
values = my_dict.values()
print(values)  # Output: dict_values(['value1', 'value2', 'value3'])
```

## Работа с файлами в Python.
В Python существует несколько способов работы с файлами. Один из наиболее распространенных способов - использование функции **open()** для открытия файла и методов чтения или записи для работы с его содержимым.  
### Примеры использования функции open() и методов чтения и записи:

### Открытие файла для чтения:
```python
with open('file.txt', 'r') as f:
    # код для чтения файла
```
В этом случае файл file.txt открывается в режиме чтения ('r'), что позволяет программе только читать содержимое файла.

### Открытие файла для записи:
```python
with open('file.txt', 'w') as f:
    # код для записи в файл
```
В этом случае файл file.txt открывается в режиме записи ('w'), что позволяет программе записывать новое содержимое в файл. Если файл уже существует, его содержимое будет перезаписано.

### Открытие файла для добавления данных:
```python
with open('file.txt', 'a') as f:
    # код для добавления данных в файл
```
В этом случае файл file.txt открывается в режиме добавления ('a'), что позволяет программе добавлять новые данные в конец файла, не перезаписывая его содержимое.

### Чтение содержимого файла:
```python
with open('file.txt', 'r') as f:
    data = f.read()
```
В этом случае метод read() используется для чтения содержимого файла целиком и сохранения его в переменную data.

### Запись в файл:
```python
with open('file.txt', 'w') as f:
    f.write('Hello, world!')
```
В этом случае метод write() используется для записи строки 'Hello, world!' в файл.

### Чтение файла построчно:
```python
with open('file.txt', 'r') as f:
    for line in f:
        # код для обработки каждой строки
```
В этом случае файл читается построчно, и каждая строка доступна в переменной line для дальнейшей обработки.

## Способы Cчитать данные с файла:
Чтобы считать данные с файла с использованием Python, вы можете использовать функцию open() для открытия файла и методы чтения, такие как read(), readline(), или readlines(), для чтения содержимого файла.  
Примеры использования:
### read() - читает содержимое файла целиком и возвращает его в виде строки:
```python
with open('file.txt', 'r') as f:
    data = f.read()
```
### readline() - читает одну строку из файла:
```python
with open('file.txt', 'r') as f:
    line = f.readline()
```
### readlines() - читает все строки из файла и возвращает их в виде списка:
```python
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

# Создание проекта TODOLIST.
## Задача:  
### 1. Создать сайт на котором будет отображаться список дел.
### 2. Проект сайта должен содержать следующие файлы:
   1. index.html - файл с основной html разметкой
   2. style.css - файл для стилизации index.html
   3. app.js - файл с основным функционалом JavaScript
   4. data.js - файл со словарем списка дел

### Файл index.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>Document</title>
  </head>
  <body>
    <div class="todo">
      <h1>МОЙ TODOLIST</h1>
      <ul class="todo-list"></ul>
    </div>
    <script src="data.js"></script>
    <script src="app.js"></script>
  </body>
</html>
```

### Файл style.css
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  background-color: #212121;
  color: antiquewhite;
}
h1 {
  margin-bottom: 25px;
}
.todo {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  font-size: 50px;
  text-transform: uppercase;
}
.item {
  list-style: none;
  margin-bottom: 50px;
  padding: 20px;
}
```

### Файл app.js
```javascript
// Получение ссылки на элемент ul
const todoList = document.querySelector(".todo-list");

// Создание элементов li и добавление их в список ul
for (const key in data) {
  const todoItem = document.createElement("li");
  todoItem.textContent = data[key]; // Добавление информации из data по ключу
  todoItem.classList.add("item"); // Добавление класса "item"
  todoList.appendChild(todoItem); // Добавление li в ul
}
```

### Файл data.js
```javascript
data = {'todo1': 'Поиграть в футбол', 'todo2': 'Купить хлеб'}
```
### 3. Создать программу на языке Python, которая будет считывать информацию из файла app.js и добавлять туда новые дела через терминал.

## Алгоритм решения:
### 1. Открытие файла data.js и чтение его содержимого
```python
with open(r'data.js', 'r', encoding="utf-8") as file:
    content = file.read()
```
### 2. Получение строки только с данными без data =
```python
start = content.find('{')
end = content.rfind('}')
data_str = content[start+1:end]
print(data_str)
```
### 3. Создание списка старых дел
```python
lst_data = data_str.split(", ")
```
### 4. Создание словаря старых дел
```python
todo_dict_data = dict()
```
### 5. Добавление обработанных данных (без ковычик " или ') в словарь
```python
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
```
### 6. Добавление нового дела в словарь старых дел
```python
new_todo = input("Введите новое дело: ")
todo_dict_data[f"todo{len(todo_dict_data) + 1}"] = new_todo
print(todo_dict_data)
```
### 7. Запись нового дела в файл
```python
with open(r"data.js", "w", encoding="utf-8") as result:
    result.write(
        f"data = {todo_dict_data}"
    )
```

## Файл main.py
```python
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
```