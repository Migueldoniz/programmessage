import os
from crontab import CronTab
import datetime as dt
import subprocess as sp


cron = CronTab(tabfile='/etc/crontab', user=False)  # system users cron
cron = CronTab(user='moguel')
job = cron.new(command='python main.py')

arq = open("programa.txt")
linhas = arq.readlines()
arq.close()
os.remove("programa.txt")
for linha in linhas:
    linha=linha.split("|")
    dia,mes,ano=linha[0].split("/") 
    hour,min=linha[1].split(":")
    diaweek=dt.date(int(ano),int(mes),int(dia)).weekday()
    job.setall("{min} {hour} {dia} {mes} {diaweek}")
    with open('programa.txt', 'a') as fw:
                for line in linhas:
                    # we want to remove 5th line
                    if line == linha:
                        fw.write(line)
linhas.pop()


