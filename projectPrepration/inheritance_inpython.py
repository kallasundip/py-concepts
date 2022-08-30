'''
    --- one class methods access like class benz_car(car)
    --- Inherite the properties from one class to another class
'''


class Cars:
    def engien(self):
        print("Engine with 1500 cc")

    def wheels(self):
        print("Li wheels")


class Maruthi(Cars):
    pass                        # pass in class becose Empty class not accept


class Swift(Cars):
    def tyres(self):
        print("MRF Tyres")

maruthi = Maruthi()
print(maruthi.engien())
swift = Swift()
print(swift.tyres())
