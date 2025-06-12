import subprocess
import platform
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", str(ip)]

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout.lower()

        if "ttl=" in output:
            return f"[+] {ip} is ONLINE"
        else:
            return f"[-] {ip} is offline"
    except Exception as e:
        return f"[!] Error pinging {ip}: {e}"

def main():
    print("=== Ping Sweeper (Multithreaded) ===")
    subnet_input = input("Enter subnet (e.g. 192.168.1.0/24): ")

    try:
        network = ipaddress.ip_network(subnet_input, strict=False)
    except ValueError:
        print("[!] Invalid subnet format.")
        return

    ip_list = list(network.hosts())
    print(f"\n[🔍] Scanning {len(ip_list)} IP addresses...\n")

    results = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(ping_host, ip): ip for ip in ip_list}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(result)

    print("\n[✔️] Scan complete.")

    # 🔢 Sort results based on IP address
    def extract_ip(line):
        return ipaddress.ip_address(line.split()[1])

    results.sort(key=extract_ip)

    # 💾 Save to file
    with open("results.txt", "w") as f:
        for line in results:
            f.write(line + "\n")

    print("[💾] Results saved to results.txt")

        # 📄 Save as CSV
    import csv

    with open("results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Status"])  # header

        for line in results:
            parts = line.split()
            ip = parts[1]
            status = "ONLINE" if "ONLINE" in line else "offline"
            writer.writerow([ip, status])

    print("[📄] Results also saved to results.csv")




if __name__ == "__main__":
    main()
