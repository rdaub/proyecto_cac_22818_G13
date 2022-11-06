from django.urls import path
from servinquilino import views

urlpatterns=[
#    path('', views.home, name='home'),
    path('', views.signin, name='home'),
#    path('', views.login, name= 'login'),
    path('usuarios/', views.usuarios, name= 'usuarios'),
    path('nosotros/', views.nosotros , name='nosotros'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('datos/', views.datos, name='datos'),
    path('datos/<int:IdUsuario>', views.detalle_datos, name='detalle_datos'),
    path('datos/<int:IdUsuario>/borrar', views.borrar_dato, name='borrar_dato'),
    path('crear_datos/', views.crear_datos, name='crear_datos'),
    path('crear_expensas/', views.crear_expensas, name='crear_expensas'),
    path('pagar_cuota/', views.pagar_cuota, name='pagar_cuota'),
    path('cuotas/', views.cuotas, name='cuotas'),
    path('cuotas/<int:IdExpensa>', views.detalle_cuotas, name='detalle_cuotas'),
    path('cuotas/<int:IdExpensa>/pagar', views.pagar_cuota, name='pagar_cuota'),
    path('cuotas/<int:IdExpensa>/borrar', views.borrar_cuota, name='borrar_cuota'),
    ]
