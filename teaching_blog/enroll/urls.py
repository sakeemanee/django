from django.urls import path
from . import views
from enroll import views

app_name='enroll'
urlpatterns = [
    #path('', views.base1.as_view(), name='base1'),
    #path('admin/', admin.site.urls),
    path('', views.base1, name="base1"),
    path('', views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    
]
