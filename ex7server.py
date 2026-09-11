from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import socket
import webbrowser
import os
s = socket.socket()
s.bind(("localhost", 7000))
s.listen(1)
print("Waiting for connection...")
c, addr = s.accept()
url = c.recv(1024).decode()
print("Received URL:", url)
soup = BeautifulSoup(urlopen(url), "html.parser")
if not os.path.exists("images"):
    os.makedirs("images")
for img in soup.find_all("img"):
    img_url = img.get("src")
    if img_url:
        full_img_url = urljoin(url, img_url)
        img_name = os.path.basename(full_img_url.split("?")[0])
        try:
            urlretrieve(full_img_url, f"images/{img_name}")
            img["src"] = f"images/{img_name}"
            print(f"Downloaded image: {img_name}")
        except:
            print(f"Failed to download image: {img_url}")
with open("navport.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
print("Done! Webpage and images downloaded.")
c.close()
s.close()
webbrowser.open("navport.html")
