from sqlalchemy_test import User
from sqlalchemy_test import db_session


# 创建数据
user = User(name='山河老师')
db_session.add(user)
db_session.commit()
db_session.close()