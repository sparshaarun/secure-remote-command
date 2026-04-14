# Secure Remote Command Execution System

## Project Overview

This project implements a secure client-server application that allows a client to remotely execute system commands on a server and receive the output. Communication between the client and server is encrypted using SSL/TLS to ensure data security.

The system is built using TCP socket programming and supports multiple concurrent clients.

---

## Objectives

* Implement communication using TCP sockets
* Secure data exchange using SSL/TLS
* Support multiple client connections
* Execute commands remotely on the server
* Measure network delay (Round Trip Time)

---

## System Architecture

```text
Client  →  SSL Encrypted TCP Connection  →  Server
        ←        Command Output         ←
```

---

## Features

* Secure communication using SSL/TLS
* Remote command execution
* Multi-client support using threading
* Delay measurement (Round Trip Time)
* Basic error handling

---

## Technologies Used

* Python
* Socket Programming
* SSL/TLS
* Threading

---

## Project Structure

```text
miniproj/
│
├── server.py
├── client.py
├── cert.pem
├── key.pem
├── README.md
```

---

## How to Run

### Step 1: Start the Server

```bash
python server.py
```

Expected output:

```text
[LISTENING] Server running on 127.0.0.1:5000
```

---

### Step 2: Run the Client (in a separate terminal)

```bash
python client.py
```

---

### Step 3: Execute Commands

Examples:

```text
whoami
dir
ipconfig
```

---

## Sample Output

```text
[CONNECTED TO SERVER]
Enter command: whoami

[OUTPUT]
user_name

[DELAY] 5.23 ms
```

---

## Performance Evaluation

* Delay is calculated on the client side
* Represents round trip time between sending request and receiving response
* Tested with multiple concurrent clients

---

## Limitations

* Uses self-signed SSL certificates
* No authentication mechanism implemented
* Designed primarily for local network testing

---

## Future Improvements

* Add user authentication
* Develop a graphical user interface
* Support file transfer between client and server
* Extend deployment to remote networks

---

## Summary

This project demonstrates secure communication using TCP sockets and SSL/TLS. The server handles multiple clients concurrently using threading, executes commands received from clients, and returns the output. The system also measures round trip delay for performance evaluation.

---

## Submission by Team 10

1.PES2UG24CS517
2.PES2UG24CS513
3.PES2UG24CS520

