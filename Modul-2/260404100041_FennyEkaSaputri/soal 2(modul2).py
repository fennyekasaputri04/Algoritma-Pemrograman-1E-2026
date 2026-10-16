total_awal = int(input("Masukkan total belanja (Rp): "))

if total_awal % 100000 == 0:      
    diskon = 100
    keterangan = "Kelipatan Rp100.000 (Gratis)"
elif total_awal % 50000 == 0:      
    diskon = 50
    keterangan = "Kelipatan Rp50.000 (Diskon 50%)"
elif total_awal % 10000 == 0:       
    diskon = 20
    keterangan = "Kelipatan Rp10.000 (Diskon 20%)"
elif total_awal >= 200000:         
    diskon = 10
    keterangan = "Belanja >= Rp200.000 (Diskon 10%)"
else:                               
    diskon = 0
    keterangan = "Tidak ada diskon (harga normal)"


potongan = total_awal * diskon // 100
total_bayar = total_awal - potongan

# 4. Status poin memakai ternary operator
status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("Total belanja awal :", "Rp", total_awal)
print("Promo yang didapat :", keterangan)
print("Total bayar        :", "Rp", total_bayar)
print("Status poin        :", status_poin)