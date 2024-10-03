#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
Letras = input("Ponha uma consoante ou vogal em maiúsculo: ")
vogal = ('A', "E", "I", "O", "U")
consoante = ("B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z")

if (Letras in vogal):
   print("É uma vogal.");

if (Letras in consoante):
    print("É uma consoante.");
