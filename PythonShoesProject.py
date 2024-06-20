import ShoeClass, SportShoeClass , CasualShoeClass , FormalShoeClass , ShoeCollectionClass
from ShoeFactory import ShoeFactory

SportShoe = SportShoeClass.SportShoe("Rubber","red",40,"Nike","Summer","Male")
SportShoe.display()
print("Price:",SportShoe.calculateCost())
SportShoe.newChoice("Skin","black",30,"Nike","Spring","Female")
print("New choice for Sport Shoe:")
SportShoe.display()
print("Price:",SportShoe.calculateCost())
FabricSportShoe = ShoeFactory.create_shoe("Synthetic","yellow",28,"Nike","Spring","Male", category = "Sport")
print("Sport Shoe created by factory:")
FabricSportShoe.display()
print("Price:",FabricSportShoe.calculateCost(),"\n")

CasualShoe = CasualShoeClass.CasualShoe("Synthetic","black",35,"Gucci","Spring","Female")
CasualShoe.display()
print("Price:",CasualShoe.calculateCost())
CasualShoe.newChoice("Rubber","black",21,"Gucci","Winter","Male")
print("New choice for Casual Shoe:")
CasualShoe.display()
print("Price:",CasualShoe.calculateCost()) 
FabricCasualShoe = ShoeFactory.create_shoe("Skin","pink",33,"Gucci","Summer","Female", category = "Casual")
print("Casual Shoe created by factory:")
FabricCasualShoe.display()
print("Price:",FabricCasualShoe.calculateCost(),"\n")

FormalShoe = FormalShoeClass.FormalShoe("Skin","brown",42,"Clarks","Winter","Male")
FormalShoe.display()
print("Price:",FormalShoe.calculateCost())
FormalShoe.newChoice("Synthetic","grey",37,"Clarks","Spring","Female")
print("New choice for Casual Shoe:")
FormalShoe.display()
print("Price:",FormalShoe.calculateCost())
FabricFormalShoe = ShoeFactory.create_shoe("Synthetic","grey",41,"Clarks","Winter","Male", category = "Formal")
print("Formal Shoe created by factory:")
FabricFormalShoe.display()
print("Price:",FabricFormalShoe.calculateCost(),"\n")

shoeCollection = ShoeCollectionClass.ShoeCollectionClass()
shoeCollection.add(SportShoe)
shoeCollection.add(FabricSportShoe)
shoeCollection.add(CasualShoe)
shoeCollection.add(FabricCasualShoe)
shoeCollection.add(FormalShoe)
shoeCollection.add(FabricFormalShoe)

for i in range(shoeCollection.size()):
    print("Instance",i + 1,"in Shoe Collection: ")
    shoeCollection.get(i).display()
print("")
shoeCollection.printCollection()

print("Number of Sport Shoe",shoeCollection.size())

import unittest

class TestShoeClasses(unittest.TestCase):
    def setUp(self):
        self.sport_shoe = SportShoeClass.SportShoe("Skin","green",28,"Nike","Spring","Male")
        self.casual_shoe = CasualShoeClass.CasualShoe("Synthetic","lime",31,"Gucci","Spring","Female")
        self.formal_shoe = FormalShoeClass.FormalShoe("Rubber","brown",39,"Clarks","Autumn","Male")
        self.collection = ShoeCollectionClass.ShoeCollectionClass()
        self.collection.add(self.sport_shoe)
        self.collection.add(self.casual_shoe)
        self.collection.add(self.formal_shoe)
        
    def test_initialization(self):
        self.assertEqual(self.sport_shoe.material, "Skin")
        self.assertEqual(self.sport_shoe.color, "green")
        self.assertEqual(self.sport_shoe.size, 28)
        self.assertEqual(self.sport_shoe.brand, "Nike")
        self.assertEqual(self.sport_shoe.season, "Spring")
        self.assertEqual(self.sport_shoe.gender, "Male")

        self.assertEqual(self.casual_shoe.material, "Synthetic")
        self.assertEqual(self.casual_shoe.color, "lime")
        self.assertEqual(self.casual_shoe.size, 31)
        self.assertEqual(self.casual_shoe.brand, "Gucci")
        self.assertEqual(self.casual_shoe.season, "Spring")
        self.assertEqual(self.casual_shoe.gender, "Female")

        self.assertEqual(self.formal_shoe.material, "Rubber")
        self.assertEqual(self.formal_shoe.color, "brown")
        self.assertEqual(self.formal_shoe.size, 39)
        self.assertEqual(self.formal_shoe.brand, "Clarks")
        self.assertEqual(self.formal_shoe.season, "Autumn")
        self.assertEqual(self.formal_shoe.gender, "Male")
        
    def test_calculateCost(self):
        self.assertEqual(self.sport_shoe.calculateCost(), 700)
        self.assertEqual(self.casual_shoe.calculateCost(), 511.5)
        self.assertEqual(self.formal_shoe.calculateCost(), 1872)

    def test_display(self):
        from io import StringIO
        import sys

        capturedOutput = StringIO()                  
        sys.stdout = capturedOutput                   
        self.sport_shoe.display()
        self.casual_shoe.display()  
        self.formal_shoe.display()  
        sys.stdout = sys.stdout                  
        
        self.assertIn("Skin", capturedOutput.getvalue())
        self.assertIn("green", capturedOutput.getvalue())
        self.assertIn("28", capturedOutput.getvalue())
        self.assertIn("Nike", capturedOutput.getvalue())
        self.assertIn("Spring", capturedOutput.getvalue())
        self.assertIn("Male", capturedOutput.getvalue())
        
        self.assertIn("Synthetic", capturedOutput.getvalue())
        self.assertIn("lime", capturedOutput.getvalue())
        self.assertIn("31", capturedOutput.getvalue())
        self.assertIn("Gucci", capturedOutput.getvalue())
        self.assertIn("Spring", capturedOutput.getvalue())
        self.assertIn("Female", capturedOutput.getvalue())
        
        self.assertIn("Rubber", capturedOutput.getvalue())
        self.assertIn("brown", capturedOutput.getvalue())
        self.assertIn("39", capturedOutput.getvalue())
        self.assertIn("Clarks", capturedOutput.getvalue())
        self.assertIn("Autumn", capturedOutput.getvalue())
        self.assertIn("Male", capturedOutput.getvalue())

    def test_collection(self):
        self.assertEqual(3,self.collection.size())
        self.assertEqual(self.sport_shoe,self.collection.get(0))
        self.assertEqual(self.casual_shoe,self.collection.get(1))
        self.assertEqual(self.formal_shoe,self.collection.get(2))
        
    def test_display_collection(self):
        from io import StringIO
        import sys

        capturedOutput = StringIO()                  
        sys.stdout = capturedOutput                   
        self.collection.printCollection()
        sys.stdout = sys.stdout
        
        self.assertIn("Skin", capturedOutput.getvalue())
        self.assertIn("green", capturedOutput.getvalue())
        self.assertIn("28", capturedOutput.getvalue())
        self.assertIn("Nike", capturedOutput.getvalue())
        self.assertIn("Spring", capturedOutput.getvalue())
        self.assertIn("Male", capturedOutput.getvalue())
        
        self.assertIn("Synthetic", capturedOutput.getvalue())
        self.assertIn("lime", capturedOutput.getvalue())
        self.assertIn("31", capturedOutput.getvalue())
        self.assertIn("Gucci", capturedOutput.getvalue())
        self.assertIn("Spring", capturedOutput.getvalue())
        self.assertIn("Female", capturedOutput.getvalue())
        
        self.assertIn("Rubber", capturedOutput.getvalue())
        self.assertIn("brown", capturedOutput.getvalue())
        self.assertIn("39", capturedOutput.getvalue())
        self.assertIn("Clarks", capturedOutput.getvalue())
        self.assertIn("Autumn", capturedOutput.getvalue())
        self.assertIn("Male", capturedOutput.getvalue())
        
unittest.main()
    