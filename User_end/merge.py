import pyodbc

class Database:
    def __init__(self, title, author, edition, update_callback):
        self.title = title
        self.author = author
        self.edition = edition
        self.update_callback = update_callback
        self.con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/musta/OneDrive/Desktop/Digital_library_project/digital_library.accdb;'
        self.conn = pyodbc.connect(self.con_string)
        self.cursor = self.conn.cursor()

    def insert(self):
        try:

            myuser = (
                (self.title, self.author, self.edition),
            )
            self.cursor.executemany('INSERT INTO Library_base (Book_Name, Author_Name, Edition) VALUES (?,?,?)', myuser)
            self.conn.commit()
            print('Data Inserted')
            self.update_callback("Data Inserted!")

        except Exception as e:
            self.update_callback("Error in connection. Please contact the service provider.")

    def threshold(self):
        try:
            table_name = "Library_base"
            search_book = "Book_Name"
            search_author = "Author_Name"
            search_edition = "Edition"

            query = f"SELECT * FROM {table_name} WHERE {search_book} =? AND {search_author} =? AND {search_edition} =?"
            self.cursor.execute(query, (self.title, self.author, self.edition))

            # fetch the results
            rows = self.cursor.fetchall()

            if rows:
                self.update_callback("Data is already existed")
            else:
                self.update_callback("No data found!")
        except Exception as e:
            print(f"AN error has occured: {e}")
            self.update_callback("Error in connection. Please contact the service provider.")


class SearchDB:
    def __init__(self, title="", author="", edition=""):
        self.title = title
        self.author = author
        self.edition = edition

        self.con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/musta/OneDrive/Desktop/Digital_library_project/digital_library.accdb;'
        self.conn = pyodbc.connect(self.con_string)
        self.cursor = self.conn.cursor()

    def search(self):
        try:
            table_name = "Library_base"
            search_book = "Book_name"
            search_author = "Author_name"
            search_edition = "Edition"

            if self.edition == "":
                query = f"SELECT * FROM {table_name} WHERE {search_book} = ? AND {search_author} = ?"
                self.cursor.execute(query, (self.title, self.author))
            elif self.author == "":
                query = f"SELECT * FROM {table_name} WHERE {search_book} = ? AND {search_edition} = ?"
                self.cursor.execute(query, (self.title, self.edition))
            elif not self.author and not self.edition:
                query = f"SELECT * FROM {table_name} WHERE {search_book} = ?"
                self.cursor.execute(query, (self.title,))
            elif not self.title and not self.edition:
                query = f"SELECT * FROM {table_name} WHERE {search_author} = ?"
                self.cursor.execute(query, (self.author,))
            else:
                query = f"SELECT * FROM {table_name} WHERE {search_book} = ? AND {search_author} = ? AND {search_edition} = ?"
                self.cursor.execute(query, (self.title, self.author, self.edition))

            # fetch the results
            rows = self.cursor.fetchall()

            if rows:
                data = []
                for row in rows:
                    title = row.Book_name
                    author = row.Author_name
                    edition = row.Edition

                    data.append((title, author, edition))

                return data
            else:
                return []  # No data found, send an empty list

        except Exception as e:
            print(f"An error has occurred: {e}")
            return "Error in connection. Please contact the service provider."


if __name__ == "__main__":
    database = Database("DATA COMMUNICATION AND COMPUTER NETWORKS ", "Rajneesh Agrawal, Bharat Bhushan Tiwari, ", "2nd")
    # database.insert()
    database.threshold()