class Car:
    def __init__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year
    def finish(self):
        return (f"Марка: {self.brand} "
                f"\nМодель: {self.model} "
                f"\nРік: {self.year}")
rezult = Car("Tesla" , "100D" , 2017)
print(rezult.finish())
