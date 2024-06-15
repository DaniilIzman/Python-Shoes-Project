import ShoeClass, ShoePriceRegulation

class CasualShoe(ShoeClass.Shoe):
    def __init__(self,material ,color ,size ,brand ,season ,gender):
        super().__init__(material ,color ,size ,brand ,season ,gender, "Casual")

    def calculateCost(self):
        price = 0.3 * ShoePriceRegulation.ShowPriceRegulation.ShowPrice(self)
        return price
