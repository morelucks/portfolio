from django.shortcuts import render, redirect
from .forms import  ContactForm
from .models import Photo
# Create your views here.
def home(request):
  return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact instance and save it to the database
            contact = form.save()
            # You can add any additional logic here, such as sending email notifications
            return redirect('home')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
def photo(request):
    photos = Photo.objects.all()
    return render(request, 'photo.html', {'photos': photos})