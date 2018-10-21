import datetime

def get_current_time():
    return datetime.datetime.utcnow()

db.define_table('movies',
                Field('title'),
                Field('description', 'text'),
                Field('image', 'upload'),
                Field('post_time', 'datetime', update=get_current_time()),
                )