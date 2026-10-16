pin = int(input("masukkan 3 digit PIN"))
waktu = int(input("waktu kedatangan (0-23)"))

digit_1 = pin // 100
digit_2 = (pin //10) % 10
digit_3 = pin % 10
print(f"digit PIN: {digit_1}, {digit_2}, {digit_3}")

if pin % 5 == 0:
    if waktu < 12:
        pesan = "garasi pagi terbuka"
    else:
        pesan = "garasi malam terbuka, lampu dinyalakan"
elif pin % 2 == 0:
    if digit_1 + digit_3 == digit_2:
        pesan = "garasi VIP terbuka khusus bos"
    else:
        pesan = "kode genap ditolak, alarm berbunyi"
else:
    pesan = "akses ditolak"
print(pesan)

# print("mode malam merekam" if waktu > 18 else "mode siang stanby")

if waktu > 18:
    print("mode malam merekam")
else:
    print ("mode siang stanby")