from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    queryset = Post.objects.order_by("-published_date").exclude(
        published_date__exact=None
    )


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


class LatestEntriesFeed(Feed):
    title = "Blog Posts"
    link = "/blogposts/"
    description = "Updates to Blog Posts"

    def items(self):
        return Post.objects.order_by("-published_date")

    def item_title(self, item):
        return Post.title

    def item_text(self, item):
        return Post.text

    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
