from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from . import Session, engine

Base = declarative_base()


class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    ext = Column(String(50))
    abs_path = Column(String(255))
    file_type = Column(String(100))
    mime_type = Column(String(100))
    md5 = Column(String(32))

    def __repr__(self):
        return "<File (name={0}, path={1}, md5={2})>".format(
            self.name,
            self.abs_path,
            self.md5 or ''
        )


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    type = Column(String(50))
    file_id = Column(Integer, ForeignKey('files.id'))

    def __repr__(self):
        file_name = Session().query(File.name).filter(File.id == self.file_id).first()
        return "<Job (id={0} type={1} file_id={2} file_name={3}".format(
            self.id,
            self.type,
            self.file_id,
            file_name
        )


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
