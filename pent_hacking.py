#pip install progress

import time
from progress.bar import ChargingBar

print("Запущен процесс взлома Пентагона...")

print(" ")
time.sleep(2)
for i in range(1,11):
    mylist = [1,2,3,4,5,6,7,8,9,10,11]
    bar = ChargingBar ('Hacking...', max = len(mylist))
    for h in mylist:
        bar.next()
        time.sleep(0.1)
        
    print(" ВЗЛОМ. Процесс - {}%".format(i*10))
    time.sleep(0.1)

print(' ')

print("Пентагон успешно взломан.")

print(' ')

time.sleep(0.3)

print("ЗАВЕРШЕНИЕ.")

print(' ')

print('Закроется через 5 секунд')

end_list = ["END",1,2,3,4]

for e in reversed(end_list):
    time.sleep(1)
    print(f"{e}...")
