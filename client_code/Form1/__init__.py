from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties) 
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.get_current_verwaltung_data()
    
    self.repeating_zellen.items = self.get_zellendata()
    print(self.get_zellendata())
  def get_current_verwaltung_data(self):
    gefaengnisse = anvil.server.call('get_gefaengnisse')
    direktoren = anvil.server.call('get_verwaltung',"GID, direktor, freieZellen")
    for d in direktoren:
      if (d[0] == gefaengnisse[self.gefaengnisse_drop_down.selected_value -1][1]):
        self.label_direktor.text = d[1]
        self.label_freie_zellen.text = d[2]
  def gefaengnisse_drop_down_change(self, **event_args):
    self.get_current_verwaltung_data()
    self.repeating_zellen.items = self.get_zellendata()
  def get_zellendata(self):
    zellen = anvil.server.call('get_zellen')
    zellenhaeftlinge = anvil.server.call('get_ZelleHaeftlinge')
    anzahlh = 0
    newlist = []
    for z in zellen:
      for zh in zellenhaeftlinge:
        if (z[1] == zh[0]):
          anzahlh += 1
      toadd = {'zellennummer': z[0], 'anzahl_häftlinge': anzahlh},
      newlist.append(toadd)
    return newlist
    
                                   
    

 



  
 
