#include <iostream>
#include <string>
using namespace std;

#include "Vehicle.cpp" // Assume Vehicle class is defined in Vehicle.h

class Car : public Vehicle {
private:
    int jumlah_pintu;
    int jumlah_kursi;

public:
    // Constructor
    Car(string plat_nomor, string merk, int tahun_produksi, string warna, int jumlah_kursi, int jumlah_pintu)
        : Vehicle(plat_nomor, merk, tahun_produksi, warna) {
        this->jumlah_pintu = jumlah_pintu;
        this->jumlah_kursi = jumlah_kursi;
    }

    // Setters
    void setJumlahPintu(int jumlah_pintu) {
        this->jumlah_pintu = jumlah_pintu;
    }

    void setJumlahKursi(int jumlah_kursi) {
        this->jumlah_kursi = jumlah_kursi;
    }

    // Getters
    int getJumlahPintu() {
        return this->jumlah_pintu;
    }

    int getJumlahKursi() {
        return this->jumlah_kursi;
    }
};