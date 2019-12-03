from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.MainPageView.as_view(),
        name="main_page"
    ),
    url(
        r'^detail/(?P<member_pk>\d+)/$',
        views.MemberDetailView.as_view(),
        name="member_detail"
    ),
    url(
        r'^create/bank/$',
        views.CreateBankView.as_view(),
        name="create_bank"
    ),
    url(
        r'^create/member/$',
        views.CreateMemberView.as_view(),
        name="create_member"
    ),
    url(
        r'^create/transaction/$',
        views.CreateTransactionView.as_view(),
        name="create_transaction"
    ),
]
