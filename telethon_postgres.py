from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, LargeBinary, Boolean
from sqlalchemy.orm import sessionmaker
from telethon.sessions import StringSession

class PostgresSession(StringSession):
    def __init__(self, session_name, db_uri):
        super().__init__(None)
        self.engine = create_engine(db_uri)
        self.metadata = MetaData()
        self.table = Table(
            'telethon_sessions', self.metadata,
            Column('session_name', String, primary_key=True),
            Column('server_address', String),
            Column('port', Integer),
            Column('auth_key', LargeBinary),
            Column('layer', Integer),
            Column('api_id', Integer),
            Column('dc_id', Integer),
            Column('test_mode', Boolean),
            Column('date', Integer)
        )
        self.metadata.create_all(self.engine)
        self.session_name = session_name
        self.Session = sessionmaker(bind=self.engine)
        self.db_session = self.Session()

    def save(self):
        with self.db_session.begin():
            data = {
                'session_name': self.session_name,
                'server_address': self.server_address,
                'port': self.port,
                'auth_key': self.auth_key,
                'layer': self.layer,
                'api_id': self.api_id,
                'dc_id': self.dc_id,
                'test_mode': self.test_mode,
                'date': self.date
            }
            self.db_session.merge(self.table.insert().values(**data))

    def load(self):
        row = self.db_session.query(self.table).filter_by(session_name=self.session_name).first()
        if row:
            self.server_address = row.server_address
            self.port = row.port
            self.auth_key = row.auth_key
            self.layer = row.layer
            self.api_id = row.api_id
            self.dc_id = row.dc_id
            self.test_mode = row.test_mode
            self.date = row.date