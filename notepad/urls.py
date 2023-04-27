from django.urls import path
from notepad import views

urlpatterns = [
    path('', views.home_page),
    path('signup/', views.userdetails),
    path('login/', views.login_user),
    path('', views.logout_view),
    path('notesave/', views.notes),
    path('viewnote/<int:note_id>/',views.view_note),
    path('del/<int:note_id>/',views.del_note),
]