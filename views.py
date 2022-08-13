"""
crossword views
"""
from .models import Puzzle
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
