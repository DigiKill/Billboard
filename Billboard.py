import sqlite3
import datetime
import logging
from flask import Flask
from BillboardDAO import dataAccessDAO as db

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s [%(name)-18s] %(message)s',
                    datefmt='%m-%d %H:%m',
                    filename='.\\Logs\\serverlog.txt',
                    filemode='w')

log = logging.getLogger('Server_Run_Log')
log.debug('Application Started')
log2 = logging.getLogger('Secondary_Log')
log2.info('This is a second logger.')

app = Flask(__name__)

conn = sqlite3.connect('./Database/billboard-db.db')
c = conn.cursor()
d = datetime.date.today().strftime("%Y-%m-%d")


if not db.table_exist(c, 'events'):
    print("Event Table not found.")
    if db.create_table(c):
        log.error('Event Table not found and was created.')
        print("Event Table Created Successfully.")
    else:
        log.error('Event Table not found and was unable to be created.')
        print("Error Creating Event Table.")
else:
    log.debug('Event Table was found.')
    print("Event Table found.")


@app.route('/')
def index():
    return '<h1>This is the index page: '+ d + '</h1>'


if __name__== '__main__':
    app.run()

