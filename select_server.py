# Example usage:
#
# python select_server.py 3490

import sys
import socket
import select

def run_server(port):
    # Make the server socket and bind it to the port
    server_socket = socket.socket()
    server_socket.bind(("", port))
    server_socket.listen()

    # The listener socket
    read_sockets = [server_socket]

    # Loop forever
    while True:
        # call select() and get the sockets that are ready to read
        ready_to_read, _, _ = select.select(read_sockets, [], [])

        # for each socket that is ready to read
        for s in ready_to_read:
            # if the socket is the listener socket, then accept the connection
            if s is server_socket:
                client_socket, _ = server_socket.accept()
                print_client_connection_info(client_socket)
                read_sockets.append(client_socket)
            # else it is a regular socket
            else:
                message = s.recv(4096)

                # If the message is empty, the client has disconnected
                if not message:
                    print_client_disconnection_info(s)
                    s.close()
                    read_sockets.remove(s)
                else:
                    print__length_of_message_and_raw_message(s, message)

def print_client_connection_info(client_socket):
    print(f"{client_socket.getpeername()}: connected")

def print_client_disconnection_info(client_socket):
    print(f"{client_socket.getpeername()}: disconnected")

def print__length_of_message_and_raw_message(client_socket, message):
    print(f"{client_socket.getpeername()}: {len(message)} bytes: {message}")

#--------------------------------#
# Do not modify below this line! #
#--------------------------------#

def usage():
    print("usage: select_server.py port", file=sys.stderr)

def main(argv):
    try:
        port = int(argv[1])
    except:
        usage()
        return 1

    run_server(port)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
