from faker import Faker
import random

fake = Faker('pt_BR')

# Funções
def generate_email(data_amount: int):
    for _ in range(data_amount):
        yield fake.email()

def generate_name(data_amount: int):
    for _ in range(data_amount):
        yield fake.name()

def generate_random_suffix():
    suffixes = ['@gmail.com', '@hotmail.com', '@outlook.com']
    return suffixes[random.randint(0,2)]

def generate_fake_data(data_amount: int):
    for name, email in zip(generate_name(data_amount), generate_email(data_amount)):
        name = name.replace('Srta. ', '').replace('Sr. ', '').replace('Sra. ', '').replace('Dr. ', '').replace('Dra. ', '')
        name = name.split(' ')
        name = name[0] + ' ' + name[-1]
        email = email.split('@')
        email = email[0] + generate_random_suffix()
        yield name, email


# MARK: - Main

if __name__ == '__main__':
    for name, email in generate_fake_data(10):
        print(name, email)
