from django.test import render
from . import forms

def index(request):
    return render(request, 'my_app/index.html')


def form_naem_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('Valid')
            print("NAME:" + form.cleaned_data['name'])
            print("EMAIL:" + form.cleaned_data['email'])
            print("TEXT:" + form.cleaned_data['text'])

    context = {'form': form}
    return render(request, 'my_app/form_page.html', context=context)