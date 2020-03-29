"""WebTextCharacter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view, search, transfer, testdb, testdb2, search2, search3, transfer2
from . import tree
from . import transform
from . import click

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.home),
    url(r'^search$', search.search),
    url(r'^search-post$', search.search_post),
    url(r'^transfer$', transfer.transfer),
    url(r'^test', view.test),
    url(r'^insert-passages', testdb.insertPassages),
    url(r'^unify-passage', transfer.unifyPassage),
    url(r'^download-file', testdb.downloadFile),
    url(r'^download1file', view.download1file),
    url(r'^get-file-name', testdb.getFileName),
    url(r'^download-all-files', view.downloadAllfile),
    url(r'^lvzheqing',testdb.testdb),
    url(r'^index/$', view.index, name='index'),
    url(r'^jiouxing/', view.miaohong_home),
    url(r'^tree', tree.tree),
    url(r'^transform', transform.transform),
    url(r'^click',click.click),
    url(r'^Trans/', view.transform),
    url(r'^ww', testdb2.ww),
    url(r'^index2/', view.index2),
    url(r'^search-form/', search2.search_form),
    url(r'^search2/', search2.search),
    url(r'^search-post2/',search3.search_post ),
    url(r'^transfer2', transfer2.transfer)
]
