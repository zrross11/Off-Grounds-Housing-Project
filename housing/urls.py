from django.urls import path

from . import views

app_name = 'housing'
urlpatterns = [
    path('', views.HousingListing.as_view(), name='housing_index'),
    path('map', views.HousingMapping.as_view(), name='housing_listing'),
    path('inputForm', views.HousingInput.as_view(), name='housing_input'),
    path('searchResults', views.SearchView.as_view(), name="housing_search"),
    path('<int:id>', views.detailView, name="housing_details"),
    path('delete/<int:id>',
         views.delete_housing_option, name='delete_Housing_Option')
]
