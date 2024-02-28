from django.db import models


def generate_images_upload_path(instance, image):
    return f'files/images/{image}'


class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=generate_images_upload_path, blank=True, null=True)
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    patients = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    telegram_user = models.CharField(max_length=255, blank=True, null=True)
    about = models.TextField()

    def __str__(self):
        return self.full_name


class Region(models.Model):
    region_name = models.CharField(max_length=255)

    def __str__(self):
        return self.region_name


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField(null=True)
    image = models.ImageField(upload_to=generate_images_upload_path, blank=True, null=True)
    phone = models.CharField(max_length=15)
    category = models.CharField(null=True, max_length=200)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    full_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255, null=True)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return self.full_name


class Help(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
