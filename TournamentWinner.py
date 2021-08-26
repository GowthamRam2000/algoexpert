HOME_team_winner_const = 1


def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == HOME_team_winner_const else awayTeam
        update_scores(winningTeam, 3, scores)
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam += winningTeam

    return currentBestTeam


def update_scores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


print(tournamentWinner([["python", "possy"], ["html", "css"], ["css", "html"]], [0, 0, 1]))
