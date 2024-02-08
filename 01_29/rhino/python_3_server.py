#source: https://stackabuse.com/basic-socket-programming-in-python/
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
ip_address = socket.gethostbyname(local_hostname)


def cubic_grid(x_num, y_num, z_num, space):
    points = []
    for i in range(0, x_num * space , space):
        for j in range(0, y_num * space, space):
            for p in range(0, z_num * space, space):
                x = i
                y = j
                z = p
                point = (x, y, z)
                points.append(point)
    return points


def socket_server(socket, local_hostname, local_fqdn, ip_address, message_list):

    print ("working on %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

    server_address  =  (ip_address, 23456)
    print ('starting up on %s port %s' % server_address)
    sock.bind(server_address)

    sock.listen(1)

    while True:
        print('waiting..')
        connection, client_address = sock.accept()

        try:
            print('connection from', client_address)
     
            for message in message_list:
                data = connection.recv(64)
                return_msg = str(message).encode("utf-8")
                connection.sendall(return_msg)
        finally:
            connection.close()
def main():          

    grid_list = cubic_grid(10, 10, 10, 10)             
    socket_server(socket, local_hostname, local_fqdn, ip_address, grid_list)
    

main()

    
    