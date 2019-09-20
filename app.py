from flask import Flask, render_template
import requests

API_KEY = 'j82eDZBoi2iZa-DgbGtEZVBMyWBKfHGIu_k84c7OLcHPzSSCWepFE6AqBb8PNr0r'

app = Flask(__name__)


def get_lib_info(library_name):
    url = 'http://density.adicu.com/latest?auth_token={}'.format(API_KEY)
    library_name.replace("_"," ")
    library_name = library_name.capitalize()
    response = requests.get(url)
    data = response.json()['data']
    library_list = []
    for entry in data:
        if entry['building_name'] == library_name:
            library_list.append("{0} is {1}% full".format(entry['group_name'], entry['percent_full']))
    return library_list

@app.route('/', methods=['GET'])
def main():
    for entry in get_lib_info("butler"):
        print(entry)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
