from data import documents, directories
from decorators import write_to_log, write_to_log_path

LIST_COMMANDS = '''
p – выводит имя человека, по введенному номеру документа;
s – выводит номер полки, на которой находится документ с введенным номером;
l – выводит список всех документов
a – добавляет новый документ в каталог и в перечень полок
q - выход
'''

LOG_PATH_PAR = 'logs/log_p.txt'

@write_to_log_path(LOG_PATH_PAR)
def find_doc(num):
    o_id = None
    for id, doc in enumerate(documents):
        if num == doc["number"]:
            o_id = id
    return o_id


@write_to_log
def find_shelf(num):
    o_key = None
    for k, v in directories.items():
        if num in v:
            o_key = k
    return o_key


@write_to_log
def people(num):
    id = find_doc(inum)
    if id is not None:
        print(documents[id]["name"])
    else:
        print(f"Документа с номером {inum} нет.")


@write_to_log
def shelf(num):
    o_key = find_shelf(num)
    if o_key is not None:
        print(o_key)
    else:
        print(f"Документ с номером {num} не найден на полках.")


def list():
    for el in documents:
        type, number, name = el.values()
        print(type, number, name)


def add():
    itype = input('Введите тип документа: ')
    inum = input('Введите номер документа: ')
    iname = input('Введите имя владельца: ')
    ishelf = input('Введите номер полки: ')

    id = find_doc(inum)
    if id is not None:
        print(f"Документ с номером {inum} уже есть в базе.")
    else:
        if ishelf in directories:
            idict = {}
            idict["type"] = itype
            idict["number"] = inum
            idict["name"] = iname
            documents.append(idict)
            directories[ishelf].append(inum)
            print(f"Документ с номером {inum} добавлен. Помещен на полку {ishelf}.")
        else:
            print(f'Нет полки с номером {ishelf}. Документ не добавлен.')


if __name__ == '__main__':

    print(LIST_COMMANDS)

    run = True
    while run:
        command = input('Введите команду: ')
        if command == 'q':
            run = False
        elif command == 'p':
            inum = input('Введите номер документа: ')
            people(inum)
        elif command == 's':
            inum = input('Введите номер документа: ')
            shelf(inum)
        elif command == 'l':
            list()
        elif command == 'a':
            add()
        else:
            print('Неизвестная команда')
