from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from  .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView
# Create your views here.

class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    success_url = reverse_lazy("home")
    
    def get_success_url(self) -> str:
        messages.add_message(self.request,messages.SUCCESS, "Mesajiniz qebul edildi")
        return super().get_success_url()





@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")   
        else:
            return render(request, "main/contact.html",{'form': form})
             
    form = ContactForm()
    context = {
        "form":form
    }
    print(form)
    return render(request, "main/contact.html",context)






def home(request):
    text = "lorem .geldi getdi. baxdi gordu. qacdi ve .sonda hecne etmedi"
    return render(request, "main/index.html",{
        'text': text,
    })

def about(request):
    return render(request, "main/about.html")


# def home(request):
#     return render(request, "main/index.html")

# def home(request):
#     return render(request, "main/index.html")