from .models import ContactUs

def contact_info(request):
    """
    Adds the last ContactUs record to every template.
    """
    contact = ContactUs.objects.last()  # get the latest record
    return {
        'contact_info': contact
    }