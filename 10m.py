import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pay", "Ju", "Sha", "Yak"]
daromad = [120, 150, 100, 180, 200, 240, 210]
plt.plot(kunlar,daromad,marker="o",label="haftalik daromad")

plt.title("Bir haftalik daromad ")
plt.xlabel("Hafta kunlari")
plt.ylabel("Daromad")

plt.legend()
plt.grid(True)

plt.savefig("Daromad.png")
plt.show()