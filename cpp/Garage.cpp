#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Import class Vehicle
#include "Vehicle.cpp" // Assume Vehicle class is defined in Vehicle.h

class Garage {
private:
    string nama_garasi;
    double luas_garasi;
    vector<Vehicle> list_kendaraan;

public:
    // Constructor
    Garage(string nama_garasi, double luas_garasi) {
        this->nama_garasi = nama_garasi;
        this->luas_garasi = luas_garasi;
    }

    // Setters
    void setNamaGarasi(string nama_garasi) {
        this->nama_garasi = nama_garasi;
    }

    void setLuasGarasi(double luas_garasi) {
        this->luas_garasi = luas_garasi;
    }

    // Getters
    string getNamaGarasi() {
        return this->nama_garasi;
    }

    double getLuasGarasi() {
        return this->luas_garasi;
    }

    // Method to add vehicle to garage
    void addKendaraan(Vehicle kendaraan) {
        this->list_kendaraan.push_back(kendaraan);
    }

    //getListKendaraan
    vector<Vehicle> getListKendaraan() {
        return this->list_kendaraan;
    }
};