from faker import Faker
import random

emailSuffix = ['@gmail.com', '@hotmail.com', '@outlook.com']
fake = Faker('pt_BR')

# Functions
def generateEmail(data_amount: int):
    # data_amount = int(sys.argv[1])
    for mail in range(0, data_amount):
        mail = fake.email()
        mail = mail.split('@')
        mail = mail[0] + emailSuffix[random.randint(0,2)]
        print(mail)
    return mail

def generateName(data_amount: int):
    for name in range(0, data_amount):
        name = fake.name()
        name = name.replace('Srta. ','')
        name = name.replace('Sr. ','')
        name = name.replace('Sra. ','')
        name = name.replace('Dr. ','')
        name = name.replace('Dra. ','')
        name = name.split(' ')
        name = name[0] + ' ' + name[-1]
        print(name)
    return name