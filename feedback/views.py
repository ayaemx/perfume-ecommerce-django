from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Feedback
from .forms import FeedbackForm

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'feedback/feedback_list.html'
    context_object_name = 'feedbacks'

class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback_form.html'
    success_url = reverse_lazy('feedback:list')
