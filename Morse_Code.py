import random
import time
import os

CBLUE = '\033[36m'
CRED = '\033[91m'
CWHITE = '\033[97m'
CEND = '\033[0m'
clear = lambda: os.system('clear')

final_list=[]
alphabet_sort_list = ['af4himi', 'alipiry', 'alirezaklhr', 'AlirezaMAhmadi', 'alixjeys', 'arianomrani', 'HaniehFazeli', 'irbughunters', 'M_Derakhshan79', 's4hm4d', 'SamEbison', 'vahid_mg', 'Xerxews', 'Xubuntu_ir', 'yoones11832151']
morse_sort_list = ['af4himi .- -... --- .-.. ..-. .- --.. .-..', 'alipiry .-.. . .- .-. -.', 'alirezaklhr .-- .... .- - / -.. --- . ... -. .----. - / -.- .. .-.. .-.. / -.-- --- ..- / -- .- -.- . ... / -.-- --- ..- / ... - .-. --- -. --. . .-.', 'AlirezaMAhmadi -.. .- -- .- ... .... --. .. .-.. .- -.', 'alixjeys .... . .-.. .-.. --- / ..-. .-. .. . -. -.. ...', 'arianomrani .. .----. -- / .- .-. .. .- -. .-.-.-', 'HaniehFazeli .. .-.. --- ...- . .- .-. -', 'irbughunters -... ..- --. / -... --- ..- -. - -.-- / .- / .-- .- -.-- / --- ..-. / .-.. .. ..-. .', 'M_Derakhshan79 -.....---.', 's4hm4d ... ....- .... -- ....- -..', 'SamEbison .-. -.-. .', 'vahid_mg - .... . .-. . / .. ... / -. --- / ... . -.-. ..- .-. .. - -.--', 'Xerxews -.- .... .- ... .... .- -.-- .- .-.', 'Xubuntu_ir -..- ..- -... ..- -. - ..-', 'yoones11832151 .. ....... .-.. --- ...- . ....... .. .-. .- -.']

clear()
print(CBLUE + "[STEP 1] Sort the list Alphabetically:" + CEND)
for i in range(len(morse_sort_list)): 
    print (i, end = "-") 
    print (CWHITE + morse_sort_list[i] + CEND) 

try:
    print(CBLUE + '[STEP 2] Start Generate Random list from Alphabet List:' + CEND)
    time.sleep(2.4)
    for i in range(len(alphabet_sort_list)):
        st = random.choice (alphabet_sort_list)
        final_list.append(st)
        print(CWHITE + str(i) + "-" + CEND + str(st) + CWHITE +' --> ' + CEND + 'added to list.' )
        alphabet_sort_list.remove(st)
        time.sleep(1.5)
    print(CBLUE + '[STEP 3] New Random List Generated:' + CEND)
    print(str(final_list))
    time.sleep(10)
except:
    print("An exception occurred in Generated list.")

try:
    for i in range(len(final_list)-1):
        clear()
        print(CBLUE + '[STEP 4]Remaining People on the list:' + CEND)
        print(str(final_list))
        st = random.choice (final_list)
        time.sleep(0.5*i)
        print(CRED + str(st) + ' --> OUT.'+ CEND)
        #print('\x1b[0;30;41m' + str(st) + ' --> OUT.'+ '\x1b[0m')
        time.sleep(2)
        final_list.remove(st)
    print('\x1b[6;30;42m' + str(final_list[0]) + ' Congratulations, you won ;)' + '\x1b[0m')
except:
    print("An exception occurred.")