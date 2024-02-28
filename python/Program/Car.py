#Saya Muhammad Yusdan Ali Batubara NIM 2206847 mengerjakan latihan 4 dalam mata 
#kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya 
#tidak melakukan kecurangan seperti yang telah dispesifikasikan Aamiin.

# import Vehicle class
from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jumlah_kursi, jumlah_pintu):
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        self.jumlah_pintu = jumlah_pintu
        self.jumlah_kursi = jumlah_kursi

    #setter and getter
    def setJumlahPintu(self, jumlah_pintu):
        self.jumlah_pintu = jumlah_pintu
        
    def getJumlahPintu(self):
        return self.jumlah_pintu
    
    def setJumlahKursi(self, jumlah_kursi):
        self.jumlah_kursi = jumlah_kursi

    def getJumlahKursi(self):
        return self.jumlah_kursi
    
    # def printData(self):
    #     print("Plat Nomor:", self.getPlatNomor())
    #     print("Merk:", self.getMerk())
    #     print("Tahun Produksi:", self.getTahunProduksi())
    #     print("Warna:", self.getWarna())
    #     print("Jumlah Pintu:", self.getJumlahPintu())