# given an existing rank

rank = [120,100,90,90,80,70,75,60,60]
player = [70,80,105]

"""   An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

"""

def climbingLeaderboard(rank, player):
    ranked = list(set(rank))
    ranked.sort()
    n = len(ranked)
    i=0
    results = []
    
    for score in player:
        while i<n and ranked[i]<=score:
            i +=1
        results.append(n-i+1)
    return results

print(climbingLeaderboard(rank,player))