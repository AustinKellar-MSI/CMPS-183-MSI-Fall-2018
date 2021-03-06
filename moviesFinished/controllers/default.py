import datetime

def index():
    movies = db(db.movies).select()
    return dict(movies=movies)

def insert():
    form = SQLFORM(db.movies)
    if form.process().accepted:
        redirect(URL('default', 'index'))
    return dict(form=form)

def edit():
    form = SQLFORM(db.movies, db.movies(request.args(0)))
    if form.process().accepted:
        redirect(URL('default', 'index'))
    return dict(form=form)

def delete():
    db(db.movies.id == request.args[0]).delete()
    return redirect(URL('default', 'index'))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


