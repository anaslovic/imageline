from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from portfolioapp.models import Portfolio, Photo, Category, Like, Comment
from .forms import AddPhotoForm, EditPhotoForm, UpdatePortfolioInfoForm, AddCommentForm
from next_prev import next_or_prev_in_order
from django.db.models import Q


class HomeView (TemplateView):

    template_name = 'home.html'


class DiscoverPhotosView (ListView):

    template_name = 'discover-photos.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        category_list = Category.objects.all
        context['categories'] = category_list
        return context


class DiscoverArtistsView (ListView):

    template_name = 'discover-artists.html'
    model = Portfolio


class PortfolioDetailView (DetailView):

    model = Portfolio
    template_name = 'portfolio-detail.html'


class UpdatePortfolioView(UpdateView):
    model = Portfolio
    form_class = UpdatePortfolioInfoForm
    template_name = 'edit-portfolio.html'


class DiscoverPhotoDetailView (DetailView):

    model = Photo
    template_name = 'discover-photo-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        qs = Photo.objects.all()
        prev_ph = next_or_prev_in_order(self.object, qs, prev=True, loop=False)
        next_ph = next_or_prev_in_order(self.object, qs, prev=False, loop=False)
        context['prev_ph'] = prev_ph
        context['next_ph'] = next_ph

        if self.request.user.is_authenticated:
            like = Like.objects.filter(user=self.request.user, photo_id=self.object.id)
            liked = False
            if like:
                liked = True
            context['liked'] = liked

        c_form = AddCommentForm
        context['comment_form'] = c_form

        return context


class AddPhotoView(CreateView):

    model = Photo
    form_class = AddPhotoForm
    template_name = 'add-photo.html'


class EditPhotoView(UpdateView):

    model = Photo
    form_class = EditPhotoForm
    template_name = 'edit-photo.html'


class DeletePhotoView(DeleteView):

    model = Photo
    template_name = 'confirm-delete-photo.html'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('portfolio-detail', args=[str(self.object.portfolio.pk)])


class PortfolioPhotoDetailView(DetailView):

    model = Photo
    template_name = 'portfolio-photo-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        qs = Photo.objects.filter(portfolio=self.object.portfolio)
        prev_ph = next_or_prev_in_order(self.object, qs, prev=True, loop=False)
        next_ph = next_or_prev_in_order(self.object, qs, prev=False, loop=False)
        context['prev_ph'] = prev_ph
        context['next_ph'] = next_ph

        if self.request.user.is_authenticated:
            like = Like.objects.filter(user=self.request.user, photo_id=self.object.id)
            liked = False
            if like:
                liked = True
            context['liked'] = liked

        c_form = AddCommentForm
        context['comment_form'] = c_form

        return context


def CategoryView(request, cat):
    category_photos = Photo.objects.filter(category=cat)
    cats = Category.objects.all()
    cat_exists = False
    try:
        if cats.get(name=cat):
            cat_exists = True
    except Category.DoesNotExist:
        pass
    return render(request, 'category-detail.html',
                  {'category': cat, 'category_photos': category_photos,'cat_exists':cat_exists, 'all_cats': cats})


def CategoryPhotoDetailView(request, cat, pk):

    photo = Photo.objects.get(id=pk)
    qs = Photo.objects.filter(category=cat)
    prev_ph = next_or_prev_in_order(photo, qs, prev=True, loop=False)
    next_ph = next_or_prev_in_order(photo, qs, prev=False, loop=False)

    context = {
        'photo':photo,
        'next_ph': next_ph,
        'prev_ph': prev_ph,
        'category': cat
    }

    if request.user.is_authenticated:
        like = Like.objects.filter(user=request.user, photo_id=pk)
        liked = False
        if like:
            liked = True
        context['liked'] = liked

    c_form = AddCommentForm
    context['comment_form'] = c_form

    return render(request, 'category-photo-detail.html', context)


def LikePhotoView(request, pk):
    new_like, created = Like.objects.get_or_create(user=request.user, photo=Photo.objects.get(id=pk))
    prev_page = request.POST.get('next', '/')
    return HttpResponseRedirect(prev_page)


def DislikePhotoView(request, pk):
    if  Like.objects.get(user=request.user, photo_id=pk):
        Like.objects.get(user=request.user, photo_id=pk).delete()

    prev_page = request.POST.get('next', '/')
    return HttpResponseRedirect(prev_page)


def AddCommentView(request, pk):

    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            photo = form.cleaned_data['photo']
            body = form.cleaned_data['body']
            new_comment = Comment(author=author, photo=photo, body=body)
            new_comment.save()

    prev_page = request.POST.get('next', '/')
    return HttpResponseRedirect(prev_page)


def RemoveCommentView(request, pk, com_id):
    if Comment.objects.get(id=com_id):
        Comment.objects.get(id=com_id).delete()

    prev_page = request.POST.get('goto', '/')
    return HttpResponseRedirect(prev_page)


def SearchPhotosView(request):
    category_list = Category.objects.all
    if request.method == 'GET':
        searched = request.GET.get('search')
        photos = Photo.objects.filter(Q(title__contains=searched) |
                                      Q(description__contains=searched) |
                                      Q(camera_name__contains=searched) |
                                      Q(lens__contains=searched) |
                                      Q(used_light=searched))

        return render(request, 'discover-searched-photos.html', {'photos': photos,
                                                                 'categories': category_list,
                                                                 'searched': searched})


def SearchPhotoDetailView(request, searched, pk):
    photo = Photo.objects.get(id=pk)
    qs = Photo.objects.filter(Q(title__contains=searched) |
                              Q(description__contains=searched) |
                              Q(camera_name__contains=searched) |
                              Q(lens__contains=searched) |
                              Q(used_light=searched))
    prev_ph = next_or_prev_in_order(photo, qs, prev=True, loop=False)
    next_ph = next_or_prev_in_order(photo, qs, prev=False, loop=False)

    context = {
        'photo': photo,
        'next_ph': next_ph,
        'prev_ph': prev_ph,
        'searched': searched,
        'qs': qs
    }

    if request.user.is_authenticated:
        like = Like.objects.filter(user=request.user, photo_id=pk)
        liked = False
        if like:
            liked = True
        context['liked'] = liked

    c_form = AddCommentForm
    context['comment_form'] = c_form

    return render(request, 'discover-searched-photo-detail.html', context)


def SearchArtistsView(request):
    if request.method == 'GET':
        searched = request.GET.get('search')
        portfolios = Portfolio.objects.filter(Q(artistic_name__contains=searched) |
                                              Q(bio__contains=searched) |
                                              Q(photographer__username__contains=searched) |
                                              Q(photographer__first_name__contains=searched) |
                                              Q(photographer__last_name__contains=searched))

        return render(request, 'discover-searched-artists.html', {'portfolios': portfolios})




