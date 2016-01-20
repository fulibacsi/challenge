import sqlite3


INSERT_STATEMENT = 'INSERT INTO {table_name} ({columns}) VALUES ({vals});'
SELECT_STATEMENT = 'SELECT {columns} FROM {table_name};'


def create(db_name, script_path):
    """ Creates data tables from the given script at script_path.

    Parameters:
    -----------
        db_name: str
            name of database database file
        script_path: str
            path for script

    Returns:
    --------
        None
    """
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        with open(script_path) as sql_file:
            for statement in sql_file.read().split('\n\n'):
                c.execute(statement)
        conn.commit()


def insert(db_name, table_name, columns, vals):
    # TODO: sanitize input!
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        c.execute(INSERT_STATEMENT.format(table_name=table_name,
                                          columns=columns,
                                          vals=vals))
        conn.commit()


def get_users(db_name):
    with sqlite3.connect(db_name) as conn:
        c = conn.cursor()
        c.execute(SELECT_STATEMENT.format(columns='*', table_name='profile'))
        return c.fetchall()


if __name__ == '__main__':
    create('example.db', './create.sql')
    import string
    for char in string.ascii_letters:
        insert('example.db',
               'profile',
               "'email', 'username', 'password'",
               "'{0}', '{0}', '{0}'".format(char))
    print(get_users('example.db'))
