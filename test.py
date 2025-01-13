import socket

def test_connection(host, port):
    try:
        print(f"Attempting to connect to {host} on port {port}...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Connection to {host}:{port} succeeded.")
    except Exception as e:
        print(f"Connection to {host}:{port} failed: {e}")

if __name__ == "__main__":
    # Test connection to the server
    test_connection('localhost', 8080)  # Expected to be blocked if using the same port as the server
    test_connection('localhost', 9999)  # Should be allowed as it's not a blocked port
