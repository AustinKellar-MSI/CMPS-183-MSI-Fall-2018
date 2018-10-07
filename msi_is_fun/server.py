from bottle import run, get, static_file # these are the only functions you need

# your code goes here
@get('/images/<filename:path>')
def send_image(filename):
    return static_file(filename, root='images/')

@get('/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root='css/')

@get('/msi')
def msi():
    return static_file('my_view.html', root='views')

run(host='localhost', port=8080, debug=True)
