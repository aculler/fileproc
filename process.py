import re
from hashlib import md5

import magic

from database import Session
from database.models import File


def parse_metadata(fileid, jobid):
    session = Session()
    file_obj = session.query(File).filter(File.id == fileid).first()
    match = re.search(
        r'(.+)\.([a-z0-9]+)$',
        file_obj.abs_path.split('/')[-1],
        re.I
    )
    filename = match.group(1)
    extension = match.group(2)

    file_type = magic.from_file(file_obj.abs_path)
    mime_type = magic.from_file(file_obj.abs_path, mime=True)

    file_obj.name = filename
    file_obj.ext = extension
    file_obj.file_type = file_type
    file_obj.mime_type = mime_type
    session.commit()

def hash_file(file_obj, job):
    md5sum = md5(open(file_obj.abs_path, 'rb').read()).hexdigest()

    print('md5sum: {0}'.format(md5sum))

def main():
    # Parse the metadata for any files that are missing it.

    # Grab a file for hashing
    for item in session.query(File).filter_by(md5=None):
        pass
