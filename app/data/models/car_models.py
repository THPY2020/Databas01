from app.data.db import Base
import sqlalchemy as sa


class CarModels(Base):

    __tablename__ = 'car_models'

    id = sa.Column(sa.Integer, primary_key=True)
    car_brand = sa.Column(sa.String(100), nullable=False)
    model_name = sa.Column(sa.String(100), nullable=False)
    production_year = sa.Column(sa.String(100), nullable=False)
    colour = sa.Column(sa.String(45), nullable=True)
    # TODO: Make many->many relations with products and car_models

    def __repr__(self):
        return f'CarModels(id={self.id}, car_brand={self.car_brand}, model_name{self.model_name},' \
               f'production_year={self.production_year}, colour={self.colour})'