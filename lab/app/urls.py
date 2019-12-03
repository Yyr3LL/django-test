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
        views.BankCreateView.as_view(),
        name="create_bank"
    ),
    url(
        r'^create/member/$',
        views.MemberCreateView.as_view(),
        name="create_member"
    ),
    url(
        r'^create/transaction/$',
        views.TransactionCreateView.as_view(),
        name="create_transaction"
    ),
    url(
        r'^delete/bank/(?P<bank_pk>\d+)$',
        views.BankDeleteView.as_view(),
        name="delete_bank"
    ),
    url(
        r'^delete/member/(?P<member_pk>\d+)$',
        views.MemberDeleteView.as_view(),
        name="delete_member"
    ),
    url(
        r'^delete/transaction/(?P<transaction_pk>\d+)$',
        views.TransactionDeleteView.as_view(),
        name="delete_transaction"
    ),
]
