import time
import images
import png


def write(messaggio):
    lst = [ord(x) for x in messaggio]
    #write a list that convert in ascii format every letter of the messsage

    img = images.load("image.png")
    #loads the image
    
    img2 = []
    #create a new list containing all the pixels in the image and converts them from tuples to lists so we can write into them
    for lista in range(len(img)):
        img2.append([])
        for tupla in img[lista]:
            img2[lista].append(list(tupla))

    images.save(img2,"output")

    c = 0
    for x in range(len(lst)):
        #I use a counter so if the lenght of the phrase is bigger than the width of the image we can write into the image changing the X (height) coordinate
        print("entra")
        try:
            img2[c % len(img)][0+x][0] = lst[x]
            #in the first element of the RGB pixel we write our letter
        except:
            #if the phrase is longer than the images width we shift to another x coordinate that is a bit distant from the previous one
            c+=10
    images.save(img2,"output.png")

def leggi(immagine):
    #we read the image using the same logic
    img = images.load(immagine)
    str = ""
    c = 0
    while True:
        for tupla in img[c % len(img)]:
            if (tupla[0] < ord("a") or tupla[0] > ord("z")) and chr(tupla[0]) not in [" ",","]:
                return str
            str+=chr(tupla[0])
        c+= 10
#write("sto scrivendo, sto scrivendo" * 20)
#write(input("inserisci il messaggio: "))
print(leggi("output.png"))

