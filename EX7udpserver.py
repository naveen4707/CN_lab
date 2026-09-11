from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import socket, webbrowser, os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("localhost", 7000))
print("UDP Server waiting for URL packet...")
data, addr = s.recvfrom(1024)
url = data.decode().strip()
print(f"Received URL: {url} from {addr}")
soup = BeautifulSoup(urlopen(url), "html.parser")
for img in soup.find_all("img"):
    img_src = img.get("src")
    if img_src:
        img_url = urljoin(url, img_src)
        filename = os.path.basename(img_url)
        urlretrieve(img_url, filename) 
        img["src"] = filename 
with open("navport4.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

s.close()
print("Webpage and assets downloaded successfully.")
webbrowser.open("navport4.html")
