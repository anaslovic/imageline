from django.urls import path

from portfolioapp.views import HomeView, DiscoverArtistsView, DiscoverPhotosView, PortfolioDetailView, \
    AddPhotoView, EditPhotoView, DeletePhotoView, PortfolioPhotoDetailView, CategoryView, \
    CategoryPhotoDetailView, UpdatePortfolioView, LikePhotoView, DislikePhotoView, DiscoverPhotoDetailView, \
    AddCommentView, RemoveCommentView, SearchPhotosView, SearchArtistsView, SearchPhotoDetailView

#regarding home and discover page
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('discover/photos/', DiscoverPhotosView.as_view(), name='discover-photos'),
    path('discover/artists/', DiscoverArtistsView.as_view(), name='discover-artists'),
    path('discover/photos/photo/<int:pk>', DiscoverPhotoDetailView.as_view(), name='discover-photo-detail'),
    path('discover/photos/search/', SearchPhotosView, name='search-photos'),
    path('discover/photos/<str:searched>/<int:pk>', SearchPhotoDetailView, name='search-result-photo-detail'),
    path('discover/artists/search/', SearchArtistsView, name='search-artists'),
]

#regarding portfolio page
urlpatterns+=[
    path('portfolio/<int:pk>', PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('portfolio/photo/<int:pk>', PortfolioPhotoDetailView.as_view(), name='portfolio-photo-detail'),
    path('portfolio/update/<int:pk>', UpdatePortfolioView.as_view(), name='portfolio-update'),
]

#regarding category pages
urlpatterns+=[
    path('category/<str:cat>', CategoryView, name='category-detail'),
    path('category/<str:cat>/photo/<int:pk>', CategoryPhotoDetailView, name='category-photo-detail'),
]

#regarding photo create, update, delete
urlpatterns+=[
    path('add_photo/', AddPhotoView.as_view(), name='add-photo'),
    path('photo/edit_photo/<int:pk>', EditPhotoView.as_view(), name='edit-photo'),
    path('photo/delete_photo/<int:pk>', DeletePhotoView.as_view(), name='delete-photo'),
]

#regardin likes and comments
urlpatterns+=[
    path('like/<int:pk>', LikePhotoView, name='like-photo'),
    path('dislike/<int:pk>', DislikePhotoView, name='dislike-photo'),
    path('comment/<int:pk>', AddCommentView, name='add-comment'),
    path('comment/delete/<int:pk>/<int:com_id>', RemoveCommentView, name='remove-comment'),
]