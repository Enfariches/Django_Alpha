from django.shortcuts import render

def index_page(request):
    return render(request, 'main/index.html')

def exceltoexcel_page(request):
    return render(request, 'main/excelToExcel.html')

def wordtoexcel_page(request):
    return render(request, 'main/wordtoexcel.html')

def exceltojson_page(request):
    return render(request, 'main/exceltojson.html')
