import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(("localhost", 7000))
url = input("Enter URL: ")
client.send(url.encode())
client.close()
print("URL sent via TCP.")
