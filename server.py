import socket
import ssl
import threading
import subprocess

HOST = '127.0.0.1'
PORT = 5000

def handle_client(conn, addr):
    print(f"[+] Connected: {addr}")

    try:
        while True:
            data = conn.recv(1024).decode()

            if not data:
                break

            print(f"[COMMAND from {addr}] {data}")

            try:
                # Execute command
                output = subprocess.getoutput(data)
            except Exception as e:
                output = str(e)

            # If no output, send something
            if not output:
                output = "[No output]"

            conn.sendall(output.encode())

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")

    finally:
        conn.close()
        print(f"[-] Disconnected: {addr}")


def main():
    # SSL setup
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    print(f"[LISTENING] Server running on {HOST}:{PORT}")

    # Wrap with SSL
    with context.wrap_socket(sock, server_side=True) as secure_sock:
        while True:
            conn, addr = secure_sock.accept()

            # Multi-client support using threading
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    main()
