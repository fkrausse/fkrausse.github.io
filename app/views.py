from flask import render_template, request, make_response
from main import app

@app.route('/')
def index():
    user_ip = request.remote_addr
    response= make_response(render_template('sobre.html'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/historia')
def historia():
    user_ip = request.remote_addr
    response= make_response(render_template('historia.html'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/article')
def article():
    user_ip = request.remote_addr
    response= make_response(render_template('article_1.html'))
    response.set_cookie('user_ip', user_ip)
    return response

@app.route('/article2')
def article2():
    user_ip = request.remote_addr
    response= make_response(render_template('article_2.html'))
    response.set_cookie('user_ip', user_ip)
    return response
