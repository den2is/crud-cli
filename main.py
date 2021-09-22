import os
import crud


def run():
    data = crud.load_file()

    try:
        os.system('clear')
        while True:
            print("""
                  CRUD
                  [C]reate.
                  [R]ead.
                  [U]pdate.
                  [D]elete.\n
                  [Q]uit or [ctrl]+C\n""")

            choice = input("\tEnter an option. ").lower()

            if choice == 'c':
                print("\tCreate a contact.")
                person = crud.create_person()
                data.append(person)
                os.system('clear')

            if choice == 'r':
                os.system('clear')
                crud.show_on_screen(data)

            if choice == 'u':
                print("\tUpdating contact.")
                data = crud.update_person(data)

            if choice == 'd':
                print("\tDelet a contact")
                print("\tTo delete all, write 'all'.")
                to_del = input("\tPerson's name: ").lower()
                data = crud.delete_person(data, to_del)
                continue
            if choice == 'q':
                raise KeyboardInterrupt

    except KeyboardInterrupt as ki:
        crud.save_on_file(data)
        print(ki)
        print("\tSee you later.")


if __name__ == '__main__':
    run()
