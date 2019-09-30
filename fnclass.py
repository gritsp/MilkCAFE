#menu get name and price
class Product:
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price    

class Order:
    def __init__(self,id,name,price,amount):
        self.id = id
        self.name = name
        self.price = price    
        self.amount = amount
    
class menuOrder:
    def __init__(self):
        self.order = None

    def push(self,id,name,price,amount):
        datafile = open("order.txt","a")
        datafile.write(id+" "+name+" "+price+" "+amount+"\n")
    
    def showdata(self):
        datafile = open("order.txt","r")
        show = []
        for line in datafile:
            data = line.split()
            order = Order(data[0],data[1],data[2],data[3])
            show.append(order)
        return show
    
    def delete(self,id):
        f = open("order.txt","r")
        lines = f.readlines()
        f.close()
        f = open("order.txt","w")
        for line in lines:
            if line.split()[0]!=id:
                f.write(line)
    
    def clear(self):
        open("order.txt","w").close()
        


class Menu:
    def __init__(self):
        self.product = None
    
    def push(self,id,name,price,files):        
        datafile = open(files+".txt","a")
        datafile.write(id+" " + name+" "+str(price)+"\n")
    
    def showdata(self,files):
        datafile = open(files+".txt","r")
        show = []
        for line in datafile:
            data = line.split()
            prod = Product(data[0],data[1],data[2])
            show.append(prod)
        return show
    
    def search(self,id,files):
        datafile = open(files+".txt","r")
        for line in datafile:
            data = line.split()
            if data[0] == id:
                return Product(data[0],data[1],data[2])

    def delete(self,id,files):
        f = open(files+".txt","r")
        lines = f.readlines()
        f.close()
        f = open(files+".txt","w")
        for line in lines:
            if line.split()[0]!=id:
                f.write(line)
    
    def checkfile(self,files):
        datafile = open(files+".txt","r")
        for line in datafile:
            data = line.split()
            if (data[0] == "\n"):
                return None

#order get order.menu and amount


# a = Menu()
# # a.push("milk",30,"menu")
# a.delet("milk","menu")
# b = a.showdata("menu")

# print(b)
