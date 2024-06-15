import ShoeClass, ShoePriceRegulation

class FormalShoe(ShoeClass.Shoe):
    def __init__(self,material ,color ,size ,brand ,season ,gender):
        super().__init__(material ,color ,size ,brand ,season ,gender, "Formal")

    def calculateCost(self):
        price = 0.8 * ShoePriceRegulation.ShowPriceRegulation.ShowPrice(self)
        return price
