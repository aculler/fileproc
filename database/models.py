from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


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
    status = Column(String(50), default='pending')

    def __repr__(self):
        file_name = Session().query(File.name).filter(File.id == self.file_id).first()
        return "<Job (id={0} type={1} file_id={2} file_name={3}".format(
            self.id,
            self.type,
            self.file_id,
            file_name
        )
