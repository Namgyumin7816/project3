
from django.urls import path
from . import views
  urlpatterns = [                                                                                                
      path('admin/', admin.site.urls),                                                                           
      path(r'/$', views.home), # 여기에서 home 컨트롤러를 호출하게 맵핑해준다.  
  ]