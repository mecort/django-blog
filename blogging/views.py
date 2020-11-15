from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)

# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)

class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    queryset = Post.objects.order_by('-published_date').exclude(published_date__exact=None)

class BlogDetailView(DetailView):
    # model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'

    # def get_queryset(self):
    #     self.published = get_object_or_404(Post.objects.filter(pk=post_id))
    #     # queryset = Post.objects.exclude(published_date__exact=None)
    #     return self.published
