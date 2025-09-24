# author: 测试蔡坨坨
# datetime: 2024/1/14 15:51
# function: 账单解析规则

from constants.enums import (AccountEnum, ProviderEnum)


class Rules:
    # 对应微信账单字段&借贷账户：供应商, 交易类型, 交易对方, 商品, 收支, 支付方式, 当前状态, 借方, 贷方
    wechat_rules = [
        # 中国石化
        (ProviderEnum.WECHAT, '', '中国石化', '', '支出', '零钱', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '', '中国石化', '', '支出', '浦发银行储蓄卡.*1959', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.ASSETS_SPD1959),

        (ProviderEnum.WECHAT, '', '中国石化', '', '支出', '兴业银行信用卡.*1943', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB1943),

        (ProviderEnum.WECHAT, '', '中国石化|加油', '', '支出', '兴业银行信用卡.*8903', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB8903),

        (ProviderEnum.WECHAT, '', '中国石化', '', '支出', '招商银行信用卡.*7383', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CMB7383),

        # 国网智慧车联网
        (ProviderEnum.WECHAT, '商户消费', '国网智慧车联网技术有限公司', '', '支出', '零钱', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '商户消费', '国网智慧车联网技术有限公司', '', '支出', '建设银行储蓄卡.*8249', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.ASSETS_CCB8249),

        (ProviderEnum.WECHAT, '商户消费', '国网智慧车联网技术有限公司', '', '支出', '浦发银行信用卡.*8741', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_SPD8741),

        (ProviderEnum.WECHAT, '商户消费', '国网智慧车联网技术有限公司', '', '支出', '兴业银行信用卡.*1943', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB1943),

        (ProviderEnum.WECHAT, '商户消费', '国网智慧车联网技术有限公司', '', '支出', '兴业银行信用卡.*8903', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB8903),

        (ProviderEnum.WECHAT, '商户消费', '国网智慧车联网技术有限公司', '', '支出', '招商银行信用卡.*7383', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CMB7383),

        (ProviderEnum.WECHAT, '商户消费', '国网智慧车联网技术有限公司', '', '支出', '中国银行信用卡.*3705', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_BOC3705),

        # 充电
        (ProviderEnum.WECHAT, '商户消费', '充电', '', '支出', '兴业银行信用卡.*1943', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB1943),

        (ProviderEnum.WECHAT, '商户消费', '充电', '', '支出', '招商银行信用卡.*7383', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CMB7383),

        # 违章
        (ProviderEnum.WECHAT, '商户消费', '江苏财政', '道路交通安全违法', '支出', '建设银行储蓄卡.*8249', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.ASSETS_CCB8249),

        (ProviderEnum.WECHAT, '商户消费', '江苏财政', '道路交通安全违法', '支出', '兴业银行信用卡.*8903', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB8903),

        (ProviderEnum.WECHAT, '商户消费', '江苏财政', '道路交通安全违法', '支出', '招商银行信用卡.*7383', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CMB7383),

        # ETC
        (ProviderEnum.WECHAT, '商户消费', '贵州黔通', 'ETC', '支出', '兴业银行信用卡.*1943', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB1943),

        (ProviderEnum.WECHAT, '商户消费', '贵州黔通', 'ETC', '支出', '兴业银行信用卡.*8903', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB8903),

        (ProviderEnum.WECHAT, '商户消费', '贵州黔通', 'ETC', '支出', '中国银行信用卡.*3705', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_BOC3705),

        # 停车
        (ProviderEnum.WECHAT, '商户消费', '停车', '', '支出', '兴业银行信用卡.*8903', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB8903),

        (ProviderEnum.WECHAT, '商户消费', '', '停车', '支出', '招商银行信用卡.*7383', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CMB7383),

        # 修车洗车
        (ProviderEnum.WECHAT, '扫二维码付款', '汽车维修', '', '支出', '零钱', '已转账',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '扫二维码付款', '周艳|汽修', '', '支出', '建设银行储蓄卡.*8249', '已转账',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.ASSETS_CCB8249),

        # 购票
        (ProviderEnum.WECHAT, '商户消费', '同程旅行|中铁网络', '', '支出', '兴业银行信用卡.*1943', '支付成功',
         AccountEnum.EXPENSES_CARCOST, AccountEnum.LIABILITIES_CIB1943),

        # 二、饮食吃喝

        # 2。3小商店
        (ProviderEnum.WECHAT, '商户消费', '猫猫幸福', '', '支出', '零钱', '支付成功',
         AccountEnum.EXPENSES_STOREMARKET, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '商户消费', '猫猫幸福', '', '支出', '建设银行储蓄卡.*8249', '支付成功',
         AccountEnum.EXPENSES_STOREMARKET, AccountEnum.ASSETS_CCB8249),

        (ProviderEnum.WECHAT, '商户消费', '猫猫幸福', '', '支出', '兴业银行信用卡.*1943', '支付成功',
         AccountEnum.EXPENSES_STOREMARKET, AccountEnum.LIABILITIES_CIB1943),

        (ProviderEnum.WECHAT, '商户消费', '猫猫幸福', '', '支出', '兴业银行信用卡.*8903', '支付成功',
         AccountEnum.EXPENSES_STOREMARKET, AccountEnum.LIABILITIES_CIB8903),

        (ProviderEnum.WECHAT, '商户消费', '猫猫幸福|丰e足食', '', '支出', '招商银行信用卡.*7383', '支付成功',
         AccountEnum.EXPENSES_STOREMARKET, AccountEnum.LIABILITIES_CMB7383),

        (ProviderEnum.WECHAT, '扫二维码付款', '叶梅', '', '支出', '零钱', '已转账',
         AccountEnum.EXPENSES_STOREMARKET, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '扫二维码付款', '叶梅', '', '支出', '浦发银行储蓄卡.*1959', '已转账',
         AccountEnum.EXPENSES_STOREMARKET, AccountEnum.ASSETS_SPD1959),

        # 三、个人资金划转，及他人过账
        # 3。1信用卡还款
        (ProviderEnum.WECHAT, '信用卡还款', '兴业银行信用卡还款', '', '', '零钱', '支付成功',
         AccountEnum.LIABILITIES_CIB1943, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '信用卡还款', '交通银行信用卡还款', '', '', '零钱', '支付成功',
         AccountEnum.LIABILITIES_COM3115, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '信用卡还款', '建设银行信用卡还款', '', '', '零钱', '支付成功',
         AccountEnum.LIABILITIES_CCB0325, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '信用卡还款', '中国银行信用卡还款', '', '', '零钱', '支付成功',
         AccountEnum.LIABILITIES_BOC3705, AccountEnum.ASSETS_WECHAT),

        # 3。2微信提现
        (ProviderEnum.WECHAT, '零钱提现', '工商银行.*8201', '', '', '工商银行储蓄卡.*8201', '提现已到账',
         AccountEnum.ASSETS_ICBC8201, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '零钱提现', '建设银行.*8249', '', '', '建设银行储蓄卡.*8249', '提现已到账',
         AccountEnum.ASSETS_CCB8249, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '零钱提现', '浦发银行.*1959', '', '', '浦发银行储蓄卡.*1959', '提现已到账',
         AccountEnum.ASSETS_SPD1959, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '零钱提现', '招商银行.*3042', '', '', '招商银行储蓄卡.*3042', '提现已到账',
         AccountEnum.ASSETS_CMB3042, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '零钱充值', '建设银行.*8249', '', '', '建设银行储蓄卡.*8249', '充值完成',
         AccountEnum.ASSETS_WECHAT, AccountEnum.ASSETS_CCB8249),


        # 四、个人支出
        (ProviderEnum.WECHAT, '商户消费', '深圳市腾讯', '', '支出', '零钱', '支付成功',
         AccountEnum.EXPENSES_TENCENT, AccountEnum.ASSETS_WECHAT),

        (ProviderEnum.WECHAT, '商户消费', '深圳市腾讯', '', '支出', '招商银行信用卡.*7383', '支付成功',
         AccountEnum.EXPENSES_TENCENT, AccountEnum.LIABILITIES_CMB7383),

        (ProviderEnum.WECHAT, '商户消费', '深圳市腾讯', '', '支出', '兴业银行信用卡.*1943', '支付成功',
         AccountEnum.EXPENSES_TENCENT, AccountEnum.LIABILITIES_CIB1943),

        (ProviderEnum.WECHAT, '商户消费', '深圳市腾讯', '', '支出', '兴业银行信用卡.*8903', '支付成功',
         AccountEnum.EXPENSES_TENCENT, AccountEnum.LIABILITIES_CIB8903),

        (ProviderEnum.WECHAT, '商户消费', '', '', '', '零钱', '',
         AccountEnum.EXPENSES_TENCENT, AccountEnum.ASSETS_WECHAT),

    ]

    alipay_rules = []
