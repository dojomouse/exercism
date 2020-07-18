class Result:
    def __init__(self, name):
        self.Name = name
        self.W = 0
        self.D = 0
        self.L = 0
    @property
    def played(self):
        return self.W + self.D + self.L
    @property
    def points(self):
        return self.W * 3 + self.D * 1

def tally(rows):
    #input is team1;team2;result\n
    #split on ;
    #create dict keyed with team, store wins, draws, losses.
    # Matches played and points can be calculated, although have to sort by points.
    results = {}
    for row in rows:
        team1, team2, outcome = row.split(";")
        for team in [team1, team2]:
            if team not in results:
                results[team] = Result(team)
        if outcome == "win":
            results[team1].W += 1
            results[team2].L += 1
        if outcome == "loss":
            results[team1].L += 1
            results[team2].W += 1
        if outcome == "draw":
            results[team1].D += 1
            results[team2].D += 1
    output = []
    ROW_FORMAT = "{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}"
    output.append(ROW_FORMAT.format("Team", "MP", "W", "D", "L", "P"))
    for team, result in sorted(results.items(), key = lambda v: (-v[1].points, v[0]), reverse=False):
        output.append(ROW_FORMAT.format(team, result.played, result.W, result.D, result.L, result.points))
    print(output)
    return output