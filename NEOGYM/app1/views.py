from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm
from django.shortcuts import redirect




class ContactView(TemplateView):
    template_name = "contact.html"

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success_url')
        
        return self.render_to_response({'form': form})



class TrainerView(TemplateView):
    template_name = "trainer.html"

class WhyView(TemplateView):
    template_name = "why.html"

class SuccessView(TemplateView):
    template_name = "success.html"

