import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import calculateGpaFromGrades, parsePDFFileToNotes, calculateAvgGpaFromGpas

# Create your views here.
class UcGradesToGpaView(APIView):
    def put(self, request):
        try:
            file_obj = request.data['file']
            grades = parsePDFFileToNotes(file_obj)
            gpas = calculateGpaFromGrades(grades)
            avg_gpa = calculateAvgGpaFromGpas(gpas)
            return Response(json.dumps({
                "notes": grades,
                "gpas": gpas,
                "avg_gpa": avg_gpa,
            }))
        except Exception:
            return Response(400)
