from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np
import pandas as pd

def score(mentor, mentee):
  score = 0
  for r,e in zip(mentor,mentee):
    score+=abs(r-e)
  return score

class Assign(APIView):

	def get(self,request,format=None):
		'''
		Data Format ->
		Fields: ['field1','field2'...]
		Mentors:
		{
		name: [xx,xx,...] (llength = length of fields)
		}
		Menntees:
		{
		name: [xx,xx,...] (llength = length of fields)
		}
		'''
		data = {
		"mentors": {
		"1":[24,35,75],
		"2":[54,76,94],
		"3":[4,67,34]
		},
		"mentees":{
		"1":[24,35,75],
		"2":[54,76,94],
		"3":[4,67,34]
		}
		mentors = data['mentors']
		mentees = data['mentees']
		if mentors != None and mentees != None:
			if len(mentors) == len(mentees):
				preferences = []
				for mentee_name,mentee_fields in mentees.items():
					mentor_matches = {}
					for mentor_name, mentor_fields in mentors.items():
						s = score(mentor_fields,mentee_fields)
						mentor_matches[mentor_name] = s
					preferences.append(mentor_matches)
				matrix = np.array(pd.DataFrame(preferences))
				return Response(matrix,status=status.HTTP_200_OK)
		return Response(None,status=status.HTTP_400_BAD_REQUEST)