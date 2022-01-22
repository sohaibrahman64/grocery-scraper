from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, insert
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///groceries.db', echo=True)
# meta = MetaData()
Base = declarative_base()


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    url = Column(String)
    alias = Column(String)


class Home(Base):
    __tablename__ = 'home'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description_1 = Column(String)
    description_2 = Column(String)
    description_3 = Column(String)
    description_4 = Column(String)
    description_5 = Column(String)

    image_1 = Column(String)
    image_2 = Column(String)
    image_3 = Column(String)
    image_4 = Column(String)
    image_5 = Column(String)

    old_price = Column(String)
    new_price = Column(String)
    availability = Column(String)
    product_code = Column(String)


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey(Categories.id))
    name = Column(String)
    description_1 = Column(String)
    description_2 = Column(String)
    description_3 = Column(String)
    description_4 = Column(String)
    description_5 = Column(String)

    image_1 = Column(String)
    image_2 = Column(String)
    image_3 = Column(String)
    image_4 = Column(String)
    image_5 = Column(String)

    old_price = Column(String)
    new_price = Column(String)
    availability = Column(String)
    product_code = Column(String)

    categories = relationship("Categories", back_populates="categories")


class DbUtils:
    engine = None

    def __init__(self, en):
        self.engine = en

    def insert_records(self, table_name, values):
        with self.engine.connect() as conn:
            stmt = insert(table_name).values(values)
            result = conn.execute(stmt)
            print(result)
