from test.product import Product
"""In the product_repository.py file, the class ProductRepository should be implemented. 
It is a repository for all products that are delivered to the grocery shop.
The class should have products: list - an empty list, which will be containing all products (objects). 
Also, the class should have 4 additional methods:
•	add(product: Product) - adds a product to the repository
•	find(product_name: str) - returns a product (object) with that name
•	remove(product_name) - removes a product from the repository
•	__repr__() - override the method, so it returns information for all products in the repository: 
"{product_name1}: {quantity1}"
{product_name2}: {quantity2}
…
{product_nameN}: {quantityN}"
"""
class ProductRepository:
    def __init__(self):
        self.products=[] # store all products

    def add(self,product):# class Product) - adds a product to the repository
        self.products.append(product)

    def find(self,product_name: str): # - returns a product (object) with that name
        for each_product in self.products:
            if product_name==each_product.username:
                return each_product

    def remove(self,product_name): # - removes a product from the repository
        for each_product in self.products:
            if each_product.username==product_name:
                self.products.remove(each_product)
                break

    def __repr__(self):
        result=""
        for index in range(len(self.products)):
            """ VERY IMPORTANT PRINTING WITHOUT EMPTY ROW IN THE END"""
            if index<len(self.products)-1:
                result+= f"{self.products[index].username}: {self.products[index].quantity}\n" # {product_name1}: {quantity1}"
            else:
                result += f"{self.products[index].username}: {self.products[index].quantity}"

        return result

