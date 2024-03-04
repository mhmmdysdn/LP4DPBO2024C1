#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
using namespace std;


// Import class headers
#include "Vehicle.cpp"
#include "Car.cpp"
#include "Motorcycle.cpp"
#include "Garage.cpp"
#include "ParkingLot.cpp"

int main() {
    // Create objects
    Car car1("B 1234 XYZ", "Toyota", 2019, "Merah", 4, 4);
    Car car2("B 4321 XYZ", "Honda", 2018, "Hitam", 4, 4);
    Car car3("B 5678 XYZ", "Mitsubishi", 2017, "Putih", 4, 4);
    Car car4("B 8765 XYZ", "Suzuki", 2016, "Biru", 4, 4);
    Car car5("B 9101 XYZ", "Daihatsu", 2015, "Silver", 4, 4);

    Motorcycle motorcycle1("B 1234 XYZ", "Yamaha", 2019, "Biru", "Matic", 6);
    Motorcycle motorcycle2("B 4321 XYZ", "Suzuki", 2018, "Putih", "Manual", 7);
    Motorcycle motorcycle3("B 5678 EFD", "Honda", 2017, "Hitam", "Matic", 5);
    Motorcycle motorcycle4("B 8765 EFD", "Kawasaki", 2016, "Merah", "Manual", 8);
    Motorcycle motorcycle5("B 9101 EFD", "Ducati", 2015, "Silver", "Matic", 5);
    Motorcycle motorcycle6("B 9101 EFD", "Beat", 2015, "Silver", "Matic", 5);

    Garage garasi1("Garasi 1", 1000);

    // Add vehicles to garage
    garasi1.addKendaraan(car1);
    garasi1.addKendaraan(car2);
    garasi1.addKendaraan(car3);
    garasi1.addKendaraan(car4);
    garasi1.addKendaraan(car5);
    garasi1.addKendaraan(motorcycle1);
    garasi1.addKendaraan(motorcycle2);
    garasi1.addKendaraan(motorcycle3);
    garasi1.addKendaraan(motorcycle4);
    garasi1.addKendaraan(motorcycle5);

    ParkingLot parkiran1(10);

    // Park vehicles
    parkiran1.parkir_kendaraan(car1.getMerk());
    parkiran1.parkir_kendaraan(car2.getMerk());
    parkiran1.parkir_kendaraan(car3.getMerk());
    parkiran1.parkir_kendaraan(car4.getMerk());
    parkiran1.parkir_kendaraan(car5.getMerk());
    parkiran1.parkir_kendaraan(motorcycle1.getMerk());
    parkiran1.parkir_kendaraan(motorcycle2.getMerk());
    parkiran1.parkir_kendaraan(motorcycle3.getMerk());
    parkiran1.parkir_kendaraan(motorcycle4.getMerk());
    parkiran1.parkir_kendaraan(motorcycle5.getMerk());

    if (parkiran1.getJumlahKendaraan() < parkiran1.getKapasistas()) {
        garasi1.addKendaraan(motorcycle6);
        parkiran1.parkir_kendaraan(motorcycle6.getMerk());
    }

    // Display garage information
    cout << "\nInformasi Garasi" << endl;
    cout << "Nama Garasi      : " << garasi1.getNamaGarasi() << endl;
    cout << "Luas Garasi      : " << garasi1.getLuasGarasi() << "m2" << endl;
    cout << "\nList Kendaraan:" << endl;

    for (Vehicle kendaraan : garasi1.getListKendaraan()) {
        cout << "Plat Nomor: " << kendaraan.getPlatNomor() << endl;
        cout << "Merk: " << kendaraan.getMerk() << endl;
        cout << "Tahun Produksi: " << kendaraan.getTahunProduksi() << endl;
        cout << "Warna: " << kendaraan.getWarna() << endl;
        cout << endl;
    }

    // Display parking lot information
    cout << "Informasi Parkiran" << endl;
    cout << "Kapasistas Parkiran            : " << parkiran1.getKapasistas() << endl;
    cout << "Jumlah Kendaraan di Parkiran  : " << parkiran1.getJumlahKendaraan() << endl;

    return 0;
}
