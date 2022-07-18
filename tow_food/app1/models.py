from unicodedata import category
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)
    category= models.CharField(max_length=500)
    perishable = models.BooleanField(default=False)
    weight = models.FloatField(default=0)

    def __str__(self):
        return "name:" + self.name + "barcode:" + self.barcode + "category:" + self.category + "perishable:" + str(self.perishable) + "weight:" + str(self.weight)  + "id:" + str(self.id) + "created_at:" + str(self.created_at) + "updated_at:" + str(self.updated_at)

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    addressFirstLine = models.CharField(max_length=500)
    ageGroup = models.CharField(max_length=100)
    ethnicity = models.CharField(max_length=100)
    postCode = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    email = models.EmailField(max_length=100)
    prefContact = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    isCarer = models.BooleanField(default=False)
    isMember = models.BooleanField(default=True)
    isEmployed = models.BooleanField(default=True)
    noAdults = models.IntegerField(default=0)
    noChildren = models.IntegerField(default=0)
    foodAllergies = models.CharField(max_length=300)
    prefLarder = models.CharField(max_length=100)
    acceptedPolicy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    totalFoodCollected = models.FloatField(default=0)
    baselineHealthScore = models.FloatField(default=0)
    currentHealthScore = models.FloatField(default=0)

    def __str__(self):
        return "firstName:" + self.firstName + "lastName:" + self.lastName + "addressFirstLine:" + self.addressFirstLine + "ageGroup:" + self.ageGroup + "ethnicity:" + self.ethnicity + "postCode:" + self.postCode + "phone_regex:" + self.phone_regex + "phone_number:" + self.phone_number + "email:" + self.email + "prefContact:" + self.prefContact + "occupation:" + self.occupation + "isCarer:" + str(self.isCarer) + "isMember:" + str(self.isMember) + "isEmployed:" + str(self.isEmployed) + "noAdults:" + str(self.noAdults) + "noChildren:" + str(self.noChildren) + "foodAllergies:" + self.foodAllergies + "prefLarder:" + self.prefLarder + "acceptedPolicy:" + str(self.acceptedPolicy) + "created_at:" + str(self.created_at) + "updated_at:" + str(self.updated_at) + "totalFoodCollected:" + str(self.totalFoodCollected) + "baselineHealthScore:" + str(self.baselineHealthScore) + "currentHealthScore:" + str(self.currentHealthScore)

class Volunteers(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    addressFirstLine = models.CharField(max_length=500)
    postCode = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "firstName:" + self.firstName + "lastName:" + self.lastName + "addressFirstLine:" + self.addressFirstLine + "postCode:" + self.postCode + "phone_regex:" + self.phone_regex + "phone_number:" + self.phone_number + "email:" + self.email + "password:" + self.password + "isAdmin:" + str(self.isAdmin) + "age:" + str(self.age) + "created_at:" + str(self.created_at)



