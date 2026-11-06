
import ipaddress
import socket
import subprocess
import errno


# ==========================================
# NETWORK RECONNAISSANCE TOOLKIT
# ==========================================

def display_banner():
    print("===================================")
    print("   Network Reconnaissance Toolkit  ")
    print("===================================")
    print("Welcome to your network reconnaissance tool!")


# ==========================================
# 1. TARGET VALIDATION
# ==========================================

def validate_target(target):
    try:
        ipaddress.ip_address(target)
        return True

    except ValueError:
        try:
            socket.gethostbyname(target)
            return True

        except socket.gaierror:
            return False


# ==========================================
# 2. NETWORK CALCULATION
# ==========================================

def get_network(ip, subnet):
    network = ipaddress.ip_network(
        f"{ip}/{subnet}",
        strict=False
    )
    return network


# ==========================================
# 3. HOST DISCOVERY
# ==========================================

def is_host_alive(ip):

    result = subprocess.run(
        ["ping", "-c", "1", "-W", "1", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print(f"Host {ip} is alive")
        return True

    else:
        print(f"Host {ip} is not responding")
        return False


def discover_hosts(network):

    for ip in network.hosts():

        if is_host_alive(ip):
            print(f"Discovered host: {ip}")


# ==========================================
# 4. TCP PORT SCANNING
# ==========================================

def scan_ports(target, port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:

        scanner.settimeout(1)
        result = scanner.connect_ex((target, port))

    if result == 0:
        status = "open"

    elif result == errno.ECONNREFUSED:
        status = "closed"

    elif result == errno.ETIMEDOUT:
        status = "filtered/unknown"

    else:
        status = "unknown"

    error_name = (
        "SUCCESS" if result == 0
        else errno.errorcode.get(result, "UNKNOWN_ERROR")
    )

    print(
        f"Port {port}: "
        f"Error code = {result}, "
        f"Error name = {error_name}"
    )

    return {
        "port": port,
        "status": status
    }


# ==========================================
# SUMMARIZE RESULT
# ========================================== 

def summarize_result(result):
    open_count = closed_count = filtered_count = unknown_count = 0

    for port_result in result:
        status = port_result.get("status")

        if status == "open":
            open_count += 1
        elif status == "closed":
            closed_count += 1
        elif status == "filtered/unknown":
            filtered_count += 1
        else:
            unknown_count += 1

    print("===================================")
    print("           SCAN SUMMARY")
    print("===================================")
    print(f"Open ports: {open_count}")
    print(f"Closed ports: {closed_count}")
    print(f"Filtered/unknown ports: {filtered_count}")
    print(f"Unknown ports: {unknown_count}")
    print("-----------------------------------")
    print(f"Total ports scanned: {len(result)}")
    print("===================================")

 
# ==========================================
# 5. MAIN PROGRAM
# ==========================================

def main():

    display_banner()

    target = input("\nPlease enter the target IP address: ").strip()

    if not validate_target(target):
        print(f"Invalid input: {target}")
        return

    print(f"\nValid target: {target}")

    ports = [22, 53, 80, 443, 3306, 465, 143, 69, 23, 25, 8080]

    print("\nStarting TCP port scan...\n")

    scan_result = []
    for port in ports:
        result = scan_ports(target, port)
        scan_result.append(result) 
       


    summarize_result(scan_result)





# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()



