import requests


def get_info(url, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    payload = {'nTqm': '', 'lang': 'ru'}
    places = ['london', 'sheremetyevo', 'cherepovets']
    for place in places:
        print(get_info('http://wttr.in/' + place, payload))


if __name__ == '__main__':
    main()
