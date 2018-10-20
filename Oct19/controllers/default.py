# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    movies = db(db.movies).select()
    return dict(movies=movies)

def edit(): 
    form = SQLFORM(db.movies, request.args[0])
    if form.process().accepted:
        redirect(URL('default', 'index'))
    logger.info("My session is: %r" % session)
    return dict(form=form)

def delete():
    db(db.movies.id == request.args[0]).delete()
    redirect(URL('default', 'index'))

def insert():
    # Your code goes here
    # Hints:
    #   - Use the SQLFORM function that Luca showed in class on Friday
    #   - You can see an example here:
    #       https://bitbucket.org/luca_de_alfaro/web2py_start/src/2f66f185a80a19f73dd1a83c1a6fd32157d8d378/controllers/default.py?at=oct-12-2018&fileviewer=file-view-default

    form = SQLFORM(db.movies)
    if form.process().accepted:
        redirect(URL('default', 'index'))
    logger.info("My session is: %r" % session)
    return dict(form=form)

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


