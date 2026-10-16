suhu = float(input("masukkan suhu reaktor (celcius)"))
tekanan = float(input("masukkan tekanan gas (bar)"))

if suhu > 1000:
    if tekanan > 50:
        status = "segera evakuasi"
    else:
        status ="bahaya suhu: segera turunkan daya"
elif suhu > 500:
    if tekanan >30:
        status = "peringatan tekanan tidak stabil"
    else:
        status = "operasi reaktor normal"
else:
    status ="reaktor belum cukup panas"

pompa = "pompa maksimal" if suhu > 800 else "pompa normal"

print("suhu reaktor :", suhu, "derajat celcius")
print("tekanan gas :", tekanan, "bar")
print("status reaktor :", status)
print("status pompa :", pompa)