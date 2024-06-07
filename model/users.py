from sqlalchemy import Column, Integer, String, DateTime, func, select, or_, and_
from model.database import Base, engine, get_session
from datetime import datetime
from loguru import logger


def get_user():
    try:
        with get_session() as session:

            query = select(Users).where(Users.deleted_at.is_(None))
            res = session.execute(query)
            session.commit()
            logger.info("users query success")
            result = res.scalars().all()
            return result
    except Exception as e:
        logger.error(f"Error: {e}")
        return None
    finally:
        session.close()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    permission = Column(String(255), nullable=False, default=100)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)
    
    def login(self):
        try:
            with get_session() as session:
                query = select(Users).where(Users.name == self.name and Users.deleted_at.is_(None))
                res = session.execute(query)
                session.commit()
                users = res.scalars().first()
     
                return users
        except Exception as e:
            logger.error(f"Error: {e}")
            session.rollback()
            return None
        finally:
            session.close()
            
    def add_user(self):
        try:
            with get_session() as session:
                session.add(self)
                session.commit()
                logger.info("users add success")
                return True

        except Exception as e:
            logger.error(f"Error: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    def exist_user(self):
        try:
            with get_session() as session:
                query = select(Users).where(Users.id == self.id and Users.deleted_at.is_(None))
                res = session.execute(query)
                session.commit()
                users = res.scalars().all()
                if users is not None:
                    return users[0]
                return False
            
        except Exception as e:
            logger.error(f"Error: {e}")
            session.rollback()
            return None
        finally:
            session.close()
    
    def update_user(self):
        try:
            with get_session() as session:
                session.query(Users).filter(Users.id == self.id and Users.deleted_at.is_(None)).update({
                    'name': self.name,
                    'password': self.password,
                    'permission': self.permission,
                    'updated_at': func.now()
                })
                session.commit()
                logger.info("users update success")
                return True

        except Exception as e:
            logger.error(f"Error: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    def delete_user(self):
        try:
            with get_session() as session:
                session.query(Users).filter(Users.id == self.id and Users.deleted_at.is_(None)).update({
                    'deleted_at': datetime.now()}
                )
                session.commit()
                logger.info("users delete success")
                return True
            
        except Exception as e:
            logger.error(f"Error: {e}")
            session.rollback()
            return False
        finally:
            session.close()





