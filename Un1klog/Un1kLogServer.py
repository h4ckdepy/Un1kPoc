import socketserver
import requests
import datetime
import os
import base64
import json



class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        ## 获取上次捕获流量时候的ip信息
        lasturl = open("record.txt", 'r')
        lasturl = lasturl.readline()
        ## 获取客户端的访问ip
        flag = (self.client_address[0])
        nowurl = open("record.txt", 'w')
        nowurl.write(flag) 
        nowurl.close()
        try:
            self.data = self.request.recv(1024)
            # print("{} send:".format(self.client_address), self.data)
            check = self.data.decode("utf-8")
            checkflag = "GETRECORD"
            if check == checkflag:
                record = open("recorddata.txt", 'r')
                l_str = json.dumps(record.readlines())
                l_bytes = l_str.encode('utf-8')
                self.request.sendall(base64.b64encode(l_bytes))
                print("[UN1KPOC] send data to clinet.")
            if check == "DELETERECORD":
                record = open("recorddata.txt", 'w')
                record.write("") 
                record.close()
                self.request.sendall("DeleteSuccess.".encode("utf-8"))
                print("[UN1KPOC] delete data.")
            if not self.data:
                print("connection lost")
        except Exception as e:
            check =""
        finally:
            if check == "GETRECORD":
                print("[-] GETRECORD DO NOOOOOOT Record.")
            elif check == "DELETERECORD":
                print("[-] DELETERECORD DO NOOOOOOT Record.")
            else:
                data = ("[+] "+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" {"+str(self.client_address)+"!}@")
                print("\033[0;32;40m"+data+"\033[0m")
                record = open("recorddata.txt", 'a')
                record.write(data) 
                record.close()
                self.request.close()


if __name__ == "__main__":
   
    print("=========================================")
    print("Un1kLog For Un1kPoc - Author:depy@rce.ink")
    print("=========================================")
    filename = './record.txt'
    filename2 = './recorddata.txt'
    if not os.path.exists(filename):
        os.system(r"touch {}".format(filename))#调用系统命令行来创建文件
        print(filename+" does not exist,just create!")
    if not os.path.exists(filename2):
        os.system(r"touch {}".format(filename2))#调用系统命令行来创建文件
        print(filename2+" does not exist,just create!")
    HOST, PORT = "0.0.0.0", 8878
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
