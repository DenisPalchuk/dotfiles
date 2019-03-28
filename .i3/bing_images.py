import requests
import json
import os


def main():
    response = requests.get(
        'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US')
    data = json.loads(response.text)
    url_to_image = data["images"][0]['url']
    file_path = download_file("http://bing.com" + url_to_image)
    os.system("feh --bg-scale " + file_path)
0


def download_file(url):
    # NOTE the stream=True parameter
    response = requests.get(url, stream=True)
    file_system_path = os.path.dirname(
        os.path.realpath(__file__)) + "/current_image_python.jpg"
    with open(file_system_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                file.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    return file_system_path
if __name__ == "__main__":
    main()
