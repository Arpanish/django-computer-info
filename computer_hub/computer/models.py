from django.db import models


# Model without foreign key:ComputerBrand Model
class ComputerBrand(models.Model):
    brand_name = models.CharField(max_length=55)
    logo = models.ImageField(upload_to="computer/images")
    def __str__(self):
        return self.brand_name


# Model with foreignkey : ComputerSpecification Model
class ComputerSpecification(models.Model):
    generation = models.CharField(max_length=10)
    price_min  = models.IntegerField()
    price_max = models.IntegerField()
    ram = models.IntegerField()
    brand = models.ForeignKey(
        # """
        # It returns the brand name.
        # :return: The brand name
        # """
        'ComputerBrand',
        on_delete=models.CASCADE,)
    def __str__(self):
        return str(self.brand)

# Model with foreignkey : Computer Model
class Computer(models.Model):
    computer_code = models.CharField(max_length=20,unique=True)
    computer = models.ForeignKey(
        'ComputerSpecification',
        on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField()
    unit_rate = models.PositiveIntegerField()
    
    @property
    def total_price(self):
        total_price = self.quantity*self.unit_rate
        return total_price


