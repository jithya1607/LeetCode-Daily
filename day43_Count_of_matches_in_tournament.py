#43 Count of matches in tournament
# Count the number of matches played in a tournament where n teams participate. If even number of teams, each team plays with another team. If odd number of teams, one team gets a bye (does not play, and moves to the next round) and the rest play. Return the number of matches played until a winner is decided.
def numberOfMatches(n):
    m=0
    while n!=1:
        if n%2==0:
            n//=2
            m+=n
        else:
            m+=(n-1)/2
            n=(n-1)/2+1
    return int(m)