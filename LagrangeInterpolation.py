def wypelnianieListy(a,n):
    i=0
    while i<n:
        a.append(float(input("Podaj: ")))
        i=i+1
def check(a,n,punkt):
    result=True
    i=0
    while i<n-1:
        if(a[i]>=a[i+1]):
            result=False
        i=i+1
    if(punkt<a[0] or punkt>a[n-1]):
        result=False
    return result
def lagrange(a,b,n,punkt):
    i=0
    suma=0
    while i<n:
        wynik=1
        j=0
        while j<n:
            if j!=i:
                wynik=wynik*((punkt-a[j])/(a[i]-a[j]))
            j=j+1
        suma=suma+b[i]*wynik
        i=i+1
    return suma
def main():
    tabx=[]
    taby=[]
    wezly = int(input("Podaj liczbe węzłów: "))
    i=0
    print("Wypełnianie tabeli X")
    wypelnianieListy(tabx,wezly)
    print("Wypełnianie tabeli Y")
    wypelnianieListy(taby,wezly)
    punkt=float(input("Podaj punkt: "))
    print(check(tabx,wezly,punkt))
    print("Wynik:"+str(lagrange(tabx,taby,wezly,punkt)))


if __name__ == '__main__':
    main()
