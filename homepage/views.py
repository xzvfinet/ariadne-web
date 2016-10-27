from django.shortcuts import render, HttpResponseRedirect
from .forms import PhotoUploadForm


def main(request):
    return render(request, 'index.html', {})


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = PhotoUploadForm()
    return render(request, 'upload.html', {'form': form})

