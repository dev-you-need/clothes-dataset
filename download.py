import pandas as pd
from tqdm import tqdm
import os
import requests
import multiprocessing

path_to = 'imgs'


def download_image(pair):
    row = pair[1] #way to skip index of iterator
    path_to_id = os.path.join(os.path.join(path_to, str(row.id)))
    path_to_color = os.path.join(path_to_id, row.color)
    path_to_source = os.path.join(path_to_color, row.source)

    if not os.path.isdir(path_to_id):
        os.makedirs(path_to_id, exist_ok=True)
    if not os.path.isdir(path_to_color):
        os.makedirs(path_to_color, exist_ok=True)
    if not os.path.isdir(path_to_source):
        os.makedirs(path_to_source, exist_ok=True)

    filename = row.url.split('/')[-1]
    if not os.path.isfile(os.path.join(path_to_source, filename)):
        try:
            r = requests.get(row.url)
            if r.status_code == 200:
                with open(os.path.join(path_to_source, filename), 'wb') as f:
                    f.write(r.content)
        except requests.RequestException:
            print('Something wrong with with url {}'.format(row.url))


def loader():
    if not os.path.isdir(path_to):
        os.makedirs(path_to, exist_ok=True)
    df = pd.read_csv("clothes-dataset.csv")
    pool = multiprocessing.Pool(processes=8)
    iterator = pool.imap_unordered(download_image, df.iterrows())

    # start download. It looks weird, but it works.
    for _ in tqdm(iterator, total=len(df)):
        pass

    pool.close()
    pool.terminate()


if __name__ == '__main__':
    loader()
