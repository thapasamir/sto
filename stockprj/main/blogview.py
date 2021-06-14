from django.views.generic import ListView,DetailView
from .models import New
from django.shortcuts import get_object_or_404
from django.db.models import Q


class NewsView(ListView):
    template_name = 'news/index.html'
    queryset = New.Post.all()
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = super(NewsView, self).get_queryset()
        query = self.request.GET.get('search')
        if query is None:
            return queryset
        queryset = New.objects.filter(
            Q(title__icontains=query) | Q(post__icontains=query)
        )

        return queryset



class NewsDetail(DetailView):
    template_name = "news/news_detail.html"
    model = New
    context_object_name = 'posts'

