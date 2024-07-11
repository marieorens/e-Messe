from django.urls import path
from Messe import views
urlpatterns = [
    
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('forgot',views.forgot,name='forgot'),  
    path('',views.firstpage,name='first'),
    path('home',views.acce,name="acceuil"),
    path('demande',views.demande,name='demande'),
    path('demande-validée',views.validation,name='validation'),
    path("historique",views.voirHistorique,name='historique'),
    path("insert",views.insert,name="insert"),
    path('api/messe/', views.api_get_demandes, name='api_get_demandes')
]
