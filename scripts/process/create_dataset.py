"""Imports for scrapping and loading datasets"""
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from datasets import Dataset


def get_data(urls: List[str], wd) -> dict:
    """"""
    id_list = []
    title_list = []
    intro_list = []

    idx = 0
    for url in urls:
        wd.get(url)
        idx += 1
        title = (wd.find_element(By.XPATH, '//h1[@class="mb-1"]'))
        intro = (wd.find_element(By.XPATH, '//div[@class="block_1"]/p[1]'))
        print(f'Scrapped title: {title.text}')
        print(f'Scrapped intro: {intro.text[:100]}')
        id_list.append(idx)
        title_list.append(title.text)
        intro_list.append(intro.text)

    data_dict = {'id': id_list, 'url': urls, 'title': title_list, 'intro': intro_list}

    return data_dict


def split_dataset(ds: Dataset, percentage: float) -> dict:
    """Split a dataset into train, dev and set. Returns a dict of datasets"""
    train_dev_test = ds.train_test_split(test_size=percentage*2)
    train = train_dev_test['train']
    dev_test = train_dev_test['test'].train_test_split(test_size=0.5)
    dev = dev_test['train']
    test = dev_test['test']

    dict_train_dev_test = {'train': train, 'dev': dev, 'test': test}

    return dict_train_dev_test


def main(url_file, output_file, split, percentage):
    """"""
    with open(url_file, 'r') as file:
        urls = [url.strip() for url in file.readlines()]

    print('Initializing webdriver...')
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)

    print('Collecting data...')
    data_dict = get_data(urls, wd)
    print('Finished data collection.')

    ds = Dataset.from_dict(data_dict)

    if split is None:
        ds.to_parquet(f'{output_file}.parquet', compression='snappy')
        print(f'Dataset created at {output_file}.parquet')
    else:
        train_dev_test = split_dataset(ds, percentage)
        for split_name, dataset in train_dev_test.items():
            dataset.to_parquet(f'{output_file}_{split_name}.parquet', compression='snappy')
            print(f'{split_name.capitalize()} set created at {output_file}_{split_name}.parquet')


if __name__ == '__main__':
    """Configurate argument parser"""
    import argparse
    parser = argparse.ArgumentParser(description='Create a parquet from a file of urls.')
    parser.add_argument('url_file', help='Input txt file with one url per line.')
    parser.add_argument('output_file', help='Output file (without .parquet suffix).')
    parser.add_argument('-s', '--split', action='store_true', help='Split your dataset into train, dev and test.')
    parser.add_argument('-p', '--percentage', type=float, help='Size of each dev and test. Value between 0 and 0.5')
    args = parser.parse_args()

    if args.split:
        if not args.percentage:
            raise Exception('Split percentage required when -s option activated.')
        else:  # Check if split percentage is a valid value
            if args.percentage >= 0.5 or args.percentage < 0:
                raise ValueError('Split percentage must be between 0 and 0.5.')

    main(url_file=args.url_file,
         output_file=args.output_file,
         split=args.split,
         percentage=args.percentage)
