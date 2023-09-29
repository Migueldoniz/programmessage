import datetime as dt
import requests

arq = open("Dados.txt")
linhas = arq.readlines()
time = dt.datetime.now()
for linha in linhas:
    linha1 = linha.split("|")
    nomearq=str(time.day)+"/"+str(time.month)+"/"+str(time.year)+"|"+str(time.hour)+":"+str(time.minute)
    if linha.startswith(nomearq):
        print ("sim igual")
        cel = linha1[2]
        msg = linha1[3]
        req=requests.post("http://127.0.0.1:3000/sendmessage",{
             "telnumber":cel,
             "message":msg
        })
        print (f"Mensagem:'{msg}' para {cel} em {linha1[0]} {linha1[1]} ")
        with open('Dados.txt', 'w') as fw:
                for line in linhas:
                    # we want to remove 5th line
                    if line != linha:
                        fw.write(line)
    
    print("Deleted")
    
