from django.shortcuts import render, redirect
from django.http import HttpResponse
from Indexos import templates
from django.contrib import messages
import pymysql.cursors

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        conn = pymysql.connect(host='indexos-1.c4zciaga036k.eu-west-3.rds.amazonaws.com',
                               user='admin',
                               password='cb2240_ED',
                               db='INDEXOS_TEST')
        try:
            with conn.cursor() as cursor:
                sql = "CREATE USER '" + request.POST['email'] + "'@% IDENTIFIED BY '" + request.POST['password'] + "'"
                sql2 = "INSERT INTO INDEXOS_USERS (USERNAME) VALUE (" + request.POST['email'] + ");"
                cursor.execute(sql)
                cursor.execute(sql2)
                result = cursor.fetchone()
                print(result)
        finally:
            conn.close()
        messages.success(request , 'the view works')
        print(request.POST['email'])
        print(request.POST['password'])
        print(request.POST['confirmation'])
        return redirect('../home')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        conn = pymysql.connect(host='indexos-1.c4zciaga036k.eu-west-3.rds.amazonaws.com',
                               user=request.POST['email'],
                               password=request.POST['password'],
                               db='information_schema')
        try:
            with conn.cursor() as cursor:
                print('it works !!')
        finally:
            conn.close()
        messages.success(request, 'the view works')
        print(request.POST['email'])
        print(request.POST['password'])
        return redirect('../home')
    return render(request, 'login.html')