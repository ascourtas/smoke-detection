from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import shutil



url = "http://hpwren.ucsd.edu/HPWREN-FIgLib/HPWREN-FIgLib-Data/20160604_FIRE_rm-n-mobo-c/"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))
    filename = link.get('href')
    if filename.split(".")[-1] not in ["jpg", "jpeg", "mp4"]:
        continue

    full_url = os.path.join(url, filename)

    # image = urllib.request.urlretrieve(full_path, filename + "tmp")
    # with open(image, "wb") as f:
    #     f.write(image)



    # Open the url image, set stream to True, this will return the stream content.
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