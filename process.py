import re
from hashlib import md5

import magic

from database.models import File, Session

session = Session()

def parse_metadata(file_obj, job):
    match = re.search(
        r'([a-z0-9 ]+)\.([a-z0-9]+)$',
        file_obj.abs_path.split('/')[-1],
        re.I
    )
    filename = match.group(1)
    extension = match.group(2)

    file_type = magic.from_file(file_obj.abs_path)
    mime_type = magic.from_file(file_obj.abs_path, mime=True)

    print('filename: {0}'.format(filename))
    print('extension: {0}'.format(extension))
    print('file_type: {0}'.format(file_type))
    print('mime_type: {0}'.format(mime_type))

def hash_file():
    pass

def main():
    # Parse the metadata for any files that are missing it.

    # Grab a file for hashing
    for item in session.query(File).filter_by(md5=None):
        pass
