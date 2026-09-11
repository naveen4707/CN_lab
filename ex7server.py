from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import socket, webbrowser, os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 7000))
s.listen(1)
print("TCP Server waiting for client...")
c, addr = s.accept()
url = c.recv(1024).decode().strip()
soup = BeautifulSoup(urlopen(url), "html.parser")
for img in soup.find_all("img"):
    img_src = img.get("src")
    if img_src:
        img_url = urljoin(url, img_src)
        filename = os.path.basename(img_url)
        urlretrieve(img_url, filename) 
        img["src"] = filename          
with open("navport.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

c.close()
s.close()
print("Success! Webpage downloaded.")
webbrowser.open("navport.html")
