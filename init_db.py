import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unchained.settings')
django.setup()

from notes.models import Note


# Clear table
Note.objects.all().delete()

# Insert notes
n = Note(note_text='This is the 1st note.')
n.save()
n = Note(note_text='This is the 2nd note.')
n.save()
n = Note(note_text='This is the 3rd note. Stop press next button!')
n.save()
n = Note(note_text='The database is self-destroying ...')
n.save()
n = Note(note_text='Just kidding! Hahahahahahahaha')
n.save()

for note in Note.objects.all():
  print('> {}'.format(note.note_text))
