import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
import sqlite3

class TestAlarmaApp(unittest.TestCase):

    def setUp(self):
        # Set up a Tkinter root window
        self.root = tk.Tk()
        self.root.title("Test")

    def tearDown(self):
        self.root.destroy()

    @patch('sqlite3.connect')
    def test_login_success(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = ("user", "pass")

        # Create a test instance of the login UI
        entry_username = tk.Entry(self.root)
        entry_password = tk.Entry(self.root, show="*")
        entry_username.insert(0, "user")
        entry_password.insert(0, "pass")

        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            login(entry_username, entry_password)
            mock_showinfo.assert_called_with("Login Successful", "Welcome user")

    @patch('sqlite3.connect')
    def test_login_failure(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None

        # Create a test instance of the login UI
        entry_username = tk.Entry(self.root)
        entry_password = tk.Entry(self.root, show="*")
        entry_username.insert(0, "user")
        entry_password.insert(0, "wrong_pass")

        with patch('tkinter.messagebox.showerror') as mock_showerror:
            login(entry_username, entry_password)
            mock_showerror.assert_called_with("Error", "Invalid Username or Password")

    @patch('sqlite3.connect')
    def test_register_success(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Create a test instance of the register UI
        register_window = tk.Toplevel(self.root)
        entry_fullname = tk.Entry(register_window)
        entry_email = tk.Entry(register_window)
        entry_phone = tk.Entry(register_window)
        entry_reg_username = tk.Entry(register_window)
        entry_reg_password = tk.Entry(register_window)

        entry_fullname.insert(0, "John Doe")
        entry_email.insert(0, "john@example.com")
        entry_phone.insert(0, "1234567890")
        entry_reg_username.insert(0, "johndoe")
        entry_reg_password.insert(0, "password")

        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            save_user(entry_fullname, entry_email, entry_phone, entry_reg_username, entry_reg_password)
            mock_showinfo.assert_called_with("Success", "User Registered Successfully")
            mock_cursor.execute.assert_called_with(
                "INSERT INTO users (fullname, email, phone, username, password) VALUES (?, ?, ?, ?, ?)",
                ("John Doe", "john@example.com", "1234567890", "johndoe", "password")
            )

def login(entry_username, entry_password):
    username = entry_username.get()
    password = entry_password.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        tk.messagebox.showinfo("Login Successful", "Welcome " + username)
    else:
        tk.messagebox.showerror("Error", "Invalid Username or Password")

def save_user(entry_fullname, entry_email, entry_phone, entry_reg_username, entry_reg_password):
    fullname = entry_fullname.get()
    email = entry_email.get()
    phone = entry_phone.get()
    username = entry_reg_username.get()
    password = entry_reg_password.get()
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (fullname, email, phone, username, password) VALUES (?, ?, ?, ?, ?)",
              (fullname, email, phone, username, password))
    conn.commit()
    conn.close()
    tk.messagebox.showinfo("Success", "User Registered Successfully")

if __name__ == '__main__':
    unittest.main()
