import os
import datetime
import shutil

"""
@summary: 文件工具
"""
class FileUtil:

    def __init__(self, path):
        self.f = open(path, 'w', encoding="utf-8")

    def read(self):
        c = self.f.read()
        return c

    def write(self, string):
        self.f.write(string)

    def close(self):
        self.f.close()

    #----------- 文件夹
    @staticmethod
    def getCurrentDir():
        return os.path.abspath('.')
    
        
    @staticmethod
    def check_path(path):
        """
        @summary: 检查文件或者文件夹路径是否存在，不存在会自动创建
        @param path: 文件或者文件夹路径
        """
        
        if os.path.exists(path) == False:
            if "." in path:
                f = open(path, encoding='utf-8')
                f.close()
            elif path[len(path) - 1: len(path)] == "/":
                os.makedirs(path)
    
    @staticmethod
    def path_exists(path):
        """
        @summary: 检查文件或者文件夹路径是否存在
        @param path: 文件或者文件夹路径
        """
        
        if os.path.exists(path):
            return True
        else:
            return False
        
    @staticmethod
    def rename(old, new):
        """
        @summary: 重新命名文件
        @param old: 旧文件路径
        @param new: 新文件路径
        """
        
        os.rename(old, new)
    
    @staticmethod
    def create_dir(path):
        """
        @summary: 生成文件夹
        @param path: 文件夹路径
        """
        
        if os.path.exists(path) == False:
            os.makedirs(path)
    
    @staticmethod
    def pack_dir(sourcePath, storePath):
        # 检查路径
        FileUtil.check_path(storePath)
        
        # 压缩文件
        zip_name = shutil.make_archive(sourcePath, f'zip', sourcePath)
        # print(zip_name)  # 返回文件的最终路径
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H:%M:%S")
        names = zip_name.split("/")
        
        # 获取压缩文件名
        zip_name1 = formatted_datetime+"_"+names[len(names) - 1]
        
        # 重命名文件
        os.rename(zip_name, zip_name1)
        
        # 移动文件
        shutil.move(zip_name1, storePath)

    #----------- 文件
    @staticmethod
    def read_file(file_path="out.json"):
        """
        @summary: 读取文件内容
        """
        f = open(file_path, 'r', encoding="utf-8")
        c = f.read()
        f.close()
        
        return c
        
    @staticmethod
    def write_file(content, file_path="out.json"):
        """
        @summary: 写入文件内容
        """
        f = open(file_path, 'w', encoding="utf-8")
        c = f.write(content)
        f.close()
        
        return c
        
    @staticmethod
    def append_file(content, file_name="out.json"):
        """
        @summary: 在末尾添加文件内容
        """
        with open(file_name, 'a') as file:
            file.write(content)
        
    @staticmethod
    def delete_file(file_path):
        sta = FileUtil.path_exists(file_path)
        if sta:
            os.remove(file_path)