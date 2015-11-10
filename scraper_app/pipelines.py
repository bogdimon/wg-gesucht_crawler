from sqlalchemy.orm import sessionmaker
from models import Entries, db_connect, create_entries_table


class WGGesuchtPipeline(object):
    """Livingsocial pipeline for storing scraped items in the database"""
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_entries_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        entry = Entries(**item)

        try:
            session.add(entry)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item