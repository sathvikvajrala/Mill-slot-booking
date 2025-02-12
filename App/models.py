# from django.db import models


# class District(models.Model):
#     district_name = models.CharField(max_length=150)

#     def __str__(self):
#         return self.district_name
    
# class Mandal(models.Model):
    
#     district_name = models.ForeignKey(District,on_delete=models.CASCADE)
#     mandal_name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.mandal_name
    
# class Mill(models.Model):
#     mill_name = models.CharField(max_length=150)
#     mill_no = models.IntegerField()
#     mill_owner_name = models.CharField(max_length=200)
#     mill_contact_number = models.IntegerField()
#     mill_address = models.TextField()
#     mill_details = models.TextField()
#     available_slots = models.IntegerField(default=0)

#     def __str__(self):
#         return self.mill_name



# from django.db import models

# class Country(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     name = models.CharField(max_length=50)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name


from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    mill_no = models.IntegerField(default=0,blank=True, null=True)
    mill_owner_name = models.CharField(max_length=200,blank=True, null=True)
    mill_contact_number = models.IntegerField(default=0,blank=True, null=True)
    mill_address = models.TextField()
    mill_details = models.TextField()
    available_slots = models.IntegerField(default=0,blank=True, null=True)
    def __str__(self):
        return self.name
    
class SlotBooking(models.Model):
    dist_name = models.CharField(max_length=200)
    mandal_name = models.CharField(max_length=200)
    # mill_name = models.CharField(max_length=200)
    # mill_id = models.IntegerField()
    