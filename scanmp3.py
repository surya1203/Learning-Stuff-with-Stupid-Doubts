import os
import fnmatch
import id3reader_p3 as id3reader


def get_songs(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolutepath = os.path.abspath(path)
            yield os.path.join(absolutepath, file)


for f in get_songs('music', 'emp3'):
    error_files = []
    try:
        id3r = id3reader.Reader(f)
        print('Artist: {}, Album: {}, Track:{}, Song: {}'.format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))

    except OSError:
        error_files.append(f)
    finally:
        next(get_songs('music', 'emp3'))
        for f in error_files:
            print(f)