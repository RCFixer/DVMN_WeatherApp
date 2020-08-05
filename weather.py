import requests


def get_weather(url):
    payload = {'nTqm':'', 'lang':'ru'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    urls = [
        'http://wttr.in/london',
        'http://wttr.in/sheremetyevo',
        'http://wttr.in/cherepovets'
    ]
    for url in urls:
        print(get_weather(url))


if __name__ == '__main__':
    main()
