import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unchained.settings')
django.setup()

from notes.models import Note


# Clear table
print('>> Clearing Notes table ...')
Note.objects.all().delete()
print('>> Notes table has been cleared.')

# Insert notes
notes = [
  "A remote mysql database has been created and hosted on pythonanywhere.\n"
  " This tutorial shows how to access to the remote database when developing "
  "locally. \nYou may refer to https://github.com/WilliamRo/unchained.git for help.",
  'Step 1: Modify settings.py file. Install mysqlclient in your python '
  'environment. If you are using Windows system, install your ssh app.',
  'Step 2: Provide my.cnf file in the root. This file should be excluded from '
  'git cuz it contains the password of your database. Note that the host '
  'attribute in your local codes is different from that deployed on the cloud.'
  ' As for details, please ask William for help.',
  'Finally, if you want to modify the remote database, you must give your '
  'python code access to the remote database.',
]
for note in notes:
  n = Note(note_text=note)
  n.save()
print('>> Default notes inserted:')

for note in Note.objects.all():
  print('  [{}] {}'.format(note.pk, note.note_text))
