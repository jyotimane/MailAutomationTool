from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from packages.single_validation import single_validation_module
from packages.multiple_validation import multiple_validation_module


def emailvalidation(request):
    return render(request, 'emailvalidation.html')


def singlemailvalidation(request):
    single_validation_module(request)
    return render(request, 'emailvalidation.html', {'single_valid_mail': request.session['valid_mail']})


def multiplemailvalidation(request):
    multiple_validation_module(request)
    return render(request, 'emailvalidation.html', {'multiple_valid_mail': request.session['valid_mail']})


def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['document']
        if not csv_file.name.endswith('.csv'):
            return render(request, 'emailvalidation.html', {'invalidfileerror': "This file is invalid."})
            # messages.error(request, 'This is not a csv file.')
        print(csv_file.name)
        request.session['csvpath'] = csv_file.name
        fs = FileSystemStorage()
        fs.save(csv_file.name, csv_file)
    return render(request, 'emailvalidation.html')
