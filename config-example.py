ENVIRONMENT = 'development'
DB = {
    'development': {
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite3',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    },
    'production': {
        'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}'.format(
            username="<username from the PythonAnywhere Databases tab>",
            password="<password you set on the PythonAnywhere Databases tab>",
            hostname="<database host address from the Databases tab>",
            databasename="<database name you chose e.g. yourusername$tutorial>"),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_POOL_RECYCLE': 299,
    }
}