# author: 测试蔡坨坨
# datetime: 2024/3/22 0:45
# function: 主入口


from constants.enums import ProviderEnum
from src.accounting.ledger import Ledger
from src.process.bill_file_finder import BillFileFinder
from src.utils.path_utils import PathUtils
import os


class Main:
    def __init__(self, bill_dir='data'):
        self.bill_dir = bill_dir
        self.project_root = PathUtils().get_project_path()
        # 使用路径拼接
        data_dir = os.path.join(self.project_root, bill_dir)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def main(self):
        # 使用相同的finder实例
        finder = BillFileFinder(self.bill_dir)
        ledger = Ledger()

        # 微信账单处理
        wechat_files = finder.find_files_with_keyword('微信')
        if wechat_files:
            ledger.parse_bill(ProviderEnum.WECHAT, 18, wechat_files[0])
        else:
            print("【微信】：未存入待处理文件")

        # 支付宝账单处理
        alipay_files = finder.find_files_with_keyword('alipay')
        if alipay_files:
            ledger.parse_bill(ProviderEnum.ALIPAY, 26, alipay_files[0])
        else:
            print("【支付宝】：未存入待处理文件")


if __name__ == '__main__':
    Main().main()

    # beanhub工具进行账本内容格式化
    project_root = PathUtils().get_project_path()
    os.chdir(project_root)
    os.system('bh format wechat_transaction.bean')
