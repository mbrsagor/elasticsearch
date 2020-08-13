from django.shortcuts import render


def search(request):
    context = {
        'name': 'Mbr-Sagor'
    }
    template_name = 'search.html'
    return render(request, template_name, context)
