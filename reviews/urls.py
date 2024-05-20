from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views
from rest_framework_simplejwt import views as jwt_views
router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)

urlpatterns = [
    path('', views.welcome_view, name='welcome_view'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>', views.book_detail, name='book_detail'),
    path("publishers/<int:pk>/", views.publisher_edit, name="publisher_edit"),
    path("publishers/new/", views.publisher_edit, name="publisher_create"),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:book_pk>/media/', views.book_media, name='book_media'),
    path('api/', include((router.urls, 'api'))),
    path('api/login', api_views.Login.as_view(), name='login'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api_example/',views.api_example, name='api_example')
]


