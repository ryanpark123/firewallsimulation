import socket

def simulate_firewall(host='localhost', port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Listening on {host}:{port}")

    # Define rules for blocking IPs and specific ports
    block_ips = ["192.168.1.10"]  # List of IPs to block
    block_ports = [8080]  # List of ports to block

    try:
        while True:
            client_socket, addr = server_socket.accept()
            client_ip, client_port = addr
            print(f"Received connection from {addr}")

            # Check if the IP or port should be blocked
            if client_ip in block_ips:
                print(f"Blocked IP {client_ip}")
                client_socket.close()
            elif client_port in block_ports:
                print(f"Blocked port {client_port}")
                client_socket.close()
            else:
                print(f"Allowed {addr}")
                # Here you could handle the client request if needed
                client_socket.close()
    except KeyboardInterrupt:
        print("Shutting down server...")
        server_socket.close()

if __name__ == "__main__":
    simulate_firewall()
