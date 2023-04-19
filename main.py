import csv


def has_digit(s):
    return any(char.isdigit() for char in s)


data_files = ['main_general.csv', 'main_house.csv', 'main_location.csv', 'main_measurements.csv']

merge_file = "clean_merge.csv"

positive_valued_fields_indexes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]

limited_valued_fields_indexes = [13, 14]
grade_field_index = 9

valid_rows = []

with open(merge_file, mode='r') as file:
    csv_reader = csv.reader(file)
    line_count = 0
    flagged_values = 0
    for row in csv_reader:
        flagged = False
        if line_count == 0:
            line_count += 1
            valid_rows.append(row)
            continue

        for index in positive_valued_fields_indexes:
            val = float(row[index])
            if index == grade_field_index and (val > 13 or val < 0):
                print(f'Invalid value [limited] at line: {line_count} , id: {row[0]} , field index: {index} ,  value: {val}')
                flagged_values += 1
                flagged = True

            if val < 0:
                print(f'Invalid value [negative] at line: {line_count} , id: {row[0]} , field index: {index} ,  value: {val}')
                flagged_values += 1
                flagged = True

        for index in limited_valued_fields_indexes:
            val = float(row[index])
            if val < -180 or val > 180:
                print(f'Invalid value [limited] at line: {line_count + 1}, id: {row[0]} , field index: {index} , value: {val}')
                flagged = True
                flagged_values += 1

        if not flagged:
            valid_rows.append(row)
        line_count += 1

print(f"Total flagged values: {flagged_values}")

with open('clean_merge.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(valid_rows)
    print("Re-written valid rows")

