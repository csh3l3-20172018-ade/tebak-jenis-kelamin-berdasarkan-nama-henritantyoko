#membuat program dimana sebuah nama lengkap diidentifikasikan gendernya, apa itu perempuan atau laki-laki
# pengecekkan nama hanya dilakukan di kata pertama, setelah spasi maka tidak diidentifikasi lagi kata berikutnya

print("============Identifikasi Nama==================")
nama = input("NAMA = ").lower()              #menginputkan nama lengkap, huruf besar dan kecil tak berpengaruh
laki = perempuan = noidentify = i = 0        #set variable menjadi 0

while(nama[i] !=" "):                        #terus berulang dan berhenti ketika ada spasi
    if(nama[i]=='b'):                        #kondisi jika kata ke i dari array nama ternyata sama dengan b
        laki += 1                            #maka variable laki bertambah 1
    elif(nama[i] == 'd'):
        laki += 1
    elif (nama[i] == 'o'):
        laki += 1
    elif (nama[i] == 'a'):                   #kondisi jika kata ke i dari array nama ternyata sama dengan a
        perempuan += 1                       #maka variable perempuan bertambah 1
    elif (nama[i] == 'i'):
        perempuan += 1
    elif (nama[i] == 'u'):
        perempuan += 1
    elif (nama[i] == 'e'):
        perempuan += 1
    elif (nama[i] == 'o'):
        perempuan += 1
    elif (nama[i] == 't'):
        perempuan += 1
    elif (nama[i] == 'l'):
        perempuan += 1
    else:                                    #kondisi selain kondisi diatas
        noidentify += 1                      #maka variable nodidentify bertambah 1
    i+=1                                     #penanda array bertambah 1 untuk pindah karakter

print("Jumlah huruf laki = ",laki)
print("Jumlah huruf perempuan = ",perempuan)
print("Jumlah huruf no identify = ",noidentify)
print("==========HASIl===========")
if (laki)>(perempuan):                        #kondisi jika jumlah huruf identifikasi laki-laki lebih besar dari perempuan
    print(" Gender adalah laki-laki")         #hasilnya gender laki-laki
elif(laki)<(perempuan):
    print("Gender adalah perempuan")
else :
    print("Gender tidak diketahui")

#Hasil Percobaan
# henri tantyoko = perempuan
# bramantyo agung = perempuan
# wawan suloyo = perempuan
# sopian pratama putra = perempuan
# adityo nugroho = perempuan

# dari hasil perobaan dapat ditarik kesimpulan jika ternyata dari 5 teman laki-laki saya teryata kllima teman saya perempuan
# jika pengidentifikasian menggunakan requirement diatas
# banyak nama yang menggunakan huruf vokal dan itu ternyata diidentifikasi sebagai perempuan, sebaiknya identifikasinya lebih detil dengan kombinasi yang sesuai