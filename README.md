В проекті містяться модулі: main.py, TK_1.py, TK_2.py, TK_3.py, TK_4.py, TK-5.py та скрипт запуску start.sh.

Модуль TK_1.py містить функцію inputlist(), яка надає користувачу інтерфейс введення з консолі значень та їх привласнення до списку й повернення списку з функції. В якості параметру, функція приймає ціле значення кількості значень для введення.

Модуль TK_2.py містить функцію minmaxcortege(), яка приймає в якості параметру список та повертає кортеж з мінімального та максимального значень.

Модуль TK_3.py містить функцію divavrg(), яка приймає в якості параметру список та повертає список, кожний елемент якого – це значення, яке поділене на середнє значення цього списку.

Модуль TK_4.py містить функцію multiavrg(), яка приймає в якості параметру список та повертає список, кожний елемент якого – це значення, яке помножене на середнє значення цього списку.

Модуль TK-5.py містить функцію sqrtlist(), яка приймає в якості параметру список та повертає список, кожний елемент якого – це значення, яке отримане після операції взяття квадратного кореня з вхідного елементу списку.

Модуль main.py містить імпорти TK-модулей і їх фунцій. В функції main реалізовано послідовне виконання функцій з TK-модулей. Також в модулі main.py імпортовано importlib для використання модуля TK-5.py без перейменування.

Для того, щоб модуль main.py можна було виконати в ОС Ubuntu, необхідно встановити віртуальне середовище Python, якщо воно відсутнє. Встановлення відбувається за допомогою команди: sudo apt install python3-venv Для того, щоб виконати цю команду, необхідно мати права суперкористувача. Далі необхідно перейти до каталогу, де ви хочете зберегти нове віртуальне середовище та створити його командою: python3 -m venv ім'я_каталогу. Далі необхідно перенести модулі main.py, TK_1.py, TK_2.py, TK_3.py, TK_4.py, TK-5.py та скрипт запуску start.sh до каталогу з віртуальним середовищем, після чого необхідно відкрити термінал та ввести наступну команду: ./start.sh
