from kurs import kurs as ks #Import dictionary kurs dari file kurs

def konversi(jumlah, dari, ke): #Membuat fungsi konversi dengan parameter jumlah, dari, dan ke
    if dari == "IDR": #Jika dari (mata uang asal) sama dengan "IDR"
        return jumlah/ks[ke] #Kembalikan jumlah/ks[ke]
    elif ke == "IDR": #Jika ke (mata uang tujuan konversi) sama dengan "IDR"
        return jumlah*ks[dari] #Kembalikan jumlah*ks[dari]
    else: #Yang lain
        return (jumlah*ks[dari])/ks[ke] #Kembalikan (jumlah*ks[dari])/ks[ke]