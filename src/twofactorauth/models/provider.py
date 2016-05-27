import sqlite3
import logging
from os import path
from gi.repository import GdkPixbuf, Gtk
logging.basicConfig(level=logging.DEBUG,
                format='[%(levelname)s] %(message)s',
                )
class Provider:
    def __init__(self):
        self.conn = sqlite3.connect('/home/bilal/Projects/Two-factor-gtk/database.db')

    def add_provider(self, name, secret_code, image):
        t = (name, secret_code, image,)
        query = "INSERT INTO providers (name, secret_code, image) VALUES (?, ?, ?)"
        try:
            self.conn.execute(query, t)
            self.conn.commit()
        except Exception as e:
            logging.error(query)
            logging.error("Couldn't add a new provider to database")
            logging.error(str(e))

    def remove_from_database(self, id):
        query = "DELETE FROM providers WHERE id=?"
        try:
            self.conn.execute(query, (id,))
            self.conn.commit()
        except Exception as e:
            logging.error("Couldn't remove the application with id : %s", id)
            logging.error(str(e))

    def count_providers(self):
        c = self.conn.cursor()
        query = "SELECT COUNT(id) AS count FROM providers"
        try:
            data = c.execute(query)
            return data.fetchone()[0]
        except Exception as e:
            logging.error(query)
            logging.error("Couldn't fetch providers list")
            logging.error(str(e))
            return None

    def fetch_providers(self):
        c = self.conn.cursor()
        query = "SELECT * FROM providers"
        try:
            data = c.execute(query)
            return data.fetchall()
        except Exception as e:
            logging.error(query)
            logging.error("Couldn't fetch providers list")
            logging.error(str(e))
            return None

    def get_provider_image(self, image):
        img = Gtk.Image(xalign=0)
        directory = "/home/bilal/Projects/Two-factor-gtk/data/logos/"
        theme = Gtk.IconTheme.get_default()
        if path.isfile(directory + image) and path.exists(directory + image):
            img.set_from_file(directory + image)
        elif path.isfile(image) and path.exists(image):
            img.set_from_file(image)
        elif theme.has_icon(path.splitext(image)[0]):
            img.set_from_icon_name(path.splitext(image)[0],
                                    Gtk.IconSize.DIALOG)
        else:
            img.set_from_icon_name("image-missing", Gtk.IconSize.DIALOG)
        return img

    def get_latest_id(self):
        c = self.conn.cursor()
        query = "SELECT id FROM providers ORDER BY id DESC LIMIT 1;"
        try:
            data = c.execute(query)
            return data.fetchone()[0]
        except Exception as e:
            logging.error(query)
            logging.error("Couldn't fetch providers list")
            logging.error(str(e))
            return None