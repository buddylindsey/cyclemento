from django.conf.urls import url, patterns

from contact.views import FeedbackView, ThankyouView

urlpatterns = patterns(
    '',
    url('^$', FeedbackView.as_view(), name='feedback'),
    url('^thankyou/$', ThankyouView.as_view(), name='feedback_thankyou'),
)
