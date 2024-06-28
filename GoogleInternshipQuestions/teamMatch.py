from collections import defaultdict
groups = [[1,2,6,5],[3,4,7,8]]

countries = {
    "itly":[1,2,3],
    "germany":[4,5],
    "france":[6],
    "cicago":[7,8]
}


def solve(groups,countries):

    teamToGroupMap = {}

    for groupNo in  range(len(groups)):
        for team in groups[groupNo]:
            teamToGroupMap[team] = groupNo


    print(teamToGroupMap)
    teamToCountryMap = {}


    for countrie in  countries:
        for team in countries[countrie]:
            teamToCountryMap[team] = countrie

    print(teamToCountryMap)

    PossibleMatches = {}  # outdegree
    indegreeMap = defaultdict(set) # which was possible map to me

    for team in teamToGroupMap:
        PossibleMatches[team]  = set(teamToGroupMap.keys()) - set(countries[teamToCountryMap[team]]).union(set(groups[teamToGroupMap[team]]))

        for team2 in PossibleMatches[team]:
            indegreeMap[team2].add(team)

    print(indegreeMap)
    print(PossibleMatches)

    out = []

    def greedyFind():

        if(len(PossibleMatches)==0):
            return True

        if(len(PossibleMatches)%2==1):
            return False


        smallestKey = None
        smallestVal = None

        for key in PossibleMatches:

            if(smallestKey==None or len(PossibleMatches[smallestKey])>len(PossibleMatches[key])):
                smallestKey = key

                if(PossibleMatches[key]==[]):
                    return False


                smallestVal = PossibleMatches[key].pop()
                PossibleMatches[key].add(smallestVal)

        # now we know the smallest Key value , remove them from mappings

        del PossibleMatches[smallestKey]
        del PossibleMatches[smallestVal]

        # clear the maps

        for team in indegreeMap[smallestKey]:
            if(team not in PossibleMatches):continue
            PossibleMatches[team].discard(smallestKey)
            if(len(PossibleMatches[team])==0):
                return False

        for team in indegreeMap[smallestVal]:
            if(team not in PossibleMatches):continue
            PossibleMatches[team].discard(smallestVal)
            if(len(PossibleMatches[team])==0):
                return False

        out.append([smallestKey,smallestVal])

        return greedyFind()



    if(greedyFind()):
        return out

    return []


print(solve(groups,countries))

















# ans =

# 1 can match up with which all teams  ?

# 1: set(teams) - countries[1].intersection(group[1]) =  6 - 3 - 3



# 1: [4,5]
# 2: [4,5]
# 3: [6]
# 4: [1,2,6]
# 5: [1,2,6]
# 6: [3,4,5]



# 3->6 (remove 3 from map and remove 3 and 6 from all other outdegree)

# which all teams were possibly match with 6?
# indegreeMap 6:[4,5,3]  , 3: [6]

#     How we removed? using indegreeMap

# 1: [4,5]
# 2: [4,5]
# 4: [1,2]
# 5: [1,2]


# 1-> 4  (remove 1 from map and remove 4 and 1 from all other outdegree)
#    indegreeMap 1:[4,5]  , 4: [1,2]


# 2: [5]
# 5: [2]

# 2-> 5  (remove 2 from map and remove 5 and 2 from all other outdegree)
#     indegreeMap 2:[4,5]  , 5: [1,2,6]


# [3,6],[1,4],[2,5]











