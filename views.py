"""
nba views
"""
import random
from pathlib import Path
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from .nba_utils.view_helpers import report
from rest_framework.response import Response
from rest_framework.decorators import api_view

### Global Constants ###
n_players = 20
current_dir = f"{Path(__file__).parent.absolute()}"

@api_view(['GET'])
def fetch_players(request, *args, **kwargs) -> HttpResponse:
    """
    Fetches 20 random players and sends their information {points, name, rebounds, img, assists, …} 
    to the frontend

    Inputs    
        :request: <HttpRequest> to fetch the players

    Outputs
        :returns: Status … 
                         … HTTP_200_OK if the players were fetched successfully
                         … HTTP_403_FORBIDDEN if the players were not fetched successfully
    """
    data = {}
    user_status = status.HTTP_200_OK
    try:
        with open(f"{current_dir}/stats.json", "r") as player_stats:
            player_stats = json.loads(player_stats.read())
            selected_players = random.sample(player_stats, n_players)

            data['players'] = selected_players
    
    except Exception as error: 
        user_status = status.HTTP_403_FORBIDDEN
        print(f"Error raised while fetching players\n{report(error)}")
    
    return Response(status = user_status, data = data)
