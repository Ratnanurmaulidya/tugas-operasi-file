print("ratna nur maulidya 12 rpl 2")

def bacafile():
    nama_file = 'biodata.txt'
    with open("biodata.txt","r") as membaca:
        text = membaca.read()
        print(text)

bacafile()

def tulisfile():
    text = input("")
    with open("biodata.txt","r") as menulis:
        menulis.write(text)
        print(text)

tulisfile()