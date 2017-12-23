
def create_table(con):
    try:
        con.execute('''CREATE TABLE events
                    (event_id text not null, event_date date not null, event_description text, primary key (event_id))''')
        return True
    except:
        return False


def table_exist(con, tname):
    value = tname,
    con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", value)
    rs = con.fetchone()
    if rs is None:
        return False
    else:
        return True

