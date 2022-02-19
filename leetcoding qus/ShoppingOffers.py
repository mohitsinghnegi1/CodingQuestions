
def helper(price,special,needs,i=0):
    #we are calculating max possible value first then later w
    #we will try all possible offers to mimimise the cost as much as possible
    min_price=sum(p*n for p,n in zip(price,needs))
    #min_price will store min cost to buy needed items
    
    #k will bassically keep track of what offer we can't add will move to next       #offer(not sure)
    k=i
    for offer in special[i:]:
        #apply offer if possible
        #temp will store updated need after adding valid offer
        temp=[]
        for i in range(len(needs)):
            if(needs[i]-offer[i]<0):
                temp=None
                break
            temp.append(needs[i]-offer[i])
        if(temp!=None):
            #we are using vvalid offer value to calclate price and 
            #min_price will see if we can apply offer to reduce needs total price
            min_price=min(min_price,offer[-1]+helper(price,special,temp,k))
        k+=1
        
    return min_price


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        
        #this function will return minmum price
        return helper(price,special,needs)