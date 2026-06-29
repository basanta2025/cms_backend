from .payement_term import (
    VendorPaymentTermCreateView,
    VendorPaymentTermListView,
    VendorPaymentTermRetrieveView,
    VendorPaymentTermUpdateView,
)
from .vender_docs import (
    VendorDocumentCreateView,
    VendorDocumentListView,
    VendorDocumentRetrieveView,
    VendorDocumentUpdateView,
)
from .vendor_bank_acc import (
    VendorBankAccountCreateView,
    VendorBankAccountListView,
    VendorBankAccountRetrieveView,
    VendorBankAccountUpdateView,
)
from .vendor_contacts import (
    VendorContactPersonCreateView,
    VendorContactPersonListView,
    VendorContactPersonRetrieveView,
    VendorContactPersonUpdateView,
)
from .vendor_finance_detail import (
    VendorFinancialDetailCreateView,
    VendorFinancialDetailListView,
    VendorFinancialDetailRetrieveView,
    VendorFinancialDetailUpdateView,
)
from .vendor_labour_types import (
    VendorLabourTypeCreateView,
    VendorLabourTypeListView,
    VendorLabourTypeRetrieveView,
    VendorLabourTypeUpdateView,
)
from .vendors import (
    VendorCreateView,
    VendorListView,
    VendorRetrieveView,
    VendorUpdateView,
)

__all__ = [
    # payment term
    "VendorPaymentTermCreateView",
    "VendorPaymentTermListView",
    "VendorPaymentTermRetrieveView",
    "VendorPaymentTermUpdateView",
    # vendor docs
    "VendorDocumentCreateView",
    "VendorDocumentListView",
    "VendorDocumentRetrieveView",
    "VendorDocumentUpdateView",
    # vendor bank acc
    "VendorBankAccountCreateView",
    "VendorBankAccountListView",
    "VendorBankAccountRetrieveView",
    "VendorBankAccountUpdateView",
    # vendor contacts
    "VendorContactPersonCreateView",
    "VendorContactPersonListView",
    "VendorContactPersonRetrieveView",
    "VendorContactPersonUpdateView",
    # vendor finance detail
    "VendorFinancialDetailCreateView",
    "VendorFinancialDetailListView",
    "VendorFinancialDetailRetrieveView",
    "VendorFinancialDetailUpdateView",
    # vendor labour types
    "VendorLabourTypeCreateView",
    "VendorLabourTypeListView",
    "VendorLabourTypeRetrieveView",
    "VendorLabourTypeUpdateView",
    # vendors
    "VendorCreateView",
    "VendorListView",
    "VendorRetrieveView",
    "VendorUpdateView",
]
