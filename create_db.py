from sqlalchemy import create_engine
from src.settings import DB_URI
from src.models import Base


if __name__ == "__main__":
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
