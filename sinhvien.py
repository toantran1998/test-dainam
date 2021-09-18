def nhap_data():
    """Hàm nhập dữ liệu vào mảng"""
    global listStudents
    while True:
        print('Nhập tên sinh viên cần thêm: ')
        tmp = input()
        if tmp == '0':
            break
        listStudents.append(tmp)


def tim_sinhvien(name, listStudents):
    """hàm tìm thông tin sinh viên"""
    result = -1
    for i in range(0, len(listStudents)):
        if listStudents[i] == name:
            result = i
            break

    return result


# chương trình chính
print("Chương trình quản lý sinh viên bằng Python")

print("Bước 1: Nhập danh sách sinh viên")
print("Gõ 0 để thoát khỏi chương trình")

listStudents = []
nhap_data()

print("Bước 2: Nhập tên sinh viên muốn tìm")
name = input()

index = tim_sinhvien(name, listStudents)

if (index == -1):
    print("Không tìm thấy sinh viên")
else:
    print("Sinh viên được tìm thấy tại vị trí ", index + 1)