# input: người dùng nhập vào mã nhân viên, họ tên
# ouput: lỗi khi thông tin bị bỏ trống hoặc chứa khoảng trắng, thành công in phiếu

# dùng vòng lặp while khởi tạo while true thành vòng lặp vô hạn, cho chạy điều kiện trong vòng lặp
# nếu đúng hết thì thoát vòng lặp

while(True):
    employee_id = input("Nhập mã nhân viên: ")
    full_name = input("Nhập họ tên: ")

    if (
        employee_id.strip() == "" or full_name.strip() == "" or " " in employee_id):
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
    else:
        print("Tạo hồ sơ thành công!")
        break
