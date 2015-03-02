from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from contact.forms import FeedbackForm


class FeedbackView(FormView):
    template_name = 'contact/feedback.jinja'
    form_class = FeedbackForm
    success_url = reverse_lazy('feedback_thankyou')

    def form_valid(self, form):
        form.send_email()
        return super(FeedbackView, self).form_valid(form)


class ThankyouView(TemplateView):
    template_name = 'contact/thankyou.jinja'
