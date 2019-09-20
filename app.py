from flask import Flask, render_template
import requests

API_KEY = 'j82eDZBoi2iZa-DgbGtEZVBMyWBKfHGIu_k84c7OLcHPzSSCWepFE6AqBb8PNr0r'

app = Flask(__name__)


def get_lib_info():
    url = 'http://density.adicu.com/latest?auth_token={}'.format(API_KEY)
    response = requests.get(url)
    data = response.json()['data']
    return data


def get_lib_info_by_name(library_name):
    data = get_lib_info()
    library_name = library_name.replace("_", " ")
    library_name = library_name.title()
    print(library_name)
    library_list = []
    for entry in data:
        if entry['building_name'] == library_name:
            library_list.append("{0} is {1}% full".format(entry['group_name'], entry['percent_full']))
    return library_list


def get_least_crowded(num_libraries):
    data = get_lib_info()
    data = sorted(data, key=lambda i: i['percent_full'])
    print(data)
    library_list = []
    num_libraries = min(num_libraries, len(data))
    for i in range(0, num_libraries):
        library_list.append("{0} is {1}% full".format(data[i]['group_name'], data[i]['percent_full']))
    return library_list


@app.route('/information/<input>', methods=['GET'])
def main(input):
    try:
        num_libraries = int(input)
        libraries = get_least_crowded(num_libraries)
    except ValueError:
        libraries = get_lib_info_by_name(input)

    if len(libraries) == 0:
        libraries = ['{} Not Found'.format(input)]
    return render_template('libraries.html', libraries=libraries)


@app.route('/', methods=['GET'])
def main_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
