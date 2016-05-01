from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^codebase', hello.views.codebase, name='codebase.html'),
    url(r'^dependencies', hello.views.dependencies, name='dependencies.html'),
    url(r'^config', hello.views.config, name='config.html'),
    url(r'^backing-services', hello.views.backing, name='backing-services.html'),
    url(r'^build-release-run', hello.views.build, name='build-release-run.html'),
    url(r'^process', hello.views.process, name='process.html'),
    url(r'^port-binding', hello.views.port, name='port-binding.html'),
    url(r'^concurrency', hello.views.concurrency, name='concurrency.html'),
    url(r'^disposability', hello.views.disposability, name='disposability.html'),
    url(r'^dev-prod-parity', hello.views.devprod, name='dev-prod-parity.html'),
    url(r'^logs', hello.views.logs, name='logs.html'),
    url(r'^admin-process', hello.views.admin, name='admin-process.html'),
]
