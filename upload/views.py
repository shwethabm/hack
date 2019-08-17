from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

#@login_required
def upload(request):
    lastimage = Image.objects.last()
    imagefile = lastimage.imagefile
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context={
        'imagefile':imagefile,
        'form':form
    }
    return render(request, 'upload/upload.html',context)





