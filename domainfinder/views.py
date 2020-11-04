from django.shortcuts import render

from packages.domainfinder import LinkedinDomainfinder
from createcontactlist.views import getExpObject


def domainfinder(request):
    return render(request, 'domainfinder.html')


def finddomains(request):
    # try:
    expObj = getExpObject(request)
    driver = expObj.getDriver()
    LinkedinDomainfinder(request, driver)
    return render(request, 'domainfinder.html', {'domain': "Ok"})
    # except Exception as e:
    # return render(request, 'domainfinder.html', {'domain': "Error"})
