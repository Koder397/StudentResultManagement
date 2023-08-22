from django.urls import path

from backend.views import dashboard, admin_login, admin_logout, CountryList, CountryNew, CountryUpdate, CountryDelete, \
    StateList, StateNew, StateUpdate, StateDelete, CityList, CityNew, CityUpdate, CityDelete, student_chart

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('country', CountryList.as_view(), name='list'),
    path('country/new', CountryNew.as_view(), name='new'),
    path('country/<pk>/update', CountryUpdate.as_view(), name='update'),
    path('country/<pk>/delete', CountryDelete.as_view(), name='delete'),
    path('state', StateList.as_view(), name='list'),
    path('state/new', StateNew.as_view(), name='new'),
    path('state/<pk>/update', StateUpdate.as_view(), name='update'),
    path('state/<pk>/delete', StateDelete.as_view(), name='delete'),
    path('city', CityList.as_view(), name='list'),
    path('city/new', CityNew.as_view(), name='new'),
    path('city/<pk>/update', CityUpdate.as_view(), name='update'),
    path('city/<pk>/delete', CityDelete.as_view(), name='delete'),
    path('login/', admin_login, name='login'),
    path('logout/', admin_logout, name='logout'),
    path('chart', student_chart, name='myChart')
]
