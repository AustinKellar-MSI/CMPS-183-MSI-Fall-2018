# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

# logger.info("The user record is: %r" % auth.user)

import datetime


def get_current_time():
    return datetime.datetime.utcnow()

db.define_table(
    'movies',
    Field('title'),
    Field('description', 'text'),
    Field('image', 'upload'),
    Field('date_posted', 'datetime', update=get_current_time())
)

db.movies.id.readable = False
db.movies.date_posted.readable =  db.movies.date_posted.writable = False

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
