import requests
import json
import os
import patoolib as patool
import time

def check_for_updates():
    # URL đến file JSON chứa thông tin phiên bản mới nhất
    url = "https://github.com/quocanhkcn2018/update_tu/raw/main/version.json"
    timsvip = 0
    while True:
        timsvip = timsvip + 1
        if timsvip == 5:
            print("Đang kiểm tra cập nhật...")
            break
        time.sleep(1)

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
            print("Có phiên bản mới. Đang tải về...")
            # Tải file về
            response = requests.get(latest_download_url)
            with open("new_version.zip", "wb") as f:
                f.write(response.content)

            # # Giải nén và cài đặt (phần này tùy thuộc vào cấu trúc của phần mềm)
            # # ...

            # # Cập nhật phiên bản hiện tại
            # with open("version.txt", "w") as f:
            #     f.write(latest_version)

            print("Cập nhật thành công! ")
        else:
            print("Bạn đang sử dụng phiên bản mới nhất.")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi kiểm tra cập nhật: {e}")


if __name__ == "__main__":
    check_for_updates()