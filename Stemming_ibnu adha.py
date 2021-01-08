# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

jawab = 'ya'
# stemming process
while (True):
    kalimat = input("Masukan Kata atau kalimat yang akan distemming : ")

    output  = stemmer.stem(kalimat)

    print("Kata Sebelum di Stemming: " + kalimat)   
    print("Kata Setelah di Stemming: " + output)

    jawab = input("Coba Kalimat / Kata Lain??? [ya/tidak]  ")
    if jawab == 'tidak':
        print("Terima Kasih Telah Mencoba")
        print("Ibnu Adha Shaleh")
        print("Nim : 171011400248")
        print("Kelas : 07TPLM002")

        break


