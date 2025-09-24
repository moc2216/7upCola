# author: 测试蔡坨坨
# datetime: 2024/3/20 1:01
# function: 枚举类

from enum import Enum


class AccountEnum(Enum):
    ASSETS_ICBC8201 = 'Assets:ICBC8201'
    ASSETS_CCB8249 = 'Assets:CCB8249'
    ASSETS_MS7763 = 'Assets:MS7763'
    ASSETS_SPD1959 = 'Assets:SPD1959'
    ASSETS_CMB3042 = 'Assets:CMB3042'
    ASSETS_WECHAT = 'Assets:Wechat'
    ASSETS_ZERO_REIMBURSE = 'Assets:Zero:Reimburse'
    ASSETS_ZERO_FIXME = 'Assets:Zero:Fixme'
    ASSETS_ZERO_CarLoan = 'Assets:Zero:CarLoan'
    ASSETS_ZERO_CURRENT_ACCOUNT = 'Assets:Zero:CurrentAccount'

    LIABILITIES_SPD8741 = 'Liabilities:SPD8741'
    LIABILITIES_CIB1943 = 'Liabilities:CIB1943'
    LIABILITIES_CIB8903 = 'Liabilities:CIB8903'
    LIABILITIES_CMB7383 = 'Liabilities:CMB7383'
    LIABILITIES_BOC3705 = 'Liabilities:BOC3705'
    LIABILITIES_COM3115 = 'Liabilities:COM3115'
    LIABILITIES_CCB0325 = 'Liabilities:CCB0325'
    EXPENSES_FIXME_PDD = 'Expenses:FixPDD'
    EXPENSES_CARCOST = 'Expenses:CarCost'
    EXPENSES_STOREMARKET = 'Expenses:StoreMarket'
    EXPENSES_LUNCH = 'Expenses:Lunch'
    EXPENSES_LUNCHOUT = 'Expenses:LunchOut'
    EXPENSES_EATOUT = 'Expenses:EatOut'
    EXPENSES_BREAKFAST = 'Expenses:Breakfast'
    EXPENSES_LIKEAUTHOR= 'Expenses:LikeAuthor'
    EXPENSES_INSURANCE = 'Expenses:Insurance'
    EXPENSES_FAMILY = 'Expenses:Family'
    EXPENSES_SONGLI = 'Expenses:Songli'
    EXPENSES_REDPOCKET = 'Expenses:Redpocket'
    EXPENSES_HAIRCUT = 'Expenses:HairCut'
    EXPENSES_GROCERIES = 'Expenses:Groceries'
    EXPENSES_STUDY = 'Expenses:Study'
    EXPENSES_RENQING = 'Expenses:RenQing'
    EXPENSES_TENCENT = 'Expenses:Tencent'
    EXPENSES_SUBSCRIBE = 'Expenses:Subscribe'
    EXPENSES_BILLS = 'Expenses:Bills'
    EXPENSES_ENJOY = 'Expenses:Enjoy'
    EXPENSES_UNKNOWN = 'Expenses:Unknown'
    EXPENSES_UNKNOWNBACK = 'Expenses:UnknownBack'
    EQUITY_TRANSFER = 'Equity:Transfer'
    EQUITY_RETURN = 'Equity:Return'
    EQUITY_DEPOSIT = 'Equity:Deposit'
    EQUITY_ZERO = 'Equity:Zero'
    EQUITY_REIMBURSE = 'Equity:Reimburse'
    EQUITY_CREDIT = 'Equity:CreditCard'

    def __str__(self):
        return self.value


class ProviderEnum(Enum):
    WECHAT = 'wechat'
    ALIPAY = 'alipay'

    def __str__(self):
        return self.value


class WechatColumnEnum(Enum):
    TRADE_TYPE = 1  # 交易类型
    TRADE_OBJECT = 2  # 交易对方
    PRODUCT = 3  # 商品
    INCOME_EXPENSE = 4  # 收/支
    PAY_METHOD = 6  # 交易方式
    PAY_STATUS = 7  # 交易状态


class AlipayColumnEnum(Enum):
    TRADE_TYPE = 1
    TRADE_OBJECT = 2
    PRODUCT = 4
    INCOME_EXPENSE = 5
    PAY_METHOD = 7
    PAY_STATUS = 8
