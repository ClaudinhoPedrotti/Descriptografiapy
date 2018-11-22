import string
letras=list(string.ascii_lowercase)
chave=0
palavra = input("Informe uma palavra: ")
while chave<26:
    #chave = eval(input("Informe uma chave: "))

    tamanho_da_palavra = len(palavra)

    crip = list(palavra)
    palavra_crip = palavra

    x=0
    y=0

    chave = chave + 1

    for y in range (tamanho_da_palavra):
        while palavra[y] != letras[x]:
            x=x+1
            
        x=x-chave
        #print(letras[x])

        crip[y] = letras[x]
        #chave = chave + 1
        x=0
        
    palavra_crip="".join(crip)
    print(palavra_crip , "chave é" , chave)
    
print("Acabou")

