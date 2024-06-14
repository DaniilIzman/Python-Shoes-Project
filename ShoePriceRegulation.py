import ShoeClass

class ShowPriceRegulation():
    @staticmethod
    def ShowPrice(shoe):
        price = 1
        
        if (shoe.brand == "Nike"):
            price = price * 2.5
        elif (shoe.brand == "Gucci"):
            price = price * 5
        elif (shoe.brand == "Clarks"): 
            price = price * 7.5
            
        if (shoe.material == "Skin"):
            price = price * 2
        elif (shoe.material == "Synthetic"):
            price = price * 1.1
        elif (shoe.material == "Rubber"):
            price = price * 0.8
        
        price = price * 10 * shoe.size
        
        return price