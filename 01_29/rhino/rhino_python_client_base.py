import socket
import time
import rhinoscriptsyntax as rs
import ast



def socket_client(socket_name):

    local_hostname = socket.gethostname()
    local_fqdn = socket.getfqdn()
    ip_address = socket.gethostbyname(local_hostname)

    server_address =(ip_address, 23456)
    sock.connect(server_address)
    print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))
    
    count = 0
    message_list = []
    rs.EnableRedraw(False)
    while True:
        try:
            new_data = str(count).encode("utf-8")
            sock.sendall(new_data)
            ret_msg = sock.recv(64)
            message = ast.literal_eval(ret_msg)
            message_list.append(message)
        except:
            break

    sock.close()
    
    print("done")
    return(message_list)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

points = socket_client(sock)
rs.AddPoints(points)