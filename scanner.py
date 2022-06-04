from ast import If
from ipaddress import ip_address
import nmap
scanner = nmap.PortScanner()
print("Welcome, this is a simple nmap automation tool")
print("--------------------------------------------")
ip_addr = input("Enter the IP address to scan")
print("Entered IP is: ", ip_addr)
type(ip_addr)

resp = input(""" \n Enter the type of scan to run
                    1)SYN ACK Scan
                    2)UDP Scan
                    3)Comprehensive Scan \n""")    
print("You have selected: ", resp)                    

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state()) #know if online or offline
    print(scanner[ip_addr].all_protocols())

    # display open ports, with keys() method
    print("Open Ports are: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU') # U indicates UDP
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state()) #know if online or offline
    print(scanner[ip_addr].all_protocols())

    # display open ports, with keys() method
    print("Open Ports are: ", scanner[ip_addr]['udp'].keys())
