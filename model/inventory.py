from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, func, select, Float
from model.database import Base, get_session
from loguru import logger


# 定义 inventories 表
def get_inventories():
    # query Inventories
    try:
        with get_session() as session:
            
            query = select(Inventories).where(Inventories.deleted_at.is_(None))
            res = session.execute(query)
            return res.scalars().all()
    
    except Exception as e:
        logger.error(f"Failed to get Inventories: {e}")
        session.rollback()
        return False
    finally:
        session.close()


class Inventories(Base):
    __tablename__ = 'inventories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(255), nullable=False)
    manufacturer = Column(String(255))
    count = Column(Integer, nullable=False)
    local = Column(String(255), nullable=False)
    date = Column(DateTime)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)
    
    def add_inventory(self):
        # 添加库存到数据库
        try:
            with get_session() as session:
                session.add(self)
                session.commit()
                logger.info(f"inventory {self.phone} added successfully.")
                return True
        
        except Exception as e:
            logger.error(f"Failed to add inventory: {e}")
            session.rollback()
            return False
        finally:
            session.close()
    
    def update_inventories(self):
        try:
            with get_session() as session:
                session.query(Inventories).filter(
                    Inventories.id == self.id and Inventories.deleted_at.is_(None)).update({
                        'phone': self.phone,
                        'manufacturer': self.manufacturer,
                        'count': self.count,
                        'local': self.local,
                        'date': self.date,
                        'price': self.price,
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
        
    def delete_inventories(self):
        try:
            with get_session() as session:
                session.query(Inventories).filter(
                    Inventories.id == self.id and Inventories.deleted_at.is_(None)).update({'deleted_at': func.now()})
                session.commit()
                logger.info("inventories delete success")
                return True
        
        except Exception as e:
            logger.error(f"Error: {e}")
            session.rollback()
            return False
        
        finally:
            session.close()
    
    def exist_inventories(self):
        # 检查库存是否存在
        try:
            with get_session() as session:
                
                query = select(Inventories).where(Inventories.id == self.id)
                res = session.execute(query)
                return res.scalars().first()
        
        except Exception as e:
            logger.error(f"Failed to check inventories: {e}")
            session.rollback()
            return False
        finally:
            session.close()
