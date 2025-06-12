# Ping Sweeper Tool

## Description
This Python tool scans a given subnet for active IP addresses by sending ICMP ping requests. It supports multithreaded scanning for faster results and saves the scan output in both `.txt` and `.csv` formats.

## How to use
1. Run the script:
   ```bash
   python pingsweeper.py

2. Enter the subnet you want to scan (e.g., 192.168.1.0/24).

    The tool will display which IP addresses are online or offline.

## Output files

After the scan completes, two output files are created in the same directory as the script:

    results.txt: A human-readable log of the scan results.

    results.csv: A CSV file containing IP addresses and their status (ONLINE or offline).

### Why two output files?

    The .txt file is easy to read and share.

    The .csv file is useful for data analysis, sorting, filtering, or opening in spreadsheet programs like Excel or Google Sheets.

### Example CSV content
IP Address	Status
192.168.1.1	ONLINE
192.168.1.2	offline
192.168.1.5	ONLINE
Notes

    The script uses multithreading to speed up scanning, but be mindful of network restrictions that might block too many simultaneous pings.

    The tool works cross-platform on Windows, macOS, and Linux.

## Feel free to customize or expand this README as your project grows!