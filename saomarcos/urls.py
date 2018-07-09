"""
Definition of urls for saomarcos.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^contato', include('contato.urls')),
    url(r'^venda', include('venda.urls')),
    url(r'^servico', include('servico.urls')),
    url(r'^sobre', include('sobre.urls')),
    # Examples:
    # url(r'^$', saomarcos.views.home, name='home'),
    # url(r'^saomarcos/', include('saomarcos.saomarcos.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
