import requests
import re

def find_phone_numbers(page_content):
    phone_pattern = re.compile(r"8\d{10}")
    phone_numbers = re.findall(phone_pattern, page_content)
    return phone_numbers

def get_phone_numbers(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        phone_numbers = find_phone_numbers(page_content)
        return phone_numbers
    else:
        return None

url = "https://repetitors.info/about.php"
phone_numbers = get_phone_numbers(url)
phone_numbers1 = get_phone_numbers("https://hands.ru/company/about")


if phone_numbers:
    print("Найденные номера телефонов:")
    for number in phone_numbers:
        print(number)
else:
    print("Не удалось загрузить страницу.")

if phone_numbers1:
    print("Найденные номера телефонов:")
    for number in phone_numbers1:
        print(number)
else:
    print("Не удалось загрузить страницу.")