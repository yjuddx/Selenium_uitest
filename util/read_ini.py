# coding=utf-8
import configparser
from os.path import abspath, dirname



class ReadIni(object):
    def __init__(self):
        base_dir = dirname(dirname(abspath(__file__)))
        base_dir = base_dir.replace('\\', '/')
        base_dir = base_dir + "/config/" + "conf.ini"
        self.cf = self.load_ini(base_dir)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取value得值
    def get_value(self, node, key):
        data = self.cf.get(node, key)
        return data


if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value('Login_user', 'username'))
    print(read_init.get_value('Login_user', 'password'))

