import socket
import time
print("We're in tcp client...");

#the server name and port client wishes to access
server_name = '13.60.236.199'
server_port = 12000

#create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.settimeout(1)  # Timeout of 1 second for receiving data

#Set up a TCP connection with the server
#connection_socket will be assigned to this client on the server side
client_socket.connect((server_name, server_port))

total_rtt_time = 0
requests_number = 500

print("Begin RTT Calculation...");

for i in range(requests_number):
    # send an integer to TCP server, in this case i is the request/iteration number
    msg = str(i)

    start_time = time.time()

    #send the message to the TCP server
    client_socket.send(msg.encode())

    #return values from the server
    server_response = client_socket.recv(1024)

    end_time = time.time()

    # calculate the rtt, * 1000 to get in milisecs
    rtt = (end_time - start_time) * 1000 
    total_rtt_time += rtt
    #print(f"Total time so far: {total_rtt_time}")

print(f"Average RTT over {requests_number} communications is: {total_rtt_time / requests_number} ms.")

client_socket.close()