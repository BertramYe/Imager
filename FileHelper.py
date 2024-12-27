from settings import Static_Path
from os import path,makedirs
from LoggerHelper import Logger


class Filer():
    def __init__(self) -> None:
        self.static_path = (Static_Path.strip(' ') if Static_Path.endswith('/') else f'{Static_Path.strip(' ')}/') if Static_Path else 'static/'
        self.logger = Logger()

    def check_and_create_path(self,to_check_path:str,create_checked_path:bool=False):
        try:
            if not path.exists(to_check_path):
                if create_checked_path: # 如果文件夹不存在，创建文件夹
                    makedirs(to_check_path)
                    return to_check_path
                else:
                    #  如果不需要创建静态文件
                    return None
            else:
                return to_check_path
        except Exception as error:
            self.logger.error(f'error when check the path: {to_check_path} ,error: {error}')
            return None
            
    def get_static_path(self):
        return self.check_and_create_path(self.static_path,True)