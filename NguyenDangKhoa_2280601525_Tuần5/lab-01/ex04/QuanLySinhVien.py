# Định nghĩa lớp SinhVien ngay trong file này để dễ sử dụng
class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocluc = "" # Đổi _hocLuc thành _hocluc cho thống nhất với cách dùng trong xepLoaiHocLuc

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if (self.soluongSinhVien() > 0):
            # Sắp xếp danh sách theo ID để đảm bảo maxId luôn đúng
            self.listSinhVien.sort(key=lambda sv: sv._id) 
            maxId = self.listSinhVien[-1]._id + 1 # Lấy ID lớn nhất và cộng 1
        return maxId

    def soluongSinhVien(self):
        return len(self.listSinhVien) 

    def nhapSinhVien(self):
        svid = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        
        while True: # Vòng lặp để đảm bảo nhập điểm hợp lệ
            try:
                diemTB = float(input("Nhap diem cua sinh vien: "))
                if 0 <= diemTB <= 10: # Giả sử điểm từ 0 đến 10
                    break
                else:
                    print("Diem phai nam trong khoang tu 0 den 10.")
            except ValueError:
                print("Diem khong hop le. Vui long nhap mot so.")
        
        sv = SinhVien(svid, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv:SinhVien = self.findByID(ID)
        if (sv != None):
            print(f"\nCap nhat thong tin sinh vien co ID = {ID}:")
            name = input(f"Nhap ten sinh vien (hien tai: {sv._name}): ")
            sex = input(f"Nhap gioi tinh sinh vien (hien tai: {sv._sex}): ")
            major = input(f"Nhap chuyen nganh cua sinh vien (hien tai: {sv._major}): ") 
            
            while True:
                try:
                    diemTB = float(input(f"Nhap diem cua sinh vien (hien tai: {sv._diemTB}): "))
                    if 0 <= diemTB <= 10:
                        break
                    else:
                        print("Diem phai nam trong khoang tu 0 den 10.")
                except ValueError:
                    print("Diem khong hop le. Vui long nhap mot so.")

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
            print(f"Cap nhat sinh vien co ID = {ID} thanh cong!")
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        print("\nDanh sach sinh vien da duoc sap xep theo ID.")

    def sortByName(self):
        # Sắp xếp theo tên, có thể cần xử lý tiếng Việt không dấu nếu muốn sắp xếp chuẩn hơn
        self.listSinhVien.sort(key=lambda x: x._name.lower(), reverse=False)
        print("\nDanh sach sinh vien da duoc sap xep theo ten.")

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
        print("\nDanh sach sinh vien da duoc sap xep theo diem trung binh.")

    def findByID(self, ID):
        searchResult = None
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
                    break 
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soluongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv._name.upper()): # Tìm kiếm không phân biệt hoa thường
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv:SinhVien):
        if (sv._diemTB >= 8):
            sv._hocluc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocluc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yeu"

    def showSinhVien(self, listSV):
        if not listSV: # Kiểm tra danh sách rỗng
            print("Khong co sinh vien nao de hien thi.")
            return

        print("{:<8} {:<18} {:<8} {:<15} {:<10} {:<10}".format("ID", "Ho Ten", "Gioi Tinh", "Chuyen Nganh", "Diem TB", "Hoc Luc"))
        print("-" * 77) # Dòng kẻ ngang để dễ nhìn

        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<15} {:<10.2f} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien