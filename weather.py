import requests


def get_weather(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    urls = [
        'http://wttr.in/london?nTqm&lang=ru',
        'http://wttr.in/sheremetyevo?nTqm&lang=ru',
        'http://wttr.in/cherepovets?nTqm&lang=ru'
    ]
    for url in urls:
        print(get_weather(url))


if __name__ == '__main__':
    main()
