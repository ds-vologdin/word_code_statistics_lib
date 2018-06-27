import collections
from nltk import pos_tag

from ast_tree import get_trees, get_all_names_in_tree
from ast_tree import get_functions_names_in_ast_tree


def flatten_list(not_flat_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return [item for sublist in not_flat_list for item in sublist]


def is_verb(word):
    ''' Проверка на глагол '''
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def get_verb_from_name(name):
    if not name:
        return []
    return [word for word in name.split('_') if is_verb(word)]


def split_snake_case_name_to_words(name):
    ''' Разбить имя на слова '''
    if not name:
        return []
    return [n for n in name.split('_') if n]


def get_all_words_in_path(path):
    ''' Получить все слова используемые в текстовых файлах каталога path '''
    trees = [t for t in get_trees(path) if t]
    names = flatten_list([get_all_names_in_tree(t) for t in trees])
    # Исключаем магические функции
    names = [
        f for f in names if not (f.startswith('__') and f.endswith('__'))
    ]
    return flatten_list(
        [split_snake_case_name_to_words(name) for name in names]
    )


def get_top_verbs_in_path(path, top_size=10):
    ''' Получить ТОП используемых глаголов в каталоге path '''
    trees = [t for t in get_trees(path) if t]
    function_names_in_code = flatten_list(
        [get_functions_names_in_ast_tree(t) for t in trees]
    )
    # Удаляем магию
    names_in_code = [
        name for name in function_names_in_code
        if not (name.startswith('__') and name.endswith('__'))
    ]
    words = flatten_list([get_verb_from_name(name) for name in names_in_code])

    return collections.Counter(words).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    ''' Получить ТОП используемых имён функций в каталоге path'''
    trees = get_trees(path)
    # Формируем список имён в ast деревьях
    names = [
        f for f in flatten_list(
            [get_functions_names_in_ast_tree(t) for t in trees if t]
        ) if not (f.startswith('__') and f.endswith('__'))
    ]
    return collections.Counter(names).most_common(top_size)
