berangkat = 100
pulang = 100
konsumsi = 40
bensin = 1.5
harga_bensin = 10000

total_pp = berangkat + pulang 
total_kebutuhan_bahan_bakar = total_pp / konsumsi
total_bahan_bakar_yang_harus_dibeli = total_kebutuhan_bahan_bakar - bensin
total_biaya_yang_dikeluarkan = total_bahan_bakar_yang_harus_dibeli * harga_bensin

print("total pulang pergi =" , total_pp, "km")
print("total kebutuhan bahan bakar ="  , total_kebutuhan_bahan_bakar, "liter")
print("bahan bakar yang harus dibeli =" , total_bahan_bakar_yang_harus_dibeli, "liter")
print("biaya bensin =" , total_biaya_yang_dikeluarkan)