from django.shortcuts import render,HttpResponse,HttpResponseRedirect

def checkout(request):
    return HttpResponse("Payment is being processing please wait for it ....")
    # return HttpResponseRedirect("/")