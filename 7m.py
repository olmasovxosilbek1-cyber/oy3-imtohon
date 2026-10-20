import csv
mahsulotlar = [
    ["Olma", 8000, 15],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

with open("products.csv", "w", newline="", encoding="utf-8") as fayl:
    yozuvchi = csv.writer(fayl)

    yozuvchi.writerow(["nom", "narx", "soni"])
    yozuvchi.writerows(mahsulotlar)

