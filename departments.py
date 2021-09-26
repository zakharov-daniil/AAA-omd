def script():
    """Общий скрипт с выбором действия в задании"""
    print(
        'Выберите действие:\n'
        'Вывести иерархию команд -- 1\n'
        'Вывести сводный отчет по департаментам -- 2\n'
        'Сохранить сводный отчет в виде csv-файла -- 3\n'
    )
    option = ''
    options = {'1': 1, '2': 2, '3': 3}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()

    if options[option] == 1:
        return make_eirarchy_of_deps()
    elif options[option] == 2:
        return make_report()
    else:
        return make_csv_report()


def make_list_of_dict() -> ():
    """
    Возвращает Лист из словарей-записей из файла Corp Summary.csv И Словарь из названий Департаментов
    """
    import csv
    list_of_dict = []
    departments_dict = {}

    with open('Corp_Summary.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            departments_dict[row['Департамент']] = {}
            list_of_dict.append(row)

    return list_of_dict, departments_dict


def make_eirarchy_of_deps() -> {}:
    """
    Печатает Департаменты и Отделы с количеством работающих в них человек
    Возвращает словарь словарей { Департамент : { Отдел : N } }
    """
    list_of_dict = []
    departments_dict = {}

    list_of_dict, departments_dict = make_list_of_dict()

    for row in list_of_dict:
        if row['Отдел'] in departments_dict[row['Департамент']]:
            departments_dict[row['Департамент']][row['Отдел']] += 1
        else:
            departments_dict[row['Департамент']][row['Отдел']] = 1

    for department, dict in departments_dict.items():
        print(department, ': ')
        for k, v in dict.items():
            print('     ', k, ' : ', v, 'человек\n')

    return departments_dict


def make_report(printing: bool = True) -> {}:
    """
    Печатает Департаменты и сводную статистику по каждому из них
    Возвращает словарь { Департамент : { Свойство : Число } }
    """
    list_of_dict = []
    departments_dict = {}

    list_of_dict, departments_dict = make_list_of_dict()

    for department in departments_dict:
        departments_dict[department]['Численность'] = 0
        departments_dict[department]['Минимальная ЗП'] = 0
        departments_dict[department]['Максимальная ЗП'] = 0
        departments_dict[department]['Средняя ЗП'] = 0
        departments_dict[department]['Сумма'] = 0

    for row in list_of_dict:
        departments_dict[row['Департамент']]['Численность'] += 1

        if departments_dict[row['Департамент']]['Максимальная ЗП'] < int(row['Оклад']):
            departments_dict[row['Департамент']]['Максимальная ЗП'] = int(row['Оклад'])

        if departments_dict[row['Департамент']]['Минимальная ЗП'] == 0 \
                or departments_dict[row['Департамент']]['Минимальная ЗП'] > int(row['Оклад']):
            departments_dict[row['Департамент']]['Минимальная ЗП'] = int(row['Оклад'])

        departments_dict[row['Департамент']]['Сумма'] += int(row['Оклад'])

    for department in departments_dict:
        departments_dict[department]['Средняя ЗП'] = departments_dict[department]['Сумма'] /\
                                                     departments_dict[department]['Численность']

    if printing:
        for department, dict in departments_dict.items():
            print(department, ': ')
            for k, v in dict.items():
                if k != 'Сумма':
                    print('     ', k, ' : ', v, '\n')

    return departments_dict


def make_csv_report():
    """
    Сохраняет report.csv файл с Департаментами и сводной статистикой по каждому
    """
    import csv
    departments_dict = make_report(False)

    with open('report.csv', 'w', newline='') as file:
        fieldnames = ['Департамент', 'Численность', 'Минимальная ЗП', 'Максимальная ЗП', 'Средняя ЗП']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for department in departments_dict:
            writer.writerow({'Департамент': department,
                             'Численность': departments_dict[department]['Численность'],
                             'Минимальная ЗП': departments_dict[department]['Минимальная ЗП'],
                             'Максимальная ЗП': departments_dict[department]['Максимальная ЗП'],
                             'Средняя ЗП': departments_dict[department]['Средняя ЗП']})

    print('Файл report.csv успешно сохранён!\n')


if __name__ == '__main__':
    script()
