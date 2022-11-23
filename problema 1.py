valoarea_monedei = [1, 5, 10, 25, 50]

def returnschimb(schimb, valoarea_monedei):
    returneaza = [0] * len(valoarea_monedei)
    
    for pos, moneda in enumerate(reversed(valoarea_monedei)):
         while moneda <= schimb:
             schimb = schimb - moneda
             returneaza[pos] += 1
    return(returneaza)

suma=int(input('Dati suma necesara='))
print('Valoarea monedei',[50,25,10,5,1])
print('Numarul de monede',returnschimb(suma, valoarea_monedei))

valoarea_bancnotei1 = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

def returnschimb1(schimb, valoarea_bancnotei1):
    returneaza = [0] * len(valoarea_bancnotei1)
    for pos, bancnota in enumerate(reversed(valoarea_bancnotei1)):
         while bancnota <= schimb:
             schimb = schimb - bancnota
             returneaza[pos] += 1
    return(returneaza)

suma1=int(input('Dati suma necesara='))
print('Valoarea bancnotei',[1000,500,200,100,50,20,10,5,2,1])
print('Numarul de bancnote',returnschimb1(suma1, valoarea_bancnotei1))


