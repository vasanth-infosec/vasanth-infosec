from functions import net
from functions import passgy
from functions import payload
from functions import dos
print(" -----------------------------  ")
print("| 1) Network Scanner           |")
print("| 2) Payload Generator         |")
print("| 3) Strong Password Generator |")
print("| 4) Dos & DDos Attack         |")
print(" ------------------------------ ")
num = input("Enter the option : ")
match num:
    case "1":
        print(" ----------------- ")
        print("{ Network Scanner }")
        print(" ----------------  ")
        net.networkscanner()
    case "2":
        print(" ------------------- ")
        print("{ Payload Generator }")
        print(" ------------------- ")
        payload.payloadgenerater()
    case "3":
        print(" --------------------------- ")
        print("{ Strong PassWord Generator }")
        print(" --------------------------- ")
        passgy.passgen()
    case "4":
        print(" ------------------- ")
        print("{ Dos & DDos Attack }")
        print(" ------------------- ")
        dos.ddos()
    case _:
        print("Invaild Option")