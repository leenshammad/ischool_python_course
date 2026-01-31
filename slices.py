class Slices:
    def __init__(self,radrus):
        self.radrus=radrus
    def calculate_area(self):
        return 3.14*self.radrus**2
    def calculate_circum (self):
        
        return 2*3.14*self.radrus
watermelon_slice=Slices(7)
print(watermelon_slice.calculate_area())
print(watermelon_slice.calculate_circum())

        