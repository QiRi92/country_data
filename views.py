from django.shortcuts import render
from App.models import Directory
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django_countries import countries
import pandas as pd
from datetime import datetime
from plotly.offline import plot
from plotly.graph_objs import Scatter

def format(request):
    return render(request, "format.html")

def graph(request, directory_id):
    try:
        directory = Directory.objects.get(id = directory_id)
        try:
            #Get all headers except "Name"
            df1 = directory.eachtable.loc[:, directory.eachtable.columns != "NAME"]
            variablelist = list(df1)
            #Get all date into a list
            df4 = directory.eachtable.iloc[:, 0]
            del df4[0]
            df8 = list(df4)
            if type(df8[0]) == str:
                try:
                    df9 = []
                    for x in df8:
                        x=x[:10]
                        date_obj = datetime.strptime(x, "%d/%m/%Y").date()
                        df9.append(date_obj)
                    x_data = df9
                except:
                    errortext = "Data Table Datetime Error"
                    return render(request, "error.html", context={"error_text":errortext})
            else:
                x_data = df8
            tajuk = request.GET['topics']
            df5 = directory.eachtable.get([tajuk])
            if df5 is not None:
                unit = str(df5.iloc[0, 0])
                df6 = df5.drop(df5.index[0])
                row_list = df6.iloc[:, 0].values.flatten().tolist()
                y_data = row_list
                yframe = y_data
                y_data = []
                for x in yframe:
                    try:
                        y_data.append(float(x))
                    except:
                        y_data.append(x)
                plot_div = plot([Scatter(x=x_data, y=y_data,
                                mode='lines', name='test',
                                opacity=0.8, marker_color='green')],
                    output_type='div')
                return render(request, "line.html", context={'plot_div': plot_div, "variable_list":variablelist, "tajuk_nama":tajuk, "unit_nama":unit})
            else:
                tajuk = None
                return render(request, "line.html", context={"variable_list":variablelist, "tajuk_nama":tajuk, "directoryid":directory_id})
        except:
            errortext = "Data Table Not Found"
            return render(request, "error.html", context={"error_text":errortext})
    except:
        errortext = "Directory Not Found"
        return render(request, "error.html", context={"error_text":errortext})

def line(request, directory_id):
    try:
        directory = Directory.objects.get(id = directory_id)
        try:
            #Get all headers except "Name"
            df1 = directory.eachtable.loc[:, directory.eachtable.columns != "NAME"]
            variablelist = list(df1)
            
            #Get all data values based on column name
            if request.method=="POST":
                tajuk = str(request.GET['topics'])
                df5 = directory.eachtable.get([tajuk])
                df6 = directory.eachtable.iloc[:, 1]
                del df6[0]
                df7 = list(df6)
                y_data = df7
            else:
                tajuk = None
                y_data = None
                x_data = None

            if y_data is not None:
                plot_div = plot([Scatter(x=x_data, y=y_data,
                                mode='lines', name='test',
                                opacity=0.8, marker_color='green')],
                    output_type='div')
                return render(request, "line.html", context={'plot_div': plot_div, "variable_list":variablelist, "tajuk_nama":tajuk, "directoryid":directory_id})
            else:
                return render(request, "line.html", context={"variable_list":variablelist, "tajuk_nama":tajuk, "directoryid":directory_id})
        except:
            errortext = "Data Table Not Found"
            return render(request, "error.html", context={"error_text":errortext})
    except:
        errortext = "Directory Not Found"
        return render(request, "error.html", context={"error_text":errortext})

# Create your views here.
def home(request):
    directory_list = Directory.objects.all()
    country_list = []
    for code, name in list(countries):
        country_list += [name]
    return render(request, "home.html", {"directorys":directory_list, "countries":country_list})

# Function to ADD 
def add_directory(request):
    if request.method=="POST":
        if request.POST.get('link') \
            and request.POST.get('country') \
            and request.POST.get('periodic') \
            and request.POST.get('topics') \
            and request.POST.get('last_update') \
            or request.POST.get('next_release') \
            or request.POST.get('getfile') \
            or request.POST.get('comments'):
            directory = Directory()
            directory.link = request.POST.get('link')
            directory.country = request.POST.get('country')
            directory.periodic = request.POST.get('periodic')
            directory.topics = request.POST.get('topics')
            directory.last_update = request.POST.get('last_update')
            directory.next_release = request.POST.get('next_release')
            #directory.getfile = request.POST.get('getfile')
            directory.comments = request.POST.get('comments')
            if 'getfile' in request.FILES:
                myfile = request.FILES['getfile']
                filetype = str(myfile.name.split('.')[-1])
                if filetype == "xlsx" or filetype == "xls": 
                    data = pd.read_excel(myfile)
                    firsttable = pd.DataFrame(data)
                    if firsttable.iloc[0,0] == "UNIT" and firsttable.columns[0] == "NAME":
                        directory.eachtable = pd.DataFrame(data)
                        directory.filepresent = "YES"
                    else:
                        directory.filepresent = "NO"
                elif filetype == "csv":
                    data = pd.read_csv(myfile)
                    firsttable = pd.DataFrame(data)
                    if firsttable.iloc[0,0] == "UNIT" and firsttable.columns[0] == "NAME":
                        directory.eachtable = pd.DataFrame(data)
                        directory.filepresent = "YES"
                    else:
                        directory.filepresent = "NO"
                else:
                    directory.filepresent = "NO"
            else:
                directory.filepresent = "NO"
            directory.save()
            messages.success(request, "Directory added successfully !")
            return HttpResponseRedirect("/")
    else:
            return render(request, 'add.html')

# Function to View directory data individually
def directory(request, directory_id):
    directory = Directory.objects.get(id = directory_id)
    if directory != None:
        return render(request, "edit.html", {'directory':directory})

# Function to Edit 
def edit_directory(request):
    if request.method == "POST":
        directory = Directory.objects.get(id = request.POST.get('id'))
        if directory!= None:
            directory.link = request.POST.get('link')
            directory.country = request.POST.get('country')
            directory.periodic = request.POST.get('periodic')
            directory.topics = request.POST.get('topics')
            directory.last_update1 = request.POST.get('last_update')
            directory.next_release = request.POST.get('next_release')
            directory.comments = request.POST.get('comments')
            if 'getfile' in request.FILES:
                myfile = request.FILES['getfile']
                filetype = str(myfile.name.split('.')[-1])
                if filetype == "xlsx" or filetype == "xls" or filetype == "csv": 
                    data = pd.read_excel(myfile)
                    newtable = pd.DataFrame(data)
                    if newtable.iloc[0,0] == "UNIT" and newtable.columns[0] == "NAME":
                        directory.eachtable = pd.DataFrame(data)
                        directory.filepresent = "YES"
            directory.save()
            messages.success(request, "Directory Updated successfully !")
            return HttpResponseRedirect("/")

# Function to Delete employee
def delete_directory(request, directory_id):
    directory = Directory.objects.get(id = directory_id)
    directory.delete()
    messages.success(request, "Directory deleted successfully !")
    return HttpResponseRedirect("/")
