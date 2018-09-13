# -*- coding:utf-8 -*-

import argparse


def main():
    parser = argparse.ArgumentParser(description="Découpe CSV")
    parser.add_argument('--fichier', dest='csv_file', action='store',
                        required=True,
                        help='Fichier CSV à découper')
    parser.add_argument(
        '--lignes', dest='line_number', action='store',
        type=int, default=900000,
        help='Nombre de lignes dans les fichiers de sortie (default: 900 000)')
    options = parser.parse_args()

    out_line_number = 0
    out_file_number = 1
    with open(options.csv_file) as file_in:
        for line in file_in:
            with open('out' + str(out_file_number) + '.csv', 'a') as file_out:
                file_out.write(line)
            if out_line_number < options.line_number:
                out_line_number += 1
            else:
                out_line_number = 0
                out_file_number += 1


if __name__ == '__main__':
    main()
