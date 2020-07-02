from flask import Flask, escape, request
import os
import logging

application = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    application.logger.handlers = gunicorn_logger.handlers
    application.logger.setLevel(gunicorn_logger.level)

@application.route('/')
def hello():
	app_name = os.environ.get('APP_NAME', 'Unable to get environment Value')
	return f'This response if from {app_name}'

@application.route('/request_info', methods=['GET', 'POST'])
def request_info():
	application.logger.info(f' request_info Request received \nHeaders \n{request.headers} Data\n {request.data}')
	return f'Headers {request.headers}'

@application.route('/stickyness')
def stickyness():
	pod_name = os.environ.get('POD_NAME', 'Unable to get environment Value')
	app_name = os.environ.get('APP_NAME', 'Unable to get environment Value')
	return f'{app_name} - This request is served by {pod_name}'

if __name__ == "__main__":
    application.run(host='0.0.0.0', port="80")
