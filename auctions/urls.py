from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("create_listings", views.create_listings, name="create_listings"),

    path("listings/<int:auction_id>", views.listing, name="listings"),
    
    path("listings/<int:auction_id>/watchlist/modify", views.modify_watchlist, name="modify_watchlist"),

    path("listings/<int:auction_id>/bid", views.make_bid, name='make_bid')
]
