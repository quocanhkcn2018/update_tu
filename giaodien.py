import tkinter as tk
import threading

def start_printing():
    def print_loop():
        while True:
            if stop_flag:
                break
            print("Quốc Anh")
            window.after(1000)  # Cập nhật giao diện sau mỗi 1 giây

    global stop_flag
    stop_flag = False
    thread = threading.Thread(target=print_loop)
    thread.start()

def stop_printing():
    global stop_flag
    stop_flag = True

# Tạo cửa sổ
window = tk.Tk()
window.title("Ứng dụng in chữ")

# Tạo nút Start
start_button = tk.Button(window, text="Start", command=start_printing)
start_button.pack()

# Tạo nút Stop
stop_button = tk.Button(window, text="Stop", command=stop_printing)
stop_button.pack()

# Vòng lặp chính
window.mainloop()