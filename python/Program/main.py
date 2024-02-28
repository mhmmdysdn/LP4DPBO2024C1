#Saya Muhammad Yusdan Ali Batubara NIM 2206847 mengerjakan latihan 4 dalam mata 
#kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya 
#tidak melakukan kecurangan seperti yang telah dispesifikasikan Aamiin.

#import vehicle
from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot

# create object
car1 = Car("B 1234 XYZ", "Toyota", 2019, "Merah", 4, 4)
car2 = Car("B 4321 XYZ", "Honda", 2018, "Hitam", 4, 4)
car3 = Car("B 5678 XYZ", "Mitsubishi", 2017, "Putih", 4, 4)
car4 = Car("B 8765 XYZ", "Suzuki", 2016, "Biru", 4, 4)
car5 = Car("B 9101 XYZ", "Daihatsu", 2015, "Silver", 4, 4)

motorcycle1 = Motorcycle("B 1234 XYZ", "Yamaha", 2019, "Biru", "Matic", 6)
motorcycle2 = Motorcycle("B 4321 XYZ", "Suzuki", 2018, "Putih", "Manual", 7)
motorcycle3 = Motorcycle("B 5678 EFD", "Honda", 2017, "Hitam", "Matic", 5)
motorcycle4 = Motorcycle("B 8765 EFD", "Kawasaki", 2016, "Merah", "Manual", 8)
motorcycle5 = Motorcycle("B 9101 EFD", "Ducati", 2015, "Silver", "Matic", 5)
motorcycle6 = Motorcycle("B 9101 EFD", "Beat", 2015, "Silver", "Matic", 5)

garasi1 = Garage("Garasi 1", 1000)
garasi1.addKendaraan(car1)
garasi1.addKendaraan(car2)
garasi1.addKendaraan(car3)
garasi1.addKendaraan(car4)
garasi1.addKendaraan(car5)
garasi1.addKendaraan(motorcycle1)
garasi1.addKendaraan(motorcycle2)
garasi1.addKendaraan(motorcycle3)
garasi1.addKendaraan(motorcycle4)
garasi1.addKendaraan(motorcycle5)

parkiran1 = ParkingLot(10)
parkiran1.parkir_kendaraan(car1)
parkiran1.parkir_kendaraan(car2)
parkiran1.parkir_kendaraan(car3)
parkiran1.parkir_kendaraan(car4)
parkiran1.parkir_kendaraan(car5)
parkiran1.parkir_kendaraan(motorcycle1)
parkiran1.parkir_kendaraan(motorcycle2)
parkiran1.parkir_kendaraan(motorcycle3)
parkiran1.parkir_kendaraan(motorcycle4)
parkiran1.parkir_kendaraan(motorcycle5)

if parkiran1.jumlah_kendaraan < parkiran1.kapasistas:
    garasi1.addKendaraan(motorcycle6)
    parkiran1.parkir_kendaraan(motorcycle6)

#tampilkan informasi garasi
print()
print("Informasi Garasi")
print("Nama Garasi      :", garasi1.getNamaGarasi())
print("Luas Garasi      :", garasi1.getLuasGarasi(), "m2")
print()
print("List Kendaraan:")
for kendaraan in garasi1.list_kendaraan:
    if isinstance(kendaraan, Car):
        print("     Mobil")
    elif isinstance(kendaraan, Motorcycle):
        print("     Motor")
    print("Plat Nomor       :", kendaraan.getPlatNomor())
    print("Merk             :", kendaraan.getMerk())
    print("Tahun Produksi   :", kendaraan.getTahunProduksi())
    print("Warna            :", kendaraan.getWarna())
    if isinstance(kendaraan, Car):
        print("Jumlah Pintu     :", kendaraan.getJumlahPintu())
    elif isinstance(kendaraan, Motorcycle):
        print("Jenis Motor      :", kendaraan.getJenisMotor())
        print("Kapasitas Tangki :", kendaraan.getKapasitasTangki(), "liter")
    print()

#tampilkan informasi parkiran
print("Informasi Parkiran")
print("Kapasistas Parkiran:", parkiran1.getKapasistas())
print("Jumlah Kendaraan di Parkiran:", parkiran1.getJumlahKendaraan())