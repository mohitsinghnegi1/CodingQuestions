# Design a load balancer which implements following methods:
# add(n) where n is id of instance
# remove(n) where n is id of instance
# getRandom() which returns a random instance.
# All these operation should be of order O(1).


class LoadBalancerInstance:
    def __init__(self, id):
        self.id = id

class LoadBalancer:

    def __init__(self):
        self.instances = {}






    def add(self,instanceId):
        self.instances[instanceId] = LoadBalancerInstance(instanceId)

    def remove(self,instanceId):
        del self.instances[instanceId]
       

    def getRandom(self):
        return self.instances[random.choice(list(self.instances.keys()))]
        # for weighted random thing we need to first take a cumalative sum of all the weights and then choose a random number between 0 and sum of weights.


