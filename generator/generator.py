import random

from data.data import Person
from faker import Faker

faker_eng = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_eng.first_name() + " " + faker_eng.last_name(),
        firstname=faker_eng.first_name(),
        lastname=faker_eng.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(1000, 9999),
        department=faker_eng.job(),
        email=faker_eng.email(),
        current_address=faker_eng.address(),
        permanent_address=faker_eng.address()
    )
