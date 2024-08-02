from django.shortcuts import render, HttpResponse

from .engine.cleaning import CleanData
from .engine.attributes import calculate_player_abilities

import pandas as pd

# Create your views here.


def index(request):
    return render(request, 'index.html')


def upload_squad(request):
    print(request.FILES)
    squad = request.FILES.get('squad')
    if squad:
        df = pd.read_html(squad)[0]

        cd = CleanData()

        df = cd.clean_data(df)

        calculate_player_abilities(df)

        squad_wages = [
            {'name': x[0], 'wage': x[1]} for x in df[['Name', 'Wage']].to_numpy()
        ]

    context = {
        'filename': squad.name,
        "squad_wages": squad_wages,
    }

    return render(request, 'partials/squad_analysis.html', context)
