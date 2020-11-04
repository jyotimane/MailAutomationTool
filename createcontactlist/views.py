from django.shortcuts import render
from selenium import webdriver
from packages.loginlinkedin import LoginWithLinkedIn
from packages.applyfilter import FetchLink
from packages.linkedinDataScrap import ScrapData
from packages.ccl_downloads import downloadScrapData
import packages
from pymongo import MongoClient
import csv
from .models import CreateContactListData
from urllib.request import urlretrieve as retrieve 

Fname=[]
Lname=[]
Location=[]
Designation=[]
CompName=[]
expObj = packages.exponentialxClass()


def getExpObject(request):
    return expObj


def createcontactlist(request):
    return render(request, 'createcontactlist.html')


def loginlinkedin(request):
    try:
        # this line opening the new browser window and
        # returning us webdriver object named as driver
        driver = webdriver.Firefox(executable_path = "C:/Users/jyoti/Desktop/run_script/geckodriver.exe")
        # setting driver for each current user
        expObj.setDriver(driver)
        LoginWithLinkedIn(request, driver)
    except Exception as e:
        return render(request, 'createcontactlist.html', {'username': "Error"})
    else:
        return render(request, 'createcontactlist.html', {'username': request.session["username"]})


def applyfilter(request):
    try:
        driver = expObj.getDriver()
        # After filter applying, fetch this link to scrap data
        FetchLink(driver)
    except Exception as e:
        return render(request, 'createcontactlist.html', {'filterapplied': "Error"})
    else:
        return render(request, 'createcontactlist.html', {'filterapplied': "Filter is Applied"})


def linkedindatascrap(request):
    try:
        # get current instance of driver
        driver = expObj.getDriver()
        # scrap the data and pass it to database
        ScrapData(request, driver)
        PassDataToMongoDB(request,driver)
        out='Scrapping Done'
    except Exception as e:
        return render(request, 'createcontactlist.html', {'scrapped': "Error"})
    else:
        # closing the window of browser
        driver.quit()
        return render(request, 'createcontactlist.html', {'scrapped': "Data Scrapped", 'datadict': out})


def datascrapeddwnld(request):
    try:
        #ccl_data = request.session['ccl_data']
        # We will download the csv file
        #ccl_data = downloadScrapData(ccl_data)
        url='C:/Users/jyoti/Desktop/exponentialxApp9/exponentialxApp/Downloads'
        

    except Exception as e:
        return render(request, 'createcontactlist.html', {'dwnldscrapdata': "Error"})
    else:
        return render(request, 'createcontactlist.html', {'dwnldscrapdata': "CSV Downloaded", 'ccl_data': retrieve(url,'contactlist.csv')})

def PassDataToMongoDB(request,driver):
        Fname=request.session['ccl_data'].get('fname')
        Lname=request.session['ccl_data'].get('lname')
        Location=request.session['ccl_data'].get('location')
        Designation=request.session['ccl_data'].get('designation')
        CompName=request.session['ccl_data'].get('compName')
        i=0
        j=0
        delete_data()
        for i in range(len(Fname)):
            fn=Fname[i]
            ln=Lname[i]
            loc=Location[i]
            deg=Designation[i]
            com=CompName[i]
            reg=CreateContactListData(id=j,fname=fn,lname=ln,location=loc,designation=deg,compName=com)
            reg.save()
            j=j+1
        getDataInCSV()

def delete_data():
    user=CreateContactListData.objects.all()
    user.delete()
    print("\n\n****PreviousData successfully Deleted and new data will added in file******\n")

def getDataInCSV():
    csvFile=open('C:/Users/jyoti/Desktop/exponentialxApp9/exponentialxApp/Downloads/contactlist.csv','w+',newline='')
    try:
        writer=csv.writer(csvFile)
        writer.writerow(('FirstName'," ",'LastName'," ",'Location'," ",'Designation'," ",'CompanyName'))
        info=CreateContactListData.objects.all()
        for i in info:
            writer.writerow((i.fname," ",i.lname," ",i.location," ",i.designation," ",i.compName))
            continue 
    finally:
        csvFile.close()



