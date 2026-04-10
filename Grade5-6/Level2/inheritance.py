class Watermelon_slices:
    def __init__(self,shap,color):
        self.color=color
        self.shap=shap
    def area(self):
        pass
class Circular_slice (Watermelon_slices):
    def __init__(self, shap, color,raiduis):
        super().__init__("circle", color)
        self.raiduis=raiduis
    def area(self):
        return 3.14*self.raiduis**2
    print(Watermelon_slices)