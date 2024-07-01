import socket
import time

# Define the target host and ports for port knocking
host = ''
ports = [2201, 2211, 2234]
knock_sequence = [(host, port) for port in ports]

# Define the port to be opened after successful port knocking
service_port = 12345

# Define timeout for port knocking sequence
timeout = 15  # seconds

def knock_ports():
    for target_host, port in knock_sequence:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set timeout for connection attempt
            s.settimeout(timeout)
            # Connect to the target host and port
            s.connect((target_host, port))
            print(f"Knocked on port {port}")
            # Close the socket
            s.close()
        except socket.error as e:
            print(f"Failed to knock on port {port}: {e}")
            # If one of the ports fails, stop knocking
            return False
    return True

def open_service_port():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set timeout for connection attempt
        s.settimeout(timeout)
        # Connect to the target host and port
        s.connect((host, service_port))
        print(f"Port {service_port} opened successfully")
        # Close the socket
        s.close()
    except socket.error as e:
        print(f"Failed to open port {service_port}: {e}")

if __name__ == "__main__":
    if knock_ports():
        open_service_port()
    else:
        print("Port knocking sequence failed")



