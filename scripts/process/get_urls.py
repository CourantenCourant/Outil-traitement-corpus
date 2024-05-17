"""This script uses selenium"""
from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def get_urls(current_page_url: str, wd) -> List[str]:
    """Get all articles' urls of a page"""
    print(f'Scrapping urls at {current_page_url}')
    wd.get(current_page_url)
    xpath = '//*[@id="main-content"]/section/section[position()=1 or position()=2]/ul/li/h3/a[contains(@href, "")]'
    articles = wd.find_elements(By.XPATH, xpath)
    url_list = []
    for article in articles:
        url = article.get_attribute('href')
        url_list.append(url)

    return url_list


def get_subclass_pages(current_page_url: str, wd) -> List[str]:
    """A recursive function that navigates through all pages of a subclass and get articles' urls"""
    url_list = get_urls(current_page_url, wd)

    # Try going to the next page
    try:
        next_page = wd.find_element(By.XPATH, '//*[@class="page-item active"]//following-sibling::li[1]/a')
        next_page_url = next_page.get_attribute('href')
        print(f'Navigating to next page {next_page_url}')
        url_list.extend(get_subclass_pages(next_page_url, wd))
    # If at the last page
    except NoSuchElementException:
        print("Reached the last page on this level.")
    # Catch any other error
    except Exception as e:
        print(f"An error occurred: {e}")

    return url_list


def navigate_classes(url: str, limit: int, wd) -> List[str]:
    """A recursive function that gets all the pages of a specific class"""
    wd.get(url)
    classes = wd.find_elements(By.XPATH, '//*[@id="main-content"]/section/section/div/a')

    if not classes:  # Basic case, where on a page of articles
        return get_subclass_pages(url, wd)

    # Where on a page of classes
    classes_url = []
    for cls in classes:
        cls_url = cls.get_attribute('href')
        classes_url.append(cls_url)
    url_list = get_urls(url, wd)  # In case where this class page also have articles
    count = len(url_list)
    for cls_url in classes_url:
        print(f'Navigating deeper into {cls_url}')
        url_list.extend(navigate_classes(cls_url, limit, wd))
        count += len(url_list)
        if count >= limit:
            break

    return url_list


def main(url, output_file, limit):
    """Get pages from a class page and store in into the output file"""
    print('Initializing webdriver...')
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)

    url_list = navigate_classes(url, limit, wd)
    wd.quit()
    print(f'Scrapping finished. Scrapped {len(url_list)} urls.')

    with open(output_file, 'w', encoding='UTF-8') as file:
        for url in url_list:
            file.write(url + '\n')
    print(f'Results saved to {output_file}.')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Get all pages\' url of a given class on Encyclopédie Universalis.')
    parser.add_argument('url', type=str, help='Url of the target class.')
    parser.add_argument('output_file', help='A txt file to store results.')
    parser.add_argument('-l', '--limit', type=int, default=1000, help='The number of urls. Default set to 1000.')

    args = parser.parse_args()

    main(url=args.url,
         output_file=args.output_file,
         limit=args.limit)
