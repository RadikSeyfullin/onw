from faker import Faker
import os, random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onw.settings.settings')
django.setup()

from user_manager.models import CustomUser

fake = Faker('ru_RU')

sex_list = ['man', 'woman']

def add_user():
    sex = random.choice(sex_list)
    if sex == 'man':
        l_f_name = fake.name_male().split(' ')
        first_name = l_f_name[0]
        last_name = l_f_name[1]
        birth_date = fake.date_object(end_datetime=None)
        email = fake.email()
        password = first_name + last_name + str(birth_date.year)
        city = fake.city()
        country = 'Россия'
        website_url = fake.uri()
        phone_number = fake.phone_number()
    else:
        l_f_name = fake.name_female().split(' ')
        first_name = l_f_name[0]
        last_name = l_f_name[1]
        birth_date = fake.date_object(end_datetime=None)
        email = fake.email()
        password = first_name + last_name + str(birth_date.year)
        city = fake.city()
        country = 'Россия'
        website_url = fake.uri()
        phone_number = fake.phone_number()
    new_user = CustomUser(email=email, password=password, first_name=first_name, last_name=last_name, city=city, country=country, phone_number=phone_number, sex=sex, website_url=website_url, birth_date=birth_date)
    new_user.save()
    return new_user

def start_script(N):
    for _ in range(N):
        add_user()

if __name__ == '__main__':
    print('Creating users...')
    start_script(3)
    print('Creation complete')
