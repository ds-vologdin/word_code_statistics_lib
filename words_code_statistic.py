import sys
import argparse
from code_parse import get_top_verbs_in_path, get_top_functions_names_in_path
import logging


def convert_str_to_logging_level(level_str=None):
    level = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    return level.get(level_str, logging.WARNING)


def parse_argv():
    description_programm = '''Приложение для проведения лексического анализа \
программного кода'''
    parser = argparse.ArgumentParser(description=description_programm)
    parser.add_argument(
        '--path',
        help='''Пути к каталогам, где требуется провести анализ кода.
Можно указать несколько катологов в кавычках:
    '/home/bill/coding/ /home/alisa/coding/' '''
    )
    parser.add_argument(
        '--top-size', type=int, default=20,
        help='Ограничивает вывод количества слов.'
    )
    parser.add_argument(
        '--log-level',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
        default='warning',
        help='Уровень вывода логов. По умолчанию warning.'
    )
    parser.add_argument(
        '--log-file', default='{}.log'.format(__file__.rstrip('.py')),
        help='Имя логфайла. По-умолчанию {}.log'.format(__file__.rstrip('.py'))
    )
    return parser.parse_args()


def get_projects_in_path(path=''):
    if not path:
        return []
    return path.split()


def output_statistic_to_stdout(statistic):
    # ТОП слов
    print('='*80)
    print('| {0:<60}|{1:^15} |'.format('verbs', 'occurence'))
    print('='*80)
    for word, occurence in statistic['words_top']:
        print('| {0:<60}|{1:^15} |'.format(word, occurence))
    print('='*80)
    # ТОП имён функций
    print('='*80)
    print('| {0:<60}|{1:^15} |'.format('function name', 'occurence'))
    print('='*80)
    for word, occurence in statistic['functions_names_top']:
        print('| {0:<60}|{1:^15} |'.format(word, occurence))
    print('='*80)


def main(args):
    args = parse_argv()

    logging.basicConfig(
        filename=args.log_file,
        level=convert_str_to_logging_level(args.log_level),
        format='%(asctime)s:%(levelname)s:%(message)s'
    )

    projects = get_projects_in_path(path=args.path)
    if not projects:
        print('no projects...no statistics...')
        return None
    # Считаем статистику
    words_top = []
    functions_names_top = []

    for path_project in projects:
        words_top.extend(get_top_verbs_in_path(path_project, args.top_size))
        functions_names_top.extend(
            get_top_functions_names_in_path(path_project, args.top_size)
        )

    statistic = {
        'top_size': args.top_size,
        'words_top': words_top,
        'projects': projects,
        'functions_names_top': functions_names_top,
    }
    output_statistic_to_stdout(statistic)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
