from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("postgresql://rrbiapgaaqfsaj:b882a5415e5c61a7a245025740bad77eca762a0cfc56a3b5f40a82bd6409c4bd@ec2-34-225-159-178.compute-1.amazonaws.com:5432/d74dnoel36fu3q")
Session = sessionmaker(bind=engine)