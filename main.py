import sys
from pathlib import Path
from classes.connection import ConnectorJson
from utility.utils_menu import select_keyword, select_service, create_request, select_experience
from utility.utils import get_hh_from_url
from classes.jobs_classes import sorting, get_top, HHVacancy, SJVacancy

path = Path('jobs.json')


def main():
    print('Здравствуйте!', 'Вас Приветствует сервис для "удобной" сортировки вакансий!\n', sep='\n')

    connector = ConnectorJson(path)

    while True:
        user_selection = input('Введите 1 если хотите обновить данные.\n'
                               ' Нажмите любую клавишу если хотите работать с существующими.\n'
                               '  0 - Выход: ')
        if user_selection == '1':
            del connector.data_file
            input_services = select_service()
            input_keyword = select_keyword()
            print('Ожидайте идет сбор данных...')
            create_request(input_services, input_keyword)
        elif user_selection == '0':
            sys.exit()

        user_input = input('''Выберите номер операции: 
                            1. Отфильтровать вакансии по опыту работы
                            2. Отсортировать вакансии по зп
                            3. Вывести вакансии  топ N вакансий по зп
                            4. Поиск по ключевому слову в описании вакансии: ''')
        if user_input == '1':
            select_user_experience = select_experience()
            result = connector.select({'experience': select_user_experience})
            if result:
                for i in result:
                    print(HHVacancy(**i) if get_hh_from_url(i['url']) else SJVacancy(**i))
            else:
                print('По вашему запросу нет данных')
        elif user_input == '2':
            result_list = connector.select({})
            vacancy = [HHVacancy(**i) if get_hh_from_url(i['url']) else SJVacancy(**i) for i in result_list]

            for item in sorting(vacancy):
                print(item)
        elif user_input == '3':
            number = input('Введите число вакансий что хотите вывести: ')
            result_list = connector.select({})
            vacancy = get_top([HHVacancy(**i) if get_hh_from_url(i['url'])
                               else SJVacancy(**i) for i in result_list], int(number))
            for item in vacancy:
                print(item)
        elif user_input == '4':
            word = input('Введите слово по которому хотите отфильтровать вакансии: ')
            result_list = connector.select_for_keyword(word)
            if result_list:
                for item in result_list:
                    print(HHVacancy(**item) if get_hh_from_url(item['url']) else SJVacancy(**item))
            else:
                print('По вашему ключевому слову ничего не найдено')
