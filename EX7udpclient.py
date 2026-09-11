import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
server_address = ("localhost", 7000)
url = input("Enter URL: ")
client.sendto(url.encode(), server_address)
print("URL packet sent over UDP.")
client.close()
