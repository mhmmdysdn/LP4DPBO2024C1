#include <iostream>
#include <string>
using namespace std;

// Import class Vehicle
#include "Vehicle.cpp" // Assume Vehicle class is defined in Vehicle.h

class Motorcycle : public Vehicle {
private:
    string jenis_motor;
    double kapasitas_tangki;

public:
    // Constructor
    Motorcycle(string plat_nomor, string merk, int tahun_produksi, string warna, string jenis_motor, double kapasitas_tangki)
        : Vehicle(plat_nomor, merk, tahun_produksi, warna) {
        this->jenis_motor = jenis_motor;
        this->kapasitas_tangki = kapasitas_tangki;
    }

    // Setters
    void setJenisMotor(string jenis_motor) {
        this->jenis_motor = jenis_motor;
    }

    void setKapasitasTangki(double kapasitas_tangki) {
        this->kapasitas_tangki = kapasitas_tangki;
    }

    // Getters
    string getJenisMotor() {
        return this->jenis_motor;
    }

    double getKapasitasTangki() {
        return this->kapasitas_tangki;
    }
};