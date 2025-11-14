from django.shortcuts import render
from .models import Photo
# Create your views here.


def uploadImage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')

        Photo.objects.create(name=name, image=image)
    return render(request, 'base/upload_photo.html')


def getImages(request):
    photos = Photo.objects.all()
    return render(request, "base/gallery.html", {"photos": photos})
