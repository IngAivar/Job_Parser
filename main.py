from classes.classes import HeadHunterAPI, JSONSaver
from utils.utils import sort_by_salary_min, sort_by_salary_max


def main():

    # keyword = input("Введите ключевое слово по которому будет искаться вакансия: ")
    keyword = "python"

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    # superjob_api = SuperJobAPI()

    # Получение вакансий с разных платформ
    hh_vacancies = hh_api.get_vacation(keyword)

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver(keyword)
    json_saver.add_vacancies(hh_vacancies)

    data = json_saver.select()
    data = sort_by_salary_min(data)
    data = sort_by_salary_max(data)

    for row in data:
        print(row, end=f"\n\n{'=' * 250}\n\n")
    # json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
    # json_saver.delete_vacancy(vacancy)

    # superjob_vacancies = superjob_api.get_vacancies("Python")
    #
    # Создание экземпляра класса для работы с вакансиями
    # vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.",
    #                   "Требования: опыт работы от 3 лет...")

    # Функция для взаимодействия с пользователем
    # def user_interaction():
    #     platforms = ["HeadHunter", "SuperJob"]
    #     search_query = input("Введите поисковый запрос: ")
    #     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    #     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    #     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
    #
    #     if not filtered_vacancies:
    #         print("Нет вакансий, соответствующих заданным критериям.")
    #         return
    #
    #     sorted_vacancies = sort_vacancies(filtered_vacancies)
    #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #     print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
