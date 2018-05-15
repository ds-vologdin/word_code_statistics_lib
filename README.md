# code_parse

Библиотека позволяет оценить на сколько часто используются в проектах те или иные лексические конструкции: глаголы в именах функций и как часто повторяются имена функций.

## Установка
Установка из git:
```
git clone https://github.com/ds-vologdin/word_code_statistics_lib.git
```

## Как использовать
Пример использования библиотеки продемонстрирован ниже.
```
from code_parse import get_top_verbs_in_path, get_top_functions_names_in_path


top_size = 30
path_project = '/home/developer/code/'

words_top = get_top_verbs_in_path(path_project, top_size)
functions_names_top = get_top_functions_names_in_path(path_project, top_size)
```
## words_code_statistic.py
Пример использования библиотеки представлен в words_code_statistic.py.

Парметры приложения:
```
--path PATH          Пути к каталогам, где требуется провести анализ кода.
                    Можно указать несколько катологов в кавычках:
                    '/home/bill/coding/ /home/alisa/coding/'
--top-size TOP_SIZE  Ограничивает вывод количества слов
```
