from django.db import models


class Note(models.Model):
  note_text = models.CharField(max_length=500)

  @property
  def previous(self):
    notes = [note for note in Note.objects.all() if note.pk < self.pk]
    if len(notes) > 0: return notes[0]
    return None

  @property
  def next(self):
    notes = [note for note in Note.objects.all() if note.pk > self.pk]
    if len(notes) > 0: return notes[0]
    return None

