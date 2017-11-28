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
    session.add_all([
        File(abs_path='/home/andy/Music/Audioslave/Audioslave/Audioslave - I Am the Highway.mp3'),
        File(abs_path='/home/andy/Music/Audioslave/Audioslave/Audioslave - Light My Way.mp3', md5='f9601a71078daaa2e999fe344ea49c00'),
        File(abs_path='/home/andy/Music/Audioslave/Audioslave/Audioslave - Exploder.mp3', name='Audioslave - Exploder', ext='mp3', md5='4a95b7c48f638bb39c11dd0b32809692')
    ])

    session.add_all([
        Job(type='metadata', file_id=1)
    ])

    session.commit()
