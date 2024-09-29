from bottle import run, route
import os

@route('/')
def index():
    page =  f'''
                <h1>Ping web app</h1>
                <p>Please add a host to the url to begin pinging.</p>
                <p>Such as http://127.0.0.1:8080/cnn.com</p>
            '''
    return page

@route('/<host>')
def index(host):
    try:
        response = os.popen(f'ping -c 1 {host}').read()
    except:
        response = 'Problem connecting.'
    finally:
        if response == '':
            response = 'Host could not resolve.'
        header = '<meta http-equiv="refresh" content = "5">'
        page = f''' {header}
                    <h1>{host}</h1>
                    <p>{response}</p>
                '''
        
        return page
    

run(host= '127.0.0.1', port=8080)