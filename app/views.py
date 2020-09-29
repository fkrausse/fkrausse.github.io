from flask import render_template, request, make_response
from main import app

@app.route('/')
def index():
    user_ip = request.remote_addr
    response= make_response(render_template('index.html'))
    response.set_cookie('user_ip', user_ip)
    return response
