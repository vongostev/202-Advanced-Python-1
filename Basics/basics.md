
# Условия задач по теме "Основы языка Python"

При выполнении заданий не на *HackerRank* пользуемся следующим протоколом. 
Для каждого блока пишется файл с именем вида **block_NumOfBlock.py***.
В теле файла описываются функции и классы, выполнение тестов идет в блоке `__main__`.
Тесты представляют собой вызовы функций и методов классов, подтверждающие правильность работы программы.
Тестирование можно проводить с помощью конструкции `assert`:
```python
assert function_to_test(args) == correct_answer
```

## Основы Python. ДЗ

### Блок 1. Базовый синтаксис

15 первых задач из [списка на HackerRank](https://www.hackerrank.com/domains/python)

### Блок 2. Строки и файлы

Блок делится на 2 части:
1. Задачи на *Hackerrank*: [Find a string](https://www.hackerrank.com/challenges/find-a-string/problem), [String validators](https://www.hackerrank.com/challenges/string-validators/problem), [Text alignment](https://www.hackerrank.com/challenges/text-alignment/problem), [Text wrap](https://www.hackerrank.com/challenges/text-wrap/problem), [String Formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem), [Capitalize](https://www.hackerrank.com/challenges/capitalize/problem)
2. Задачи на формирование, запись и чтение файлов.
- Создать файл, содержащий числа от 1 до 10 на одной строке, разделенные пробелом.

- Создать файл, содержащий числа от 1 до 10, каждое число на новой строке.

- Создать файл со строками вида "Number X set to address Y", где вместо X надо подставить число от 256 до 300, а вместо Y -- его `id`

- Считать файл, созданный на предыдущем шаге. Выделить X и Y, вывести информацию на экран в виде таблицы со строками вида `| строка длиной 5 символов | строка длиной 15 символов |`. Строки внутри ячеек выравнивать по центру.

- Считать прилагаемый файл `log.txt`. Формат строки `date - module [ type   ] message`. Если строка не удовлетворяет шаблону -- её надо пропустить. Провести анализ:

1. Сформировать словарь с ключами -- значениями поля `module` и значениями -- словарями с ключами -- типами сообщений `(DEBUG, INFO, WARNING, ERROR)` и значениями -- количествами сообщений каждого типа.
То есть на выходе должен быть словарь вида:
`{'module1': {'DEBUG': 0, 'INFO': 121, 'WARNING': 1, 'ERROR': 0}, 'module2': {...}}`

2. Найти, сколько раз в логе встречается строка с заданной подстрокой `fun:`.

3. \* Сформировать список количества найденных мод (в строках типа **Found 307 modes ...**)

### Блок 3

![image](https://i0.wp.com/suit.by/wp-content/uploads/Coming-Soon.png?ssl=1 "Also")
