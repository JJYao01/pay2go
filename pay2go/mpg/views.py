from django.http.response import HttpResponse
from django.shortcuts import render
import hashlib
import time

# Create your views here.
def main(request):
    print('main')
    return render(request, 'period/main.html', {})

def checkValue(request):
#m43Yy51kOifGzcYGTIvA6DCpiy3iE6K0
#HashIV=aNZJT03HjjnSvmzp
    hashKey = 'HashKey=m43Yy51kOifGzcYGTIvA6DCpiy3iE6K0'
    hashIV = 'HashIV=aNZJT03HjjnSvmzp'
    if request.is_ajax():
        request_data = request.POST        
        checkValue = hashKey +'&'+ request_data['checkValue']+'&TimeStamp='+ str(int(time.time())) +'&'+ hashIV        
        print(checkValue)
        encrypted = hashlib.sha256(bytes(checkValue, encoding="utf-8")).hexdigest()
        print(encrypted.upper())
       
        return HttpResponse(encrypted.upper())
    