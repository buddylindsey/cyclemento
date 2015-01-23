class NextUrlMixin(object):
    def get_success_url(self):
        if 'next' in self.request.GET:
            return self.request.GET.get('next')
        return super(NextUrlMixin, self).get_success_url()
