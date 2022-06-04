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

