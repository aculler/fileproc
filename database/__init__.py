import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import File, Job, Base

# TODO: Should probably make this code into a DatabaseController class so that we don't do all of the
# database setup as soon as we import the module. Maybe. we'll see.
engine = create_engine('sqlite:///files.db', echo=True)
Session = sessionmaker()
Session.configure(bind=engine)


def print_obj(obj):
    print('-> {0}'.format(type(obj)))
    for itm in [itm for itm in dir(obj) if not itm.startswith('_')]:
        print('--> {0}: {1}'.format(
            itm,
            getattr(obj, itm, None)
        ))


def create_schema():
    Base.metadata.create_all(engine)


def generate_test_data():
    session = Session()
    spec = json.loads(open('testdata.json', 'r').read())
    session.add_all([File(**subspec) for subspec in spec['files']])
    session.add_all([Job(**subspec) for subspec in spec['jobs']])
    session.commit()
