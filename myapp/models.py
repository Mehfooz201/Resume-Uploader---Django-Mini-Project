from django.db import models

# Create your models here.

# STATE_CHOICE =(
#     ('Karachi', 'Malir', "East Karachi", 'South Karachi', 'West Karachi', 'Central karachi'),
#     ('Hyderabad', 'Hyderabad'),
#     ('Jamshoro', 'Jamshoro'),
#     ('Ghotki', 'Ghotki'),
#     ('Sukkur', 'Sukkur'),
#     ('Lahore', 'Lahore'),
#     ('Multan', 'Multan'),
#     ('Rahim Yar Khan', 'Rahim Yar Khan'),
#     ('Sadiqabad', 'Sadiqabad'),
#     ('Peshawar', 'Peshawar'),
#     ('Dera Ghazi Khan', 'Dera Ghazi Khan'),
#     ('Quetta', 'Quetta'),
#     ('Khuzdar', 'Khuzdar'),
#     ('Naushahro Feroze', 'Naushahro Feroze'),
#     ('Shaheed Benazirabad', 'Shaheed Benazirabad'),
#     ('Rawalpindi', 'Rawalpindi'),
#     ('Faisalabad', 'Faisalabad'),
#     ('Islamabad', 'Islamabad'),
#     ('Thatta', 'Thatta'),
# )

STATE_CHOICE = (
    ('Karachi','Karachi'),
    ('Hyderabad', 'Hyderabad'),
    ('Jamshoro', 'Jamshoro'),
    ('Ghotki', 'Ghotki'),
    ('Sukkur', 'Sukkur'),
    ('Lahore', 'Lahore'),
    ('Multan', 'Multan'),
    ('Rahim Yar Khan', 'Rahim Yar Khan'),
    ('Sadiqabad', 'Sadiqabad'),
    ('Peshawar', 'Peshawar'),
    ('Dera Ghazi Khan', 'Dera Ghazi Khan'),
    ('Quetta', 'Quetta'),
    ('Khuzdar', 'Khuzdar'),
    ('Naushahro Feroze', 'Naushahro Feroze'),
    ('Shaheed Benazirabad', 'Shaheed Benazirabad'),
    ('Rawalpindi', 'Rawalpindi'),
    ('Faisalabad', 'Faisalabad'),
    ('Islamabad', 'Islamabad'),
    ('Thatta', 'Thatta'),
)




class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveBigIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    mobile = models.PositiveBigIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)
