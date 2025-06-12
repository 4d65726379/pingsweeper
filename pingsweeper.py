import subprocess
import platform
import ipaddress

def ping_host(ip):
    # Detect the OS and build the correct ping command
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]

    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"[+] {ip} is ONLINE")
    except Exception as e:
        print(f"[!] Error pinging {ip}: {e}")

def main():
    print("=== Ping Sweeper ===")
    subnet_input = input("Enter subnet (e.g. 192.168.1.0/24): ")

    try:
        network = ipaddress.ip_network(subnet_input, strict=False)
    except ValueError:
        print("[!] Invalid subnet format.")
        return

    print(f"\n[🔍] Scanning {network.num_addresses} IP addresses...\n")

    for ip in network.hosts():
        ping_host(ip)

    print("\n[✔️] Scan complete.")

if __name__ == "__main__":
    main()
