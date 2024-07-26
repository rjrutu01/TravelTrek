
from django.urls import path
from traveltrekapp import views
from django.conf import settings                #import for image
from django.conf.urls.static import static      #import for image

urlpatterns = [
   path('',views.index),
   path('create_destination',views.create_destination),
   path('read_destination',views.read_destination),
   path('read_destination_detail/<rid>',views.read_destination_deatails),
   path('delete_destination/<rid>',views.delete_destination),
   path('update_destination/<rid>',views.update_destination),
   path('create_book/<rid>',views.create_book),
   path('read_book',views.read_book),
   path('update_book/<rid>',views.update_book),
   path('delete_book/<rid>',views.delete_book),
   path('sign_up',views.sign_up),
   path('sign_in',views.sign_in),
   path('logout',views.user_logout),
   path('create_feedback/<rid>',views.create_feedback),
   path('forget_password',views.forget_password),
   path('otp_verification',views.otp_verification),
   path('new_password',views.new_password)
   
]

#for image
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)