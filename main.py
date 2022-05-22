import requests
from bs4 import BeautifulSoup


def main(policy_id):
    cardano_scan = 'https://cardanoscan.io/tokenPolicy/'
    try:
        page = requests.get(cardano_scan + policy_id)
        if page.status_code != 200:
            raise ConnectionError('Status code isn\'t 200')
        else:
            soup = BeautifulSoup(page.text, 'lxml')
            minted = soup.find('span', class_='h6 text-primary font-weight-bold')
            print(minted.text)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main('1e179fa84cb7bbf6061fbc8ee404bbbb04a297dfb46382a4f7e43dff')
