from bs4 import BeautifulSoup
import requests

URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


def get_citations_needed_count(URL):
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')


    p_elements = soup.find_all('p')
    all_p_text = ''

    for p in p_elements:
        a_element = p.find('a', title="Wikipedia:Citation needed")
        p_text = p.get_text().strip()
        if a_element:
            all_p_text = all_p_text + p_text + "\n\n"
    return all_p_text



if __name__ == "__main__":
    print(get_citations_needed_count(URL))
