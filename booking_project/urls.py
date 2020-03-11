from django.conf.urls import include, url
from django.contrib import admin

from bookings.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'booking_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/$', index, name="main-view"),
    url(r'^new/$', save_booking, name="addBooking"),
    url(r'^create_new/$', new_booking),
    url(r'^edit/(?P<booking_id>\d+)/$', edit_booking),
    url(r'^update/(?P<booking_id>\d+)/$', update_booking)
]
