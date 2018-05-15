import os
import ast


def get_tree(filename):
    file_content = ''
    try:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            file_content = attempt_handler.read()
    except:
        return None
    try:
        return ast.parse(file_content)
    except SyntaxError:
        return None


def get_tree_with_file_content(filename):
    file_content = ''
    try:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            file_content = attempt_handler.read()
    except:
        return None
    try:
        return (filename, ast.parse(file_content), file_content)
    except SyntaxError:
        return None


def get_trees(path):
    ''' Функция формирования ast деревьев из .py файлов, расположенных
        в каталоге path
    '''
    filenames = get_filenames_in_path(path)
    # Собираем список ast деревьев
    return [get_tree(filename) for filename in filenames]


def get_trees_with_filenames(path):
    filenames = get_filenames_in_path(path)
    return [(filename, get_tree(filename)) for filename in filenames]


def get_trees_with_files_content(path):
    filenames = get_filenames_in_path(path)
    return [get_tree_with_file_content(filename) for filename in filenames]


def get_all_names_in_tree(tree):
    ''' Получить все имена из ast дерева '''
    if not tree:
        return []
    return [
        node.id for node in ast.walk(tree) if isinstance(node, ast.Name)
    ]


def get_functions_names_in_ast_tree(tree):
    ''' Получить список названий функций в дереве ast '''
    if not tree:
        return []
    return [
        node.name.lower()
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    ]


def get_filenames_in_path(path):
    ''' Получить все имена файлов с расширение .py в папке (рекурсивно) '''
    if not path:
        return []
    filenames = []
    for dirname, dirs, files in os.walk(path, topdown=True):
        # формируем список файлов с расширением .py в каждой папке
        filenames_current = [
            os.path.join(dirname, filename)
            for filename in files if filename.endswith('.py')
        ]
        # Накапливаем результат
        filenames += filenames_current
    return filenames
