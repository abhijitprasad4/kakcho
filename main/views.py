from ast import FormattedValue
import csv
from random import sample
import re
from django.shortcuts import render
from django.http import HttpResponse 

def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
        response = HttpResponse('Upload your file here ')
    response = HttpResponse('Please log in first')
    return response

def edited(request):
    if request.user.is_authenticated and request.method == 'POST':
        import pandas as pd
        file = request.FILES['csvfile']
        # .roundoff
        df = pd.read_csv(file)
        df["Rating Roundoff"] = round(df["Rating"])
        df.to_csv('templates/roundoff.csv')

        # free
        df = pd.read_csv('templates/roundoff.csv')
        free = df[(df['Type'] == "Free")]
        free.to_csv('templates/free.csv')
        # paid
        df = pd.read_csv('templates/roundoff.csv')
        paid = df[(df['Type'] == "Paid")]
        paid.to_csv('templates/paid.csv')

        df = pd.read_csv('templates/roundoff.csv')
        # content rating
        dict = {}
        for row in df.itertuples():
            if row[10] not in dict:
                dict[row[10]] = 1

        for keys in dict.keys():
            # print(keys)
            df = pd.read_csv('templates/roundoff.csv')
            key = df[(df['Content Rating'] == keys)]
            key.to_csv('templates/'+str(keys)+'.csv')

        return render(request,"edited.html",{"csvfile" : file})
    response = HttpResponse('Please log in first')
    return response