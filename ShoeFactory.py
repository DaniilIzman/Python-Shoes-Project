import SportShoeClass,CasualShoeClass,FormalShoeClass

class ShoeFactory:
    @staticmethod
    def create_shoe(material, color ,size ,brand ,season , gender, category):
        if category == "Sport":
            return SportShoeClass.SportShoe(material, color ,size ,brand ,season , gender)
        elif category == "Casual":
            return CasualShoeClass.CasualShoe(material, color ,size ,brand ,season , gender)
        elif category == "Formal":
            return FormalShoeClass.FormalShoe(material, color ,size ,brand ,season , gender)
        else:
            raise ValueError("Unknown material type.")