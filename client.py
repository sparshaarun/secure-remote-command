import socket
import ssl
import time

HOST = '127.0.0.1'
PORT = 5000

print("DEBUG: CLIENT FILE RUNNING")   # <-- MUST PRINT

def main():
    try:
        context = ssl._create_unverified_context()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        secure_sock = context.wrap_socket(sock, server_hostname=HOST)

        secure_sock.connect((HOST, PORT))
        print("[CONNECTED TO SERVER]")

        while True:
            command = input("Enter command (or 'exit'): ")

            if command.lower() == 'exit':
                break

            # START TIMER
            start = time.perf_counter()

            secure_sock.sendall(command.encode())
            result = secure_sock.recv(4096).decode()

            # END TIMER
            end = time.perf_counter()

            delay = (end - start) * 1000

            print("\n[OUTPUT]\n", result)
            print("DEBUG: PRINTING DELAY")   # <-- MUST PRINT
            print("[DELAY] {:.2f} ms\n".format(delay))

        secure_sock.close()

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":
    main()