def tashqi_funksiya(koeffitsiyent):
    def ichki_funksiya(son):
        return son * koeffitsiyent
    return ichki_funksiya

koeffitsiyent = 4
qiymat = 7

kopaytirish = tashqi_funksiya(koeffitsiyent)
natija = kopaytirish(qiymat)

print("Natija:", natija)