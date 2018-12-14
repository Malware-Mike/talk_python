import requests
import shutil
import os


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    resp = requests.get(url, stream=True)
    return resp.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')

    # 'wb' means write binary
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
