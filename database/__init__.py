from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# TODO: Should probably make this code into a DatabaseController class so that we don't do all of the
# database setup as soon as we import the module. Maybe. we'll see.
engine = create_engine('sqlite:///files.db', echo=True)
Session = sessionmaker()
Session.configure(bind=engine)
