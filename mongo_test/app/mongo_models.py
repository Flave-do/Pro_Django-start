from django.conf import settings
conn = settings.MONFOCLIENT['user_qingdeng']    # 需要链接的数据库

class User(object):
    db = conn['user']

    @classmethod
    def insert(cls,**params):
        return cls.db.insert(params)

    @classmethod
    def get(cls,**params):
        return cls.db.find_one(params)

    @classmethod
    def gets(cls,**params):
        return list(cls.db.find(params))

    @classmethod
    def update(cls,_id,**params):
        # 更新
        return cls.db.update({'_id':_id},{'$set':params})