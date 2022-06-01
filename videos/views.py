from django.http import HttpResponse
from django.shortcuts import render
from .models import Video
import subprocess


# Create your views here.
def index(request):
    Videos = Video.objects.all()
    return render(request,'videos/index.html',context={"videos":Videos})


def device(request):
    
    device_def="""USB:

        USB 3.0 Bus:

        Host Controller Driver: AppleUSBXHCISPTLP
        PCI Device ID: 0x9d2f 
        PCI Revision ID: 0x0021 
        PCI Vendor ID: 0x8086 

        USB 3.1 Bus:

        Host Controller Driver: AppleUSBXHCIAR
        PCI Device ID: 0x15d4 
        PCI Revision ID: 0x0002 
        PCI Vendor ID: 0x8086 
        Bus Number: 0x00 

    """

    result = subprocess.run(["system_profiler", "SPUSBDataType"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    device_details=result.stdout
    
    if device_details==device_def:
        print("NO EXTERNAL DEVICE CONNECTED")
    else:
        print("EXTERNAL DEVICE DETECTED")

    return(HttpResponse("Hai"))    
