# CLASS & OBJECT
class Mobil:
    def __init__(self,warna,brand,seri):
        self.warna = warna
        self.brand = brand
        self.seri = seri
        self.BBM = "bensin"
        self.jumlah_roda = 4

    def display_car_info(self): # NAMA FUNGSI ITU PAKE NAMA VERB
        print("Mobil {} {} {} berbahan bakar {} beroda {}".format(self.brand, self.seri, self.warna, self.BBM, self.jumlah_roda))
    
    def change_jumlah_roda(self, jumlah_roda):
        self.jumlah_roda = jumlah_roda
    
    def change_brand(self, brand):
        self.brand = brand

mobil1 = Mobil("Putih","Mazda","MX-5")
mobil1.display_car_info()
mobil1.change_jumlah_roda(jumlah_roda=10)
mobil1.change_brand(brand="Honda")
mobil1.display_car_info()

# print(mobil1.change_brand())


# mobil1.display_car_info()




# mobil2 = Mobil("Hitam","Toyota",86)
# mobil2.myfunction()

# mobil3 = Mobil("Hijau","Toyota","Avanza")
# mobil3.myfunction()

# mobil_warna = input("Warna Mobil: ")
# mobil_warna.myfunction(self.warna)


# mobil_brand = input("Brand Mobil: ")
# mobil_brand.myfunction(self.brand)
# mobil_seri = input("Seri Mobil: ")
# mobil_seri.myfunction(self.seri)

# # BLUEPRINT WAY OF THINKING
# class ManipulateExcel():

#     def __init__(file_location, sheet_name):

#         pass
#     def read_columns():
#         pass

#     def calculate_total_rows():
#         pass

#     def find_specific_value(row,column):
#         pass

# class ManipulateCSV():

#     def __init__(file_location):

#         pass
#     def read_columns():
#         pass

#     def calculate_total_rows():
#         pass

#     def find_specific_value(row,column):
#         pass

# excel1 = ManipulateExcel("./Employee.xlsx")
# excel2 = ManipulateExcel("./Salary.xlsx")
# excel3 = ManipulateExcel("./Departments.xlsx")

# print(excel1.read_columns())
# print(excel2.read_columns())