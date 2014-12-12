import csv


db = {
}


with open('db.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        db[row['TAC']] = row


def associate_data(db, tac):
    return db.get(tac, None)


def requires_data(data):
    if data['model']:
        return False

    return True


all_result = []


with open('numbers.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:

        if not requires_data(row):
            continue

        result = associate_data(db, row['TAC'])

        all_result.append({'raw_data': row, 'phone_data': result})

        if result:
            print(result)


print({'result': all_result})
