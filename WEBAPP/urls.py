from django.urls import path
from WEBAPP import views

urlpatterns=[
    path('viewhome/', views.viewhome, name="viewhome"),
    path('viewaboutus/', views.viewaboutus, name="viewaboutus"),
    path('viewacontactus/', views.viewacontactus, name="viewacontactus"),
    path('saveadmincontact/', views.saveadmincontact, name="saveadmincontact"),

    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('discategory/<itemcatg>',views.discategory,name="discategory"),
    path('displayproduct/<int:dataid>', views.displayproduct, name="displayproduct"),

    path('displayloginpage/', views.displayloginpage, name="displayloginpage"),
    path('saveweblogin/', views.saveweblogin, name="saveweblogin"),
    path('custumerlogin/', views.custumerlogin, name="custumerlogin"),
    path('weblogout/', views.weblogout, name="weblogout"),



]