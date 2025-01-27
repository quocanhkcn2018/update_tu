import os
import datetime
from time import sleep, time
import pyautogui
import psutil
import cv2
import numpy as np
import array as arr
import random
import sys
import ctypes
import threading
import tkinter as tk
import requests
import json

def print_debug(data):
    global label_debug
    label_debug.config(text=f"{data}\n")
def is_screen_black():

    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

# Kiểm tra xem tất cả các pixel có phải là màu đen không
    if cv2.countNonZero(screenshot) == 0:
        print_debug("Màn hình đang bị đen toàn bộ.")
        return True
    else:
        return False

  # Trả về True nếu giá trị trung bình gần bằng 0 (màu đen)
def update_version(file_path, new_version):
  """
  Hàm cập nhật phiên bản trong file JSON.

  Args:
    file_path: Đường dẫn đến file JSON.
    new_version: Phiên bản mới cần cập nhật.
  """

  # Đọc dữ liệu từ file JSON
  with open(file_path, 'r') as f:
    data = json.load(f)

  # Cập nhật giá trị của key "version"
  data["version"] = new_version

  # Ghi dữ liệu đã cập nhật vào file
  with open(file_path, 'w') as f:
    json.dump(data, f, indent=4)
# Hàm để đảo lộn thứ tự các phần tử trong mảng
def check_for_updates():
    # URL đến file JSON chứa thông tin phiên bản mới nhất
    url = "https://github.com/quocanhkcn2018/update_tu/raw/main/version.json"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP status codes
        data = response.json()
        latest_version = data['version']
        latest_download_url = data['download_url']

        # Lấy phiên bản hiện tại (bạn có thể lưu trữ trong một file cấu hình)
        current_version = 1  # Ví dụ
        print("last version " + str(latest_version))
        if int(latest_version) > int(current_version):
            print_debug("Đang tải về tool........................")
            # Tải file về
            response = requests.get(latest_download_url)
            with open("new_version.zip", "wb") as f:
                f.write(response.content)

            # # Giải nén và cài đặt (phần này tùy thuộc vào cấu trúc của phần mềm)
            # # ...

            # # Cập nhật phiên bản hiện tại
            # with open("version.txt", "w") as f:
            #     f.write(latest_version)

            print_debug("ĐÃ TẢI XONG, VUI LÒNG \n TẮT TOOL \n GIẢI NÉN FILE, GHI ĐÈ \n new_version.zip")
        else:
            print_debug("Bạn đang sử dụng phiên bản mới nhất.")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi kiểm tra cập nhật: {e}")
def shuffle_array(array):
# Duyệt qua các phần tử trong mảng
    for i in range(len(array)):
# Chọn một vị trí ngẫu nhiên trong mảng
        j = random.randint(0, len(array) - 1)
# Hoán đổi giá trị của hai phần tử
        array[i], array[j] = array[j], array[i]
# Trả về mảng đã đảo lộn
    return array
# Hàm để lưu mảng vào file text
def save_array(array, filename):
# Mở file text ở chế độ ghi
    with open(filename, "w") as f:
# Duyệt qua các phần tử trong mảng
        for element in array:
# Ghi phần tử vào file text, cách nhau bởi dấu phẩy
            f.write(str(element) + ",")
# Đóng file text
        f.close()
# Hàm để đọc mảng từ file text
def load_array(filename):
    try:
# Mở file text ở chế độ đọc
        file = open(filename, "r")
# Đọc nội dung file text
        content = file.read()
# Tách nội dung file text thành một list các chuỗi, cắt bởi dấu phẩy
        string_list = content.split(",")
# Tạo một mảng rỗng
        array = arr.array('i', [])
# Duyệt qua các chuỗi trong list
        for string in string_list:
# Nếu chuỗi không rỗng
            if string != "":
# Chuyển chuỗi thành số nguyên và thêm vào mảng
                array.append(int(string))
# Đóng file text
        file.close()
        if len(array)==0:
            numbers1 = arr.array('i', range(11))
            save_array(numbers1,filename)
            return numbers1
# Trả về mảng đã đọc
        return array
    except FileNotFoundError:
        
        return numbers1



def checkacctime():
    try:
# Mở tệp index.txt ở chế độ đọc
        with open("index.txt", "r") as f:
# Đọc số trong tệp
            number = int(f.read())
# In số ra màn hình
            print_debug("Số trong tệp index.txt là:"+ str(number))
            f.close()
            return number
    except FileNotFoundError:
        with open("index.txt", "w") as f:
# Ghi số 1 vào tệp
            f.write("0")
            f.close()
            return 0
def checkacctime1():
    now = datetime.datetime.now()
    start1 = datetime.datetime(now.year, now.month, now.day, 0, 0, 0) # 0h00
    end1 = datetime.datetime(now.year, now.month, now.day, 2, 10, 0) # 1h30
    if start1 <= now <= end1:
        return 0
    start2 = datetime.datetime(now.year, now.month, now.day, 2, 10, 0) # 0h00
    end2 = datetime.datetime(now.year, now.month, now.day, 4, 20, 0) # 1h30
    if start2 <= now <= end2:
        return 1
    start = datetime.datetime(now.year, now.month, now.day, 4, 20, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 6, 30, 0) # 1h30
    if start <= now <= end:
        return 2
    start = datetime.datetime(now.year, now.month, now.day, 6, 30, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 8, 40, 0) # 1h30
    if start <= now <= end:
        return 3
    start = datetime.datetime(now.year, now.month, now.day, 8, 40, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 10, 50, 0) # 1h30
    if start <= now <= end:
        return 4
    start = datetime.datetime(now.year, now.month, now.day, 10, 50, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 13, 0, 0) # 1h30
    if start <= now <= end:
        return 5
    start = datetime.datetime(now.year, now.month, now.day, 13, 0, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 15, 10, 0) # 1h30
    if start <= now <= end:
        return 6
    start = datetime.datetime(now.year, now.month, now.day, 15, 10, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 17, 20, 0) # 1h30
    if start <= now <= end:
        return 7
    start = datetime.datetime(now.year, now.month, now.day, 17, 20, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 19, 30, 0) # 1h30
    if start <= now <= end:
        return 8
    start = datetime.datetime(now.year, now.month, now.day, 19, 30, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 21, 40, 0) # 1h30
    if start <= now <= end:
        return 9
    start = datetime.datetime(now.year, now.month, now.day, 21, 40, 0) # 0h00
    end = datetime.datetime(now.year, now.month, now.day, 23, 59, 0) # 1h30
    if start <= now <= end:
        return 10
    return -1


def closefo4():
    os.system ("taskkill /im fczf.exe")
    os.system ("taskkill /im fclauncher.exe")
    os.system ("taskkill /f /im garena.exe")   
    os.system ("taskkill /f /im xm.exe")   
    
     
    print_debug("Thoát hết các task ")
    sleep(5)
    os.system ("taskkill /f /im garena.exe") 
    sleep(5)
def doctkmk(stt):
    # Mở file văn bản với chế độ đọc
    f = open("acc.txt", "r")

# Duyệt qua các dòng của file với chỉ số
    for index, line in enumerate(f):
# Nếu chỉ số bằng 0, in ra dòng đó
        if index == stt:
            f.close()
            return line
        

# Đóng file
    f.close()

def click(tenhinh,type,solanclick):
    if tenhinh=='ok'or tenhinh =='okvien' or tenhinh=='warning':
        print_debug("")
    else:
        screen = pyautogui.screenshot()
    # Lưu lại thành tên screen.png
        screen.save('./data/screen.png')
    screen = cv2.imread('./data/screen.png')

# Đọc hình ảnh nhỏ cần tìm kiếm
    template = cv2.imread('./data/'+str(tenhinh)+'.PNG')

# Lấy kích thước của hình ảnh nhỏ
    h, w = template.shape[:2]

# Sử dụng phương pháp khớp mẫu để tìm vị trí của hình ảnh nhỏ trong hình ảnh lớn
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    if str(tenhinh)=='so8'or str(tenhinh)=='so81':
        threshold=0.92
    else:
        threshold = 0.9

# Lấy các vị trí thỏa mãn ngưỡng
    locations = np.where(result >= threshold)
    if locations[0].size > 0:
# Lấy tọa độ góc trên bên trái của hình chữ nhật
        top_left = (locations[1][0], locations[0][0])
# Lấy tọa độ góc dưới bên phải của hình chữ nhật
        bottom_right = (top_left[0] + w, top_left[1] + h)
# Lấy tọa độ điểm chính giữa của hình chữ nhật
        print_debug(str(type))
        center = (top_left[0] + w // 2, top_left[1]+int(type) + h // 2 )
        
        if int(solanclick)==100:
            print_debug('')
        else:
            pyautogui.moveTo(center,duration=0.25)
            if str(tenhinh)=='so8'or str(tenhinh)=='so81':
                pyautogui.click(center,None,int(solanclick),1)
            else:
                pyautogui.click(center,None,int(solanclick),0.3)
        print_debug('tim duoc roi '+ str(tenhinh))
        return 1
    else:
# In ra thông báo không tìm thấy hình ảnh nhỏ
        print_debug('')
        return 0

def dangnhapaccmoi(stt):
    print_debug("Đăng nhập số thứ tự " + str(stt))
    while not click('ffzik',0,1):
        print_debug("chua tim thay hinh ffzik")
        sleep(1)
    click('tamdungauto',0,1)
    if "garena.exe" not in (p.name() for p in psutil.process_iter()):
        os.startfile("C:\Program Files (x86)\Garena\Garena\Garena.exe")
        sleep(7)
        ketqua = doctkmk(stt)
        if ketqua == None:
            return False
        else:
            account, password = ketqua.split("|")
            if click('garena',0, 1):
                click ('garena',80, 3)
                sleep(1)
                pyautogui.write(str(account))
                click ('garena',120, 3)
                sleep(1)
                pyautogui.write(str(password))
                click ('garena',250, 3)
                sleep(1)      
            sleep(20)
            if click('game',0, 100):
                click ('game',280, 1)
            sleep(2)
            click('game',0, 1)
            sleep(10)
            if click('play',0,100):
                click('play',650, 1)
            return True
        # sleep(30)
        # os.system ("taskkill /f /im xcoronahost.xem")
    
def isrespondingPID():
        os.system('tasklist /FI "STATUS eq NOT RESPONDING" > tmp.txt')
        tmp = open('tmp.txt', 'r')
        a = tmp.readlines()
        tmp.close()
        print_debug(a[-1].split()[0])
        if a[-1].split()[0] == 'fczf.exe' :
            print_debug('FO4 NOT RESPONDING .... OFF NOWW')
            return True
        else:
            return False


def chay_tool():
    global var1,var2
    global label
    start_time90 = time()
    start_time_backup = time()
    sothutu = checkacctime()
    sothututam=-1
    biendem=0
    biendem1=0
    thoigianchay1acc=0
    thoigianchaybackup=0
    dathaypass2=0
    max = 10
    demdangnhap=0
    khoataikhoan=0

    count = 0
    thoigianvaogame = f"Thời Gian vào game: {count}"
    thongtin = f"Debug tool: {count}"
    while not stop_flag:
        now=  datetime.datetime.now()
        time1= now.strftime("%H:%M:%S %d/%m/%Y")
        print_debug(time1)
        
        try:
            end_time = time()
            sothutu = checkacctime()
            print_debug("so thu tu tam"+ str(sothutu))
            if sothututam==100:
                now1 = datetime.datetime.now()
                dathaypass2 = 0
                print_debug(now1)
                print_debug("trả về số thứ tự acc là " + str(sothutu))
                sothututam=sothutu 
                closefo4()
                demdangnhap = demdangnhap + 1
                if demdangnhap>=2:
                    sothutu = sothutu +1
                    if sothutu==11:
                        sothutu=0
                    with open("index.txt", "w") as f:
# Ghi số 1 vào tệp
                        f.write(str(sothutu))
                        f.close()
                else:
                    sleep(5)
                    dangnhapaccmoi(sothututam)

            if sothutu!=sothututam:
                dathaypass2 = 0
                demdangnhap=0
                now1 = datetime.datetime.now()
                print_debug(now1)
                print_debug("trả về số thứ tự acc là " + str(sothutu))
                start_time90= time()
                sothututam=sothutu
                closefo4()
                sleep(5)
                if not dangnhapaccmoi(sothututam):
                    sothutu = 0
                    with open("index.txt", "w") as f:
# Ghi số 1 vào tệp
                        f.write(str(sothutu))
                        f.close()
            if isrespondingPID():
                biendem=biendem+1
                if biendem>30:
                    print_debug(" 2 phút rồi fo4 not responding")
                    sothututam=100
                    biendem = 0

            if click('loimoi',0,1):
                sothututam=100
        # if 'xcoronahost.xem' in (p.name() for p in psutil.process_iter()):
            # if click('fconline',0,1):
                # os.system ("taskkill /f /im xcoronahost.xem")
            if 'chrome.exe' in (p.name() for p in psutil.process_iter()):
                if click('khoataikhoan',0,1):
                    sys.exit("You exited the program")
                os.system ("taskkill /f /im chrome.exe")
            if 'msedge.exe' in (p.name() for p in psutil.process_iter()):
                if click('khoataikhoan',0,1):
                    sys.exit("You exited the program")
                os.system ("taskkill /f /im msedge.exe")         


            if (thoigianchay1acc)>(max) or thoigianchaybackup>133:
                thoigianchay1acc = 0
                thoigianchaybackup = 0
                sothutu = sothutu +1
                if sothutu==11:
                    sothutu=0
                with open("index.txt", "w") as f:
# Ghi số 1 vào tệp
                    f.write(str(sothutu))
                    f.close()      
            if click('warning',0,1) :
                sothututam=100        
            if 'fczf.exe' not in (p.name() for p in psutil.process_iter()):
                biendem1=biendem1+1
                if biendem1>30:
                    print_debug(" 2 phút rồi không thấy fo4 chạy....")
                    sothututam=100
                    biendem1=0
            else:

                if click('iconfo4',0,100) or click('iconfo41',0,100):
                    if click('mksai1lan',0,1) or click('mksai2lan',0,1) or click('mksai3lan',0,1) or click('mksai4lan',0,1) :
                        sys.exit("You exited the program")
                    print_debug(" fo4 is runing..... ")
                    start_time_backup=time()
                    timedachaybackup= (int(start_time_backup)-int(end_time)+2)/int(60)
                    thoigianchaybackup =thoigianchaybackup + timedachaybackup
                    
                
                    print_debug(" Acc so thu tu: " + str(sothutu) + " TIME BACKUP " + str(thoigianchaybackup) + " phut ")    
                    biendem1=0
                
                else:
                    biendem1=biendem1+1
                    if biendem1>30:
                        print_debug(" 2 phút rồi không thấy fo4 chạy....")
                        sothututam=100
                        biendem1=0
                # click('dagialap',0,1)
            if dathaypass2:
                start_time90=time()
                timedachay= (int(start_time90)-int(end_time)+2)/int(60)
                thoigianchay1acc =thoigianchay1acc + timedachay
                print_debug(" Acc so thu tu: " + str(sothutu) + " Da chay duoc " + str(round(thoigianchay1acc, 2)) + " phut ")
                thoigianvaogame = f"Thời Gian: {str(round(thoigianchay1acc, 2))}" + "phút ... Acc thứ " + str(sothutu)
                label.config(text=f"{thoigianvaogame}\n")
            else:
                if click('so8',0,10) or click('so81',0,10)  :
                    start_time90=time()
                    dathaypass2=1
                    click('xacnhanpass2',0,1)
                    if var1.get()==1 or var2.get()==1:
                        while not click('tieptucpass2',0,1):
                            print_debug("chua tim thay hinh tiep tuc pass 2")
                            sleep(1)
                        while not click('doixh',0,1):
                            print_debug("chua tim thay hinh doixh")
                            sleep(1)
                    if var2.get()==1:
                        while not click('shop',0,1):
                            print_debug("chua tim thay hinh shop")
                            sleep(1)
                        while not click('sotay',0,1):
                            print_debug("chua tim thay hinh sotay")
                            sleep(1)
                        sleep(3)
                        if click('iconsotay',0,1):
                            sleep(5)
                            click('muasotay',0,1)
                            sleep(5)   
                            click('muasotay',0,1)
                            sleep(5)
                            click('muasotay1',0,1)
                            click('xacnhansaumua',0,1)
                        while not click('sukien',0,1):
                            print_debug("chua tim thay hinh sukien")
                            sleep(1)
                        sleep(3)
                        click('nhantatcasukien',0,1)
                        while not click('sotaysvipt1',0,1):
                            print_debug("chua tim thay hinh sotaysvipt1")
                            sleep(1)
                        sleep(3)
                        click('nhantatcasvipt1',0,1)
                        while not click('sotayvipt1',0,1):
                            print_debug("chua tim thay hinh sotayvipt1")
                            sleep(1)
                        sleep(3)
                        click('nhantatcasvipt1',0,1)
                    if var1.get()==1:
                        if click('kiemtrasvip',0,1):
                            print_debug("da co svip roi")
                        else:
                            while not click('vatpham',0,1):
                                print_debug("chua tim thay hinh vatpham")
                                sleep(1)
                            while not click('vatpham',0,1):
                                print_debug("chua tim thay hinh vatpham")
                                sleep(1)
                            while not click('nhantatcavatpham',0,1):
                                print_debug("chua tim thay hinh nhantatcavatpham")
                                sleep(1)
                            while not click('nhantatcavatpham1',0,1):
                                print_debug("chua tim thay hinh nhantatcavatpham")
                                sleep(1)
                            while not click('svip',0,1):
                                print_debug("chua tim thay hinh svip")
                                sleep(1)
                            while not click('nhansvip',0,1):
                                print_debug("chua tim thay hinh nhansvip")
                                sleep(1)
                            while not click('dongsvip',0,1):
                                print_debug("chua tim thay hinh nhantatcavatpham")
                                sleep(1)
                            
                    while not click('ffzik',0,1):
                            print_debug("chua tim thay hinh ffzik")
                            sleep(1)
                    while not click('dagialap',0,1):
                            print_debug("chua tim thay hinh dagialap")
                            sleep(1)
                    

                        

            sleep(2)
        except Exception as e:
            print_debug(e)
            with open("errror.txt", "w") as f:
# Ghi số 1 vào tệp
                f.write(str(e))
                f.close() 
            os.system("starttool.bat")
def start_thread():
    global stop_flag
    stop_flag = False
    thread = threading.Thread(target=chay_tool)
    thread.start()
def start_thread_update():
    thread = threading.Thread(target=check_for_updates)
    thread.start()
def stop_thread():
    global stop_flag
    stop_flag = True
def QUIT():
    window.quit()
    while 'main.exe' in (p.name() for p in psutil.process_iter()):
        os.system ("taskkill /im main.exe")
        window.quit()
window = tk.Tk()
window.title("Tool treo acc dùng thử")
window.geometry("400x300")

var1 = tk.IntVar()
var2 = tk.IntVar()
checkbutton1 = tk.Checkbutton(window, text="SVIP", variable=var1)
checkbutton2 = tk.Checkbutton(window, text="SỔ TAY", variable=var2)
button_start = tk.Button(window, text="Start", command=start_thread)
button_stop = tk.Button(window, text="Quit", command=QUIT)
button_capnhat = tk.Button(window, text="Cập Nhật", command=start_thread_update)
label = tk.Label(window, text="Phần mềm phiên bản số 1", font=("Arial", 12))
label.place(x=50, y=180)
label_debug = tk.Label(window, text="debug tool", font=("Arial", 12))
label_debug.place(x=50, y=210)

checkbutton1.pack()
checkbutton2.pack()
button_start.pack(pady=5)
button_stop.pack(pady=5)
button_capnhat.pack()
window.mainloop()
