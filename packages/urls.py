from django.urls import path
from .views import PackageView, PackageViewDetailByName

urlpatterns = [
    path("packages/", PackageView.as_view()),
    path("packages/<str:name>/", PackageViewDetailByName.as_view()),
]
