from django.shortcuts import render

# Create your views here.


def udfilter(request):
    
    data = 'Hi i aM sHUBhaM bHArTi'
    
    data2 = 'CuRrenTLy i AM pURsuINg pyTHoN FuLL-StacK deVEloPmEnT coURsE'
    
    data3 = 'ENGINEERING'
    
    return render(request, 'udfilter.html', {'data':data, 'data2':data2, 'data3':data3})