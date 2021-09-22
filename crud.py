import csv
import timezones as tz


def load_file():
    fn = ['name', 'city', 'date']
    fp = './data/data-base-file.csv'
    data = []

    with open(fp, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=fn)#, delimiter='\t')

        for c in reader:
            data.append(c)

    return data


def save_on_file(data):
    fn = ['name', 'city', 'date']
    fp = './data/data-base-file.csv'

    with open(fp, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fn)

        #writer.writeheader()
        writer.writerows(data)


def show_on_screen(data):
    if not data:
        print("Empty file")

    print("uid \t NAME \t\t CITY \t\t\t DATE")
    for idx, d in enumerate(data):
        print(f"{idx}\t{d['name']}\t\t{d['city']}\t\t\t{d['date']}")
    

def create_person():
    person = {
        'name': get_field('Name'),
        'city': get_field('City'),
        'date': tz.get_timezone()}

    return person


def get_field(field):
    value = None

    while not value:
        value = input(f"Write the {field}: ")

    return value


def delete_person(data, d_person):
    if d_person == 'all':
        del data[:]
        data = []
        return data

    for idx, person in enumerate(data):
        if person['name'] == d_person:
            data.pop(idx)

    return data


def update_person(data):
    print("'q' to cancel.")
    val = get_field('Name')
    if val == 'q':
        return data

    for person in data:
        if person['name'] == val:
            aux = person.copy()
            field = input("write what to update name or city: ").lower()
            if field == 'name' or field == 'city':
                person[field] = input(f"New {field}: ")
                print(f"Old {field} is {aux['name']}")
                print(f"New {field} is {person['name']}")
                del aux
            else:
                print(f"{field} is not valid option.")

    return data

