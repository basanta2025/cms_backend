from django.urls import include, path

from .views import (
    VendorBankAccountCreateView,
    VendorBankAccountListView,
    VendorBankAccountRetrieveView,
    VendorBankAccountUpdateView,
    VendorContactPersonCreateView,
    VendorContactPersonListView,
    VendorContactPersonRetrieveView,
    VendorContactPersonUpdateView,
    VendorCreateView,
    VendorDocumentCreateView,
    VendorDocumentListView,
    VendorDocumentRetrieveView,
    VendorDocumentUpdateView,
    VendorFinancialDetailCreateView,
    VendorFinancialDetailListView,
    VendorFinancialDetailRetrieveView,
    VendorFinancialDetailUpdateView,
    VendorLabourTypeCreateView,
    VendorLabourTypeListView,
    VendorLabourTypeRetrieveView,
    VendorLabourTypeUpdateView,
    VendorListView,
    VendorPaymentTermCreateView,
    VendorPaymentTermListView,
    VendorPaymentTermRetrieveView,
    VendorPaymentTermUpdateView,
    VendorRetrieveView,
    VendorUpdateView,
)

payment_term_patterns = [
    path(
        "create",
        VendorPaymentTermCreateView.as_view(),
        name="vendor_payment_term_create",
    ),
    path("list", VendorPaymentTermListView.as_view(), name="vendor_payment_term_list"),
    path(
        "retrieve/<int:pk>",
        VendorPaymentTermRetrieveView.as_view(),
        name="vendor_payment_term_retrieve",
    ),
    path(
        "update/<int:pk>",
        VendorPaymentTermUpdateView.as_view(),
        name="vendor_payment_term_update",
    ),
]
vendor_document_patterns = [
    path(
        "create",
        VendorDocumentCreateView.as_view(),
        name="vendor_document_create",
    ),
    path(
        "list",
        VendorDocumentListView.as_view(),
        name="vendor_document_list",
    ),
    path(
        "retrieve/<int:pk>",
        VendorDocumentRetrieveView.as_view(),
        name="vendor_document_retrieve",
    ),
    path(
        "update/<int:pk>",
        VendorDocumentUpdateView.as_view(),
        name="vendor_document_update",
    ),
]
vendor_document_patterns = [
    path(
        "create",
        VendorDocumentCreateView.as_view(),
        name="vendor_document_create",
    ),
    path(
        "list",
        VendorDocumentListView.as_view(),
        name="vendor_document_list",
    ),
    path(
        "retrieve/<int:pk>",
        VendorDocumentRetrieveView.as_view(),
        name="vendor_document_retrieve",
    ),
    path(
        "update/<int:pk>",
        VendorDocumentUpdateView.as_view(),
        name="vendor_document_update",
    ),
]
vendor_bank_account_patterns = [
    path(
        "create",
        VendorBankAccountCreateView.as_view(),
        name="vendor_bank_account_create",
    ),
    path(
        "list",
        VendorBankAccountListView.as_view(),
        name="vendor_bank_account_list",
    ),
    path(
        "retrieve/<int:pk>",
        VendorBankAccountRetrieveView.as_view(),
        name="vendor_bank_account_retrieve",
    ),
    path(
        "update/<int:pk>",
        VendorBankAccountUpdateView.as_view(),
        name="vendor_bank_account_update",
    ),
]

vendor_contact_person_patterns = [
    path(
        "create",
        VendorContactPersonCreateView.as_view(),
        name="vendor_contact_person_create",
    ),
    path(
        "list",
        VendorContactPersonListView.as_view(),
        name="vendor_contact_person_list",
    ),
    path(
        "retrieve/<int:pk>",
        VendorContactPersonRetrieveView.as_view(),
        name="vendor_contact_person_retrieve",
    ),
    path(
        "update/<int:pk>",
        VendorContactPersonUpdateView.as_view(),
        name="vendor_contact_person_update",
    ),
]
vendor_financial_detail_patterns = [
    path(
        "create",
        VendorFinancialDetailCreateView.as_view(),
        name="vendor_financial_detail_create",
    ),
    path(
        "list",
        VendorFinancialDetailListView.as_view(),
        name="vendor_financial_detail_list",
    ),
    path(
        "retrieve/<int:pk>",
        VendorFinancialDetailRetrieveView.as_view(),
        name="vendor_financial_detail_retrieve",
    ),
    path(
        "update/<int:pk>",
        VendorFinancialDetailUpdateView.as_view(),
        name="vendor_financial_detail_update",
    ),
]
vendor_labour_type_patterns = [
    path(
        "create",
        VendorLabourTypeCreateView.as_view(),
        name="vendor_labour_type_create",
    ),
    path(
        "list",
        VendorLabourTypeListView.as_view(),
        name="vendor_labour_type_list",
    ),
    path(
        "retrieve/<int:pk>",
        VendorLabourTypeRetrieveView.as_view(),
        name="vendor_labour_type_retrieve",
    ),
    path(
        "update/<int:pk>",
        VendorLabourTypeUpdateView.as_view(),
        name="vendor_labour_type_update",
    ),
]
vendor_patterns = [
    path("create", VendorCreateView.as_view(), name="vendor_create"),
    path("list", VendorListView.as_view(), name="vendor_list"),
    path("retrieve/<int:pk>", VendorRetrieveView.as_view(), name="vendor_retrieve"),
    path("update/<int:pk>", VendorUpdateView.as_view(), name="vendor_update"),
]
urlpatterns = [
    path("payment-term/", include(payment_term_patterns)),
    path("document/", include(vendor_document_patterns)),
    path("bank-account/", include(vendor_bank_account_patterns)),
    path("contact-person/", include(vendor_contact_person_patterns)),
    path("financial-detail/", include(vendor_financial_detail_patterns)),
    path("labour-type/", include(vendor_labour_type_patterns)),
    path("vendor/", include(vendor_patterns)),
]
