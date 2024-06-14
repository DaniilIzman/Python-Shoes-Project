from abc import ABC, abstractmethod

class Shoe(ABC):
    def __init__(self,material ,color ,size ,brand ,season , gender, category):
        self.material = material
        self.color = color
        self.size = size
        self.brand = brand
        self.season = season
        self.gender = gender
        self.category = category

    @abstractmethod
    def calculateCost(self):
        pass
    
    def newChoice(self, material_new ,color_new ,size_new ,brand_new ,season_new , gender_new):
        self.material = material_new
        self.color = color_new
        self.size = size_new
        self.brand = brand_new
        self.season = season_new
        self.gender = gender_new
        
    def display(self):
        print(f"Shoe Material: {self.material}, Shoe Color: {self.color} , Shoe Size: {self.size}, Shoe Brand: {self.brand}, Season: {self.season} , Gender: {self.gender}")
        