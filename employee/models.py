from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    eaddress = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images',default="") 
    
  
    class Meta:  
        db_table = "employee"