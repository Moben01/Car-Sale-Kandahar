from .models import *
from products.models import NewCar

def contact_info(request):
    """
    Adds the last ContactUs record to every template.
    """
    contact = ContactUs.objects.last()  # get the latest record
    social = SocialMedia.objects.last()  # get the latest record

    car_count = 0
    if request.user.is_authenticated:
        car_count = NewCar.objects.filter(user=request.user).count()

    return {
        'contact_info': contact,
        'social_media': social,
        'car_count': car_count,
    }