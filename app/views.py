from django.shortcuts import render


#def addLocation(request):
#    permission_c
def map(request):
    return render(request,"map.html")


#Add Retruive Public Key based On jwt