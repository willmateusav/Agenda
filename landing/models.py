from django.db import models

class Visit(models.Model):

    ip_address_V = models.GenericIPAddressField(null=True)
    visit_day = models.DateTimeField(auto_now_add=True)
    location_country = models.CharField(max_length=30, db_index=True)
    location_city = models.CharField(max_length=30, db_index=True)
    device_type = models.CharField(max_length=20, blank=True)
    browser_type = models.CharField(max_length=50, blank=True)
    browser_version = models.CharField(max_length=64, db_index=True)
    os_type = models.CharField(max_length=50, blank=True)
    os_version = models.CharField(max_length=64, db_index=True)

class appointment(models.Model):

    HOUR = (
        ('', 'Seleccione horario'),
        ('9-10', '9-10'),
        ('10-11', '10-11'),
        ('11-12', '11-12'),
        ('12-13', '12-13'),
        ('14-15', '14-15'),
        ('15-16', '15-16'),
        ('16-17', '16-17'),
        ('17-18', '17-18'),
        ('18-19', '18-19'),
    )

    DAY = (
        ('', 'Seleccione el día'),
        ('23 de febrero', '23 de febrero'),
        ('24 de febrero', '24 de febrero'),
    )

    first_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254)
    date = models.CharField(max_length=15, choices=DAY)
    hour = models.CharField(max_length=10, choices=HOUR, default = None, null=True)
    all_is_accurate = models.BooleanField()