from django.shortcuts import render

# View to render the page with the button and count
def index(request):
    return render(request, 'index.html')