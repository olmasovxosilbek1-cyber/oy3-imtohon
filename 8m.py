import json

with open("products.json", "r", encoding="utf-8") as fayl:
    products = json.load(fayl)

nom = input("Mahsulot nomi: ")
yangi_miqdor = int(input("Yangi miqdor: "))

topildi = False

for mahsulot in products:
    if mahsulot["nom"].lower() == nom.lower():
        mahsulot["miqdor"] = yangi_miqdor
        topildi = True
        break

if topildi:
    with open("products.json", "w", encoding="utf-8") as fayl:
        json.dump(products, fayl, ensure_ascii=False, indent=4)
    print("Mahsulot miqdori yangilandi!")
else:
    print("Mahsulot topilmadi!")