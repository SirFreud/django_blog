from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html',
        {
        'contact_info': [
        "If you would like to contact me, please email me", 
        "xsdf@example.com"
            ]
        }
)
# passing a dictionary with a list after content
