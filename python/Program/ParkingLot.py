#Saya Muhammad Yusdan Ali Batubara NIM 2206847 mengerjakan latihan 4 dalam mata 
#kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya 
#tidak melakukan kecurangan seperti yang telah dispesifikasikan Aamiin.

class ParkingLot:
    def __init__(self, kapasistas):
        self.kapasistas = kapasistas
        self.jumlah_kendaraan = 0

    def setKapasistas(self, kapasistas):
        self.kapasistas = kapasistas

    def getKapasistas(self):
        return self.kapasistas
    
    def setJumlahKendaraan(self, jumlah_kendaraan):
        self.jumlah_kendaraan = jumlah_kendaraan

    def getJumlahKendaraan(self):
        return self.jumlah_kendaraan
    
    def parkir_kendaraan(self, kendaraan):
        if self.jumlah_kendaraan < self.kapasistas:
            self.jumlah_kendaraan += 1
            print(f"{kendaraan.merk} berhasil diparkir.")
            print("Jumlah kendaraan di parkiran:", self.jumlah_kendaraan)
            if self.jumlah_kendaraan == self.kapasistas:
                print("Parkiran penuh")
        else:
            print("Kendaraan tidak bisa diparkir karena penuh")