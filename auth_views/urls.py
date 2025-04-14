from django.urls import path

import auth_views
from . import views

app_name = 'auth_view1'  # تعریف app_name
urlpatterns = [
                # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
                # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
                # path('signup/', views.signup, name='signup'),  # ویو ثبت‌نام
]