import datetime
import hashlib
import time

from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def main(request):
    print('mpg/main')
    return render(request, 'mpg/main.html', {})

def checkValue(request):
#m43Yy51kOifGzcYGTIvA6DCpiy3iE6K0
#HashIV=aNZJT03HjjnSvmzp
#+ str(int(time.time()))
    hashKey = 'HashKey=m43Yy51kOifGzcYGTIvA6DCpiy3iE6K0'
    hashIV = 'HashIV=aNZJT03HjjnSvmzp'
    if request.is_ajax():
        request_data = request.POST   
        datetimeNow=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')        
        TimeStamp=str(int(time.mktime(time.strptime(datetimeNow, '%Y-%m-%d %H:%M:%S'))))     
        checkValue = hashKey +'&'+ request_data['checkValue']+'&TimeStamp='+TimeStamp +'&Version=1.1&'+ hashIV        
        print(checkValue)
        encrypted = hashlib.sha256(bytes(checkValue, encoding="utf-8")).hexdigest()
        print(encrypted.upper())       
        return HttpResponse(encrypted.upper())
    
    #841F57D750FB4B04B62DDC3ECDC26F1F4028410927DD28BD5B2E34791CC434D2
    #841F57D750FB4B04B62DDC3ECDC26F1F4028410927DD28BD5B2E34791CC434D2
    #1400137200
    #1400137200