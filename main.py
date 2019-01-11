import csv

DATA_FILE = '.archivo.csv'
DATA_SCHEMA = ['rut', 'codBen', 'typePro', 'codPro', 'incExc', 'dateIni', 'dateTer']
# DATA_SCHEMA = ['name', 'rut', 'address']
DELIMITER = ';'

_lines = []


def _load_data_from_file():
    with open(DATA_FILE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=DATA_SCHEMA, delimiter=DELIMITER, skipinitialspace=True)

        for row in reader:
            _lines.append(row)

    print()


def _print_header():
    rutTitle = 'RUT'
    codTitle = 'PRODUCTO'
    dateTitle = 'FECHA'

    print('-' * 50)
    print(f'{rutTitle:20} | {codTitle:20} | {dateTitle:20}')
    print('-' * 50)


def _show_data():
    #_print_header()

    for idx, line in enumerate(_lines):
        rut=line['rut']
        cod=line['codPro']
        date=line['dateIni']

        print(f'{rut:20} | {cod:20} | {date:20}')


if __name__ == '__main__':
    _load_data_from_file()
    _show_data()
