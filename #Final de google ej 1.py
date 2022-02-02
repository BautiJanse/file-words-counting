#Final de google ej 1

#Funciones

def abrirarch():
    try:
        arch=open("Frases.txt","r")
        palabras(arch,lista3,lista4,lista5,lista6,lista7)
        contar(lista3,final)
        contar(lista4,final)
        contar(lista5,final)
        contar(lista6,final)
        contar(lista7,final)
        
        
    except OSError as mensaje:
        print("No se pudo abrir el archivo:", mensaje)
    finally:
        try:
            arch.close()
            
        except NameError:
            pass

def palabras(arch,lista3,lista4,lista5,lista6,lista7):
    for linea in arch:
        linea=linea.rstrip("\n")
        linea=linea.split(" ")
        for i in linea:
            i=i.rstrip(",")
            i=i.rstrip(".")
            i=i.rstrip(":")
            i=i.rstrip(";")
            i=i.lower()
            if len(i)==3:
                lista3.append(i)
            elif len(i)==4:
                lista4.append(i)
            elif len(i)==5:
                lista5.append(i)
            elif len(i)==6:
                lista6.append(i)
            elif len(i)==7:
                lista7.append(i)
        
def contar(lista,final):
    lista.sort()
    for i in lista:
        a=lista.count(i)
        if i not in final:
            print(f"La palabra {i} aparece una cantidad de {a} veces.")
            final.append(i)
        else:
            pass
        


#Programa principal

lista3=[]
lista4=[]
lista5=[]
lista6=[]
lista7=[]
lista8=[]
lista9=[]
lista10=[]
final=[]


abrirarch()
print(lista3)
print(lista4)
print(lista5)
print(lista6)
print(lista7)
