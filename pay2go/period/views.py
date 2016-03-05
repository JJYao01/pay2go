import datetime
import hashlib
import time

from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, 'period/main.html', {})

def checkValue(request):
#m43Yy51kOifGzcYGTIvA6DCpiy3iE6K0
#HashIV=aNZJT03HjjnSvmzp
#+'&TimeStamp='+ timeStamp
    hashKey = 'HashKey=m43Yy51kOifGzcYGTIvA6DCpiy3iE6K0'
    hashIV = 'HashIV=aNZJT03HjjnSvmzp'
    if request.is_ajax():
        request_data = request.POST        
        #datetimeNow=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')        
        #timeStamp=str(int(time.mktime(time.strptime(datetimeNow, '%Y-%m-%d %H:%M:%S'))))      
        checkValue = hashKey +'&'+ request_data['checkValue'] +'&'+ hashIV        
        encrypted = hashlib.sha256(bytes(checkValue, encoding="utf-8")).hexdigest()       
        return HttpResponse(encrypted.upper())
    
def receive(request):
    if request['Status'] == 'SUCCESS':
        print(request)
    return render(request, 'period/main.html', {})