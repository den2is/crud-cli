from datetime import datetime
import pytz

def get_timezone():
    cities = {'Africa':['Johannesburg','Cairo'],
              'America':['Los_Angeles','Tijuana','Creston','Vancouver','Costa_Rica'],
              'Asia':['Taipei','Tokyo','Seoul'],
              'Australia':['Sydney'],
              'Europe':['Berlin','London','Paris']}
    print("Availables Time zones.")
    print(cities)

    c = input("City: ").capitalize()
    
    print(cities.keys())
    print(cities.values())
    if c in cities['America']:
        for i in cities.values():
            for j in i:
                if j == c:
                    country_tz = pytz.timezone(f"America/{j}")
    if c in cities['Africa']:
        for i in cities.values():
            for j in i:
                if j == c:
                    country_tz = pytz.timezone(f"Africa/{j}")
    if c in cities['Asia']:
        for i in cities.values():
            for j in i:
                if j == c:
                    country_tz = pytz.timezone(f"Asia/{j}")
    if c in cities['Australia']:
        for i in cities.values():
            for j in i:
                if j == c:
                    country_tz = pytz.timezone(f"Australia/{j}")
    if c in cities['Europe']:
        for i in cities.values():
            for j in i:
                if j == c:
                    country_tz = pytz.timezone(f"Europe/{j}")
    country_date =datetime.now(country_tz)
    formated = country_date.strftime("%d/%m/%Y, %H:%M:%S")

    return formated


#get_timezone()
