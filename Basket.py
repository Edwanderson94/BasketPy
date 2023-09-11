from Product import Product
class Basket:
    products = []
    total =0

def main():
# Lista de produtos:
    p1 = Product("Rice", 29.35)
    p2 = Product("Bean", 7.99)
    p3 = Product("Noodle", 4.29)
    p4 = Product("Tomato Sauce", 3.49)
    p5 = Product("Grated Cheese", 6.99)
    p6 = Product("Farofa", 9.44)

#Soma dos produtos na cesta:
    b = Basket()
    b.products.append(p1)
    b.products.append(p2)
    b.products.append(p3)
    b.products.append(p4)
    b.products.append(p5)
    b.products.append(p6)
    print("*****Seus produtos são:*****")
    for item in b.products:
        print(item.name, item.price)
    print("*****Total a Pagar:*****")
    for item in b.products:
        b.total+=item.price
    print(f'R$ {b.total}')
main()