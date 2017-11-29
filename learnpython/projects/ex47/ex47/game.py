#encoding=utf-8

class Room(object):
    """
        定义一个房间类
        有name、descript、paths属性
        有go方法获得direction
        有add_paths更新paths
    """
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
        
    def add_paths(self, paths):
        self.paths.update(paths)