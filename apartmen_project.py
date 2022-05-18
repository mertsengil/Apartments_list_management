def ekle():   
    apartman_ismi=input("Apartment name:")
    apartman_no=input("no:")
    apartman_city=input("city")
    apartman_fiyatı=input("price:")
    f = open("apartmanlar.txt","a")
    f.write(apartman_ismi+" "+apartman_no+" "+apartman_city+" "+apartman_fiyatı+"\n")
    f.close()
    
def cikar(apartman):
    f = open("apartmanlar.txt","r")
    lines = f.readlines()
    f.close()
    f = open("apartmanlar.txt","w")
    for line in lines:
        x= line.split(" ")
        if x[0]!=apartman:
            f.write(line)
    f.close()

print("""
1-)Insert an apartment
2-)Delete an apartment
3-)See all apartments
4-)Sort by alphabetically
5-)Sort by prices
""")

x = input("Select the action:")

if x == '1':
    ekle()
    
elif x == '2':
    apartman=input("Enter the name of the apartment:")
    cikar(apartman)
    
elif x == '3':
    f = open("apartmanlar.txt","r")
    x = f.readlines()
    f.close
    print("Name  No   City   Price")
    for i in x:
        print(i)
        
elif x == '4':
    with open("apartmanlar.txt", 'r') as f:
        l = [line for line in f if line.strip()]
        l.sort(key=lambda line:line.split()[0])
    with open("apartmanlar.txt", 'w') as f:
        for line in l:
            f.write(line)
            
elif x == '5':
    with open("apartmanlar.txt", 'r') as f:
        l = [line for line in f if line.strip()]
        l.sort(key=lambda line:line.split()[3])
    with open("apartmanlar.txt", 'w') as f:
        for line in l:
            f.write(line)
    
    
    
    
    

    
