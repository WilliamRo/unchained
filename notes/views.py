from django.http import HttpResponse
from django.template import loader
from notes.models import Note


def index(request, note_id=None):
  if note_id is None:
    if len(Note.objects.all()) > 0: note = Note.objects.all()[0]
    else: note = None
  else:
    notes = Note.objects.filter(pk=note_id)
    if len(notes) == 1: note = notes[0]
    else: note = None

  template = loader.get_template('index.html')
  context = {
    'note': note,
    'previous': note.previous if note else None,
    'next': note.next if note else None,
  }
  return HttpResponse(template.render(context, request))

