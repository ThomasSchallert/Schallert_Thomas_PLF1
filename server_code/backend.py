import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def get_gefaengnisse():
  conn = sqlite3.connect(data_files["prison_management.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("Select Name, GID from Gefängnis"))
  return res
@anvil.server.callable
def get_verwaltung(rows="*"):
  conn = sqlite3.connect(data_files["prison_management.db"])
  cursor = conn.cursor()
  res = list(cursor.execute(f"Select {rows} from Verwaltung"))
  return res
@anvil.server.callable
def get_zellen():
  conn = sqlite3.connect(data_files["prison_management.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("Select Zellennummer, ZID from Zellen"))
  return res
@anvil.server.callable
def get_ZelleHaeftlinge():
  conn = sqlite3.connect(data_files["prison_management.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("Select ZID, HID from ZelleHäftlinge"))
  return res
def get_Haeftlinge():
  conn = sqlite3.connect(data_files["prison_management.db"])
  cursor = conn.cursor()
  res = list(cursor.execute("Select Häftlingsnummer, Haftdauer from Häftlinge"))
  return res