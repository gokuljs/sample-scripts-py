import os
import requests
from bs4 import BeautifulSoup


def download_all_images_from_url(url, save_path='images'):
    # Ensure the 'images' directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        img_url = img_tag.get('src')

        # Ensure the URL is absolute
        if not img_url.startswith(('data:image', 'http', 'https')):
            img_url = url + img_url

        try:
            img_data = requests.get(img_url).content
            with open(os.path.join(save_path, os.path.basename(img_url)), 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded {img_url}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {img_url} - {e}")


if __name__ == "__main__":
    url = input("Enter the URL to scrape images from: ")
    download_all_images_from_url(url)
