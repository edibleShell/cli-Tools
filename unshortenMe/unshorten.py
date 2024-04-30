import requests
import json
from prettytable import PrettyTable


def unshorten(base_url, headers):
    res = requests.get(base_url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        table = PrettyTable()
        table.field_names = ['Unshortened_URL', 'Shortened_URL', 'Success']
        table.add_row([data.get('unshortened_url'), data.get('shortened_url'), data.get('success')])
        return table
    else:
        print('Request failed with status code:', res.status_code)


def main():
    headers = {
        'Authorization': 'Token <your_token>'
    }
    shorty = input('shortened URL: ')
    base_url = f'https://unshorten.me/api/v2/unshorten?url={shorty}'
    response = unshorten(base_url, headers)
    print(response)

if __name__ == "__main__":
    main()
