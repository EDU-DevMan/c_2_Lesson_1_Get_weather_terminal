import requests


CITIES = ["Лондон", "Шереметьево", "Череповец"]


def main():
    payload = {"nMTq": "", 'lang': 'ru'}

    for city in CITIES:
        url_template = 'https://wttr.in/{}'
        url = url_template.format(city)
        response = requests.get(url, params=payload)
        print(response.text)


if __name__ == '__main__':
    main()
