"""
1. Написать функцию email_parse(<email_address>),
которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен
из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?

"""
import re
address = input('Введите email: ')


def email_parse(address):
    parsed = re.findall(r'(^\w+)@((\w+)\.(\w{2,}))$', address)
    if not parsed:
        raise ValueError()
    return dict(zip(['username', 'domain'], parsed[0]))

try:
 print(email_parse(address))
except ValueError:
    print(f' {address} Данны e-mail введен не корректно ')