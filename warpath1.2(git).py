from click_module import *
import telepot
import os
from numpy import argmax
a,b,c,d,i = 0,0,0,0,0
droped = 0
restart_time = 120 # 단위 : 초
gquest = 0
gquest_cnt = 0
helpnum = 0
boomnum = 0
now = datetime.datetime.now().replace(microsecond = 0)
imgdict = {'자동이전' : "img/boomed.png"} # '연맹도움':'img/help.png', '새로고침':"img/refresh.png", '엑스이미지':'img/ximage.png'
imglist = ['img/or1.png','img/or2.png','img/or3.png']
        ############ telepot ##############        
token = "****************"
mc = "**********"
bot = telepot.Bot(token)
# bot.sendMessage(mc, "test") # 메시지 받는 양식
def sendphoto() : 
    photo_folder_path = 'C:/Users/ghgus/Pictures/Screenshots'
    pyautogui.hotkey('win', 'prtsc')
    time.sleep(1)
    photo_dir_list = []
    timelist = []
    for root, dirs, files in os.walk(photo_folder_path):
        pass
    for i in files:
        photo_dir_list.append(root +'/'+ i)
    for i in photo_dir_list:
        timelist.append(os.path.getctime(i))
    max_index = argmax(timelist)
    photo_path = photo_dir_list[max_index]    
    ph = open(photo_path,'rb')
    bot.sendPhoto(mc, ph)
    print(photo_path)
    
def handle(msg) : 
    txt = msg['text']
    if txt == '0'   :
        home = my_search("img/home.png", 1) 
        map_image = my_search("img/map.png", 1) 
        if home == 'searched' : 
            bot.sendMessage(mc, 'activating')  
        elif map_image == 'searched' :
            bot.sendMessage(mc, 'activating')
        else : 
            bot.sendMessage(mc, 'not activating')
            
    if txt == '1'   :
        droped = my_search("img/droped.png", 1) 
        refresh = my_search("img/refresh.png", 1)
        if refresh == 'searched' : 
            my_click("img/refresh.png", 1)
            bot.sendMessage(mc, '새로고침 완료')
            my_click("img/droped.png", 1)
            bot.sendMessage(mc, '재접속 완료')
        elif droped == 'searched' : 
            my_click("img/droped.png", 1)
            bot.sendMessage(mc, '재접속 완료')
        else :
            bot.sendMessage(mc, '이미지를 찾을수 없음')
            
    if txt == '사진'   :   
        sendphoto()
        
def play_imgdict() :
    global helpnum
    for idx, img in enumerate(imgdict):
        a = my_search(imgdict[img], 1)
        if a == 'searched':
            my_click(imgdict[img], 1)
            if idx == 0 :
                now = datetime.datetime.now().replace(microsecond = 0)
                helpnum += 1
                print(f'{img} {helpnum}건 완료 {now}')
            elif idx == 1 :
                now = datetime.datetime.now().replace(microsecond = 0)
                print(f'{img} {boomnum}건 완료 {now}')
                time.sleep(3)
                my_click("img/homebottom.png",1)
def clearing() :      
    lst = []
    for i in imglist:
        a = my_search(i,1)
        lst.append(a)
    if 'searched' in lst :
        my_click('img/dod.png',1)
        print('clearing 완료')
def gathering(x): 
    global i, d, c, b
    a = my_search("img/search1.png",1)
    if a == 'searched' : 
        my_click("img/search1.png",1)
        time.sleep(1)
        a = my_search("img/par1.png",1)
        if a == 'searched' : 
            my_click("img/par1.png",1)
            if x == "석유":
                my_click("img/choice3off.png",1)
            elif x == "강철":    
                my_click("img/choice2off.png",1)
            elif x == "군사비":       
                my_click("img/choice1off.png",1)
            my_click("img/gumsaek1.png",1)
            i += 1
            time.sleep(1)
            a = my_search("img/home.png",1)
            if a == 'searched' :
                my_Move_click("img/home.png", 1 , 590, -300)
                time.sleep(1)
                my_Move_click("img/home.png", 1 , 590, -200)
                time.sleep(1)
                my_Move_click("img/home.png", 1 , 590, -200)
                time.sleep(2)
                if x == "석유":
                    d += 1
                    now = datetime.datetime.now().replace(microsecond = 0)
                    # bot.sendMessage(mc, f"석유 채집요청 {d}건 완료 {now}")
                    print(f"석유 채집요청 {d}건 완료 {now}")
                elif x == "강철":    
                    c += 1
                    now = datetime.datetime.now().replace(microsecond = 0)
                    # bot.sendMessage(mc, f"강철 채집요청 {c}건 완료 {now}")
                    print(f"강철 채집요청 {c}건 완료 {now}")
                elif x == "군사비":     
                    b += 1
                    now = datetime.datetime.now().replace(microsecond = 0)
                    # bot.sendMessage(mc, f"군사비 채집요청 {b}건 완료 {now}")
                    print(f"군사비 채집요청 {b}건 완료 {now}")
 
    
print('start')
bot.message_loop(handle)
while True:
    # i = 0                 
    # while i == 0 : # oil
    #     clearing()
    #     play_imgdict()
    #     gathering("석유")
    # i = 0                     
    # while i == 0 :  # mine
    #     clearing()
    #     play_imgdict()
    #     gathering("강철")

    i = 0 
    while i == 0 : # money
        clearing()
        play_imgdict()
        gathering("군사비")




# pyautogui.mouseInfo()   



























