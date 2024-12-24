import sys
from PyQt6.QtWidgets import QApplication, QWidget
from form import Ui_Form  # Import the generated form class
import pymysql


class MyForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dang_ky.clicked.connect(self.on_submit)

    def on_submit(self):
        # Handle form submission
        ho_va_ten = self.ho_va_ten.text()
        gioi_tinh = self.gioi_tinh.currentText()
        sms = self.sms.isChecked()
        four_g = self.four_g.isChecked()
        bao_goi_nho = self.bao_goi_nho.isChecked()
        video_call = self.video_call.isChecked()
        so_phut_goi = self.so_phut_goi.value()
        dung_luong_net = self.dung_luong_net.value()
        gia_thue_bao = self.gia_thue_bao.text()
        print(f"Họ và tên: {ho_va_ten}")
        print(f"Giới tính: {gioi_tinh}")
        print(f"Sử dụng SMS: {sms}")
        print(f"Sử dụng 4G: {four_g}")
        print(f"Sử dụng video call: {video_call}")
        print(f"Sử dụng báo gọi nhỡ: {bao_goi_nho}")
        print(f"Số phút gọi: {so_phut_goi}")
        print(f"Dung lượng net: {dung_luong_net}")
        print(f"Giá thuê bao: {gia_thue_bao}")

        try:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                database='quan_ly_dich_vu'
            )
            print("Kết nối database thành công")
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        
        cursor = conn.cursor()
            
        sql = "INSERT INTO user_info_with_service (ho_va_ten, gioi_tinh, sms, four_g, video_call, bao_goi_nho, so_phut_goi, dung_luong_net) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (ho_va_ten, gioi_tinh, sms, four_g, video_call, bao_goi_nho, so_phut_goi, dung_luong_net)
         
        try:
            cursor.execute(sql, val)
            conn.commit()
            print("Dữ liệu đã được lưu thành công!")
        except:
            print("Lưu dữ liệu thất bại")
        finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())