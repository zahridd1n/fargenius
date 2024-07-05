
from django.urls import path
from .views import CategoryView,PortfolioView,ContactView,NavbarView,SliderView,AboutView,PortfolioFilter,ClientAboutView,ContactView,Category_about,PortfolioFilter1


urlpatterns = [
    path('view_category/<str:lang>/', CategoryView.as_view()),
    path('view_category/<int:id>/<str:lang>/', CategoryView.as_view()),
    path('view_portfolio/<str:lang>/', PortfolioView.as_view()),
    path('view_portfolio/<int:id>/<str:lang>/', PortfolioView.as_view()),
    path('view_category_about/<str:lang>/', Category_about.as_view()),
    path('view_category_about/<int:id>/<str:lang>/', Category_about.as_view()),
    

    path('view_category_portfolio/<str:lang>/', PortfolioFilter.as_view()),
    path('view_category_portfolio/<int:id>/<str:lang>/', PortfolioFilter.as_view()),



    path('view_portfolio_with_cat_id/<int:id>/<str:lang>/', PortfolioFilter1.as_view()),


    path('view_contact/<str:lang>/', ContactView.as_view()),
    path('view_slider/<str:lang>/', SliderView.as_view()),
    path('view_about/<str:lang>/', AboutView.as_view()),
    path('view_social/', NavbarView.as_view()),
    path('view_clients/<str:lang>/', ClientAboutView.as_view()),
    path('view_contact/', ContactView.as_view()),



    
]
