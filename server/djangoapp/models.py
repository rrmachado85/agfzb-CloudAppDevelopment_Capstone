from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):

    name = models.CharField(null=False, max_length=30, default='ford')
    description = models.CharField(null=False, max_length=30, default='none')
    
    # Create a toString method for object string representation

    def __str__(self):
        return "Name: " + self.name + "," + \
                "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):

    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    TYPES_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]
    CMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    Name = models.CharField(null=False, max_length=30, default='ford')
    Dealer_id = models.IntegerField()
    Description = models.CharField(null=False, max_length=30, default='none')
    Type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPES_CHOICES,
        default=SEDAN
    )
    Year = models.DateField(null=True)
   
    # Create a toString method for object string representation
    def __str__(self):
         return "Name: " + self.Name + "," + \
                "Description: " + self.Description + ", " + \
                "Type: " + self.Type + ", " + \
                "Year: " + str(self.Year)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
