import socket

def is_port_open(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))

        if result == 0:
            return True
        else:
            return False
    except socket.error as e:
        print(f"Error: {e}")
        return False
    finally:
        sock.close()

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5000
    if is_port_open(host, port):
        print(f"Port {port} is open on {host}")
    else:
        print(f"Port {port} is closed on {host}")
