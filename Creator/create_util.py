import os


class CreateUtil:

    @staticmethod
    def checkFolder(path):
        """
        @summary: 检查对应的文件夹是否创建，如果未创建则创建之
        """
        if not os.path.exists(path):
            os.makedirs(path)

    # def