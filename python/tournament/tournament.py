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
        team1, team2, result = row.split(";")
        for team in [team1, team2]:
            if team not in results:
                results[team] = Result(team)
        if result == "win":
            results[team1].W += 1
            results[team2].L += 1
        if result == "loss":
            results[team1].L += 1
            results[team2].W += 1
        if result == "draw":
            results[team1].D += 1
            results[team2].D += 1
    output = []
    output.append("Team                           | MP |  W |  D |  L |  P")
    for team, result in sorted(results.items(), key = lambda v: (-v[1].points, v[0]), reverse=False):
        output.append("{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}".format(team, result.played, result.W, result.D, result.L, result.points))
    print(output)
    return output