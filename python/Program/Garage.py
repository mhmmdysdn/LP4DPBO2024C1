#Saya Muhammad Yusdan Ali Batubara NIM 2206847 mengerjakan latihan 4 dalam mata 
#kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya 
#tidak melakukan kecurangan seperti yang telah dispesifikasikan Aamiin.

class Garage:
    def __init__(self, nama_garasi, luas_garasi):
        self.nama_garasi = nama_garasi
        self.luas_garasi = luas_garasi
        self.list_kendaraan = []

    def setNamaGarasi(self, nama_garasi):
        self.nama_garasi = nama_garasi

    def getNamaGarasi(self):
        return self.nama_garasi
    
    def setLuasGarasi(self, luas_garasi):
        self.luas_garasi = luas_garasi

    def getLuasGarasi(self):
        return self.luas_garasi
    
    def addKendaraan(self, kendaraan):
        self.list_kendaraan.append(kendaraan)
       