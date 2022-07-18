
from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    # path("search/<q>", views.searchAjax, name="search"),
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('stock/', views.stock, name="stock"),
    path('scan_in/', views.scan_in, name="scan_in"),
    path('scan_out/', views.scan_out, name="scan_out"),
    path('people/', views.people, name="people"),
    path('members/', views.members, name="members"),
    path('add_member/', views.add_member, name="add_member"),
]
 