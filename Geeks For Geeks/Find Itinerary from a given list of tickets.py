# Qus:https://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/

# time complexity O(n)

def printItinerary(dataSet):

    destSet = set(dataSet.values())
    # since there is only one src for a dest
    # the start node should not be in the destSet
    # find the starting point first
    start = None

    for src in dataSet:
        if(src not in destSet):
            start = src
            break

    # we got the starting node now do triversal

    while(src in dataSet):
        print src, "-> ", dataSet[src]
        src = dataSet[src]


dataSet = {}

dataSet["Chennai"] = "Banglore"
dataSet["Bombay"] = "Delhi"
dataSet["Goa"] = "Chennai"
dataSet["Delhi"] = "Goa"

printItinerary(dataSet)
