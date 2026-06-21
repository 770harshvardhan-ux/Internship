from dmart import dmart
class clothes(dmart):
    def __init__(self,category,product_name,qty,price,colour,size):
        super().__init__(category,product_name,qty,price)
        self.colour=colour
        self.size=size

    def display_clothes_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f"category:{self.colour}\nsize{self.size}"