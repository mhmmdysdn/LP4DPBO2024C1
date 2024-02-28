#Saya Muhammad Yusdan Ali Batubara NIM 2206847 mengerjakan latihan 4 dalam mata 
#kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya 
#tidak melakukan kecurangan seperti yang telah dispesifikasikan Aamiin.

class Vehicle:
    def __init__(self, plat_nomor, merk, tahun_produksi, warna):
        self.plat_nomor = plat_nomor
        self.merk = merk
        self.tahun_produksi = tahun_produksi
        self.warna = warna

    #setter and getter
    
    def setPlatNomor(self, plat_nomor):
        self.plat_nomor = plat_nomor

    def getPlatNomor(self):
        return self.plat_nomor
    
    def setMerk(self, merk):
        self.merk = merk

    def getMerk(self):
        return self.merk
    
    def setTahunProduksi(self, tahun_produksi):
        self.tahun_produksi = tahun_produksi

    def getTahunProduksi(self):
        return self.tahun_produksi
    
    def setWarna(self, warna):
        self.warna = warna

    def getWarna(self):
        return self.warna