import ShoeClass, ShoePriceRegulation

class SportShoe(ShoeClass.Shoe):
    def __init__(self,material ,color ,size ,brand ,season ,gender):
        super().__init__(material ,color ,size ,brand ,season ,gender, "Sport")

    def calculateCost(self):
        price = 0.5 * ShoePriceRegulation.ShowPriceRegulation.ShowPrice(self)
        return price