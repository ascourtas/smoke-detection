from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import shutil



url = "http://hpwren.ucsd.edu/HPWREN-FIgLib/HPWREN-FIgLib-Data/20191001_FIRE_bh-w-mobo-c/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))
    filename = link.get('href')
    if filename.split(".")[-1] not in ["mp4", "jpg", "jpeg"]:
        continue

    full_url = os.path.join(url, filename)

    # Open the url image, set stream to True, this will return the stream content.
    # code below borrowed from https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c
    r = requests.get(full_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Image Couldn\'t be retreived')
