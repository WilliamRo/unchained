from django.http import HttpResponse
import cv2


def index(request):
  return HttpResponse('Hello Rick.\nBreak your pillow.')