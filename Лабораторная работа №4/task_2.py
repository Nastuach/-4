# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(separator1=",",separator2="\n") -> None:
    with open(INPUT_FILENAME) as f:
        reader=csv.DictReader(f,delimiter=separator1)  # TODO считать содержимое csv файла
        data = [row for row in reader]

    json_data = json.dumps(data, indent=4) # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json_data)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
