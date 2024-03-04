#include <iostream>
#include <string>
using namespace std;

class ParkingLot {
private:
    int kapasistas;
    int jumlah_kendaraan;

public:
    // Constructor
    ParkingLot(int kapasistas) {
        this->kapasistas = kapasistas;
        this->jumlah_kendaraan = 0;
    }

    // Setters
    void setKapasistas(int kapasistas) {
        this->kapasistas = kapasistas;
    }

    void setJumlahKendaraan(int jumlah_kendaraan) {
        this->jumlah_kendaraan = jumlah_kendaraan;
    }

    // Getters
    int getKapasistas() {
        return this->kapasistas;
    }

    int getJumlahKendaraan() {
        return this->jumlah_kendaraan;
    }

    // Method to park vehicle
    void parkir_kendaraan(string merk) {
        if (this->jumlah_kendaraan < this->kapasistas) {
            this->jumlah_kendaraan++;
            cout << merk << " berhasil diparkir." << endl;
            cout << "Jumlah kendaraan di parkiran: " << this->jumlah_kendaraan << endl;
            if (this->jumlah_kendaraan == this->kapasistas) {
                cout << "Parkiran penuh" << endl;
            }
        } else {
            cout << "Kendaraan tidak bisa diparkir karena penuh" << endl;
        }
    }
};