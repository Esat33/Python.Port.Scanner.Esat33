import socket
import pyfiglet
import  os
import  platform



def main():
 count ="1"
 ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
 print(ascii_banner)

 print("Enter the IP address you want to scan (IPv4 only): ")
 ipv4 = input()
 target = socket.gethostbyname(ipv4)
 if platform.system() == "Windows":
  os.system("ping -n "+count+ipv4)
 if  platform.system() == "Linux":
  os.system("ping -c "+count+ipv4)
 else :
  print("İnvalid İp")

 for port in range(1, 65535):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.75)
  result = s.connect_ex((target, port))

  if result == 0:
   print(f"Port {port} is open ")
   s.close()



if __name__ == "__main__":
 main()


