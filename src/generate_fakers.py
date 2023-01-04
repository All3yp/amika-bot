from faker import Faker
import random

fake = Faker('pt_BR')

# Funções

def generate_name(data_amount: int):
    for _ in range(data_amount):
        yield fake.name()

def generate_email_from(name: str):
    username = name.replace(' ', generate_random_spacer())
    email = username + generate_random_suffix()
    return formatUnicode(email).lower()

def generate_random_spacer():
    suffixes = ['.', '_', str(random.randint(1,99)), '']
    random.shuffle(suffixes)
    return suffixes.pop()

def generate_random_suffix():
    suffixes = ['@gmail.com', '@hotmail.com', '@outlook.com']
    return suffixes[random.randint(0,2)]

def formatUnicode(email: str):
    email = email.replace('ã', 'a')
    email = email.replace('á', 'a')
    email = email.replace('à', 'a')
    email = email.replace('â', 'a')
    email = email.replace('é', 'e')
    email = email.replace('ê', 'e')
    email = email.replace('í', 'i')
    email = email.replace('ó', 'o')
    email = email.replace('õ', 'o')
    email = email.replace('ú', 'u')
    email = email.replace('ç', 'c')
    return email

def generate_fake_data(data_amount: int):
    for name in generate_name(data_amount):
        name = name.replace('Srta. ', '').replace('Sr. ', '').replace('Sra. ', '').replace('Dr. ', '').replace('Dra. ', '')
        name = name.split(' ')
        name = name[0] + ' ' + name[-1]
        email = generate_email_from(name)
        yield name, email

# MARK: - Main

if __name__ == '__main__':
    for name, email in generate_fake_data(10):
        print(name, email)
