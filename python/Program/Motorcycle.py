#Saya Muhammad Yusdan Ali Batubara NIM 2206847 mengerjakan latihan 4 dalam mata 
#kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya 
#tidak melakukan kecurangan seperti yang telah dispesifikasikan Aamiin.

# import vehicle class
from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jenis_motor, kapasitas_tangki):
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        self.jenis_motor = jenis_motor
        self.kapasitas_tangki = kapasitas_tangki

    #setter and getter
    def setJenisMotor(self, jenis_motor):
        self.jenis_motor = jenis_motor

    def getJenisMotor(self):
        return self.jenis_motor
    
    def setKapasitasTangki(self, kapasitas_tangki):
        self.kapasitas_tangki = kapasitas_tangki

    def getKapasitasTangki(self):
        return self.kapasitas_tangki

    # def printData(self):
    #     print("Plat Nomor:", self.getPlatNomor())
    #     print("Merk:", self.getMerk())
    #     print("Tahun Produksi:", self.getTahunProduksi())
    #     print("Warna:", self.getWarna())
    #     print("Jumlah Kursi:", self.getJumlahKursi())