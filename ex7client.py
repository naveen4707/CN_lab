import socket
client = socket.socket()
client.connect(("localhost", 7000))
url = input("Enter webpage URL: ")
client.send(url.encode())
print("URL sent successfully.")
client.close()
