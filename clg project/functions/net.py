import subprocess
def networkscanner():
    ip = input("Enter the Victim Ip Address or Domain Name : ")
    print("1) Scan for OS Dection ")
    print("2) Scan for Remote Operating Systems ")
    print("3) Scan for Open Ports on the Target ")
    print("4) Scan All Ports on a Target ")
    print("5) Run All Vulnerability Scans on the Target")
    option = input("Enter the Option : ")
    match option:
        case "1":
            subprocess.run(["nmap","-T4","-A",ip])
        case "2":
            subprocess.run(["nmap","-T4","-O",ip])
        case "3":
             subprocess.run(["nmap","-T4","--open",ip])
        case "4":
             subprocess.run(["nmap","-T4","-p-",ip])
        case "5":
             subprocess.run(["nmap","-T4","--script","vuln",ip])
        case _:
             print("Invaild Option")
