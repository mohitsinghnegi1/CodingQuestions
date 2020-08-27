
# QUs: https://discuss.codechef.com/t/google-online-coding-challenge-internship-2021-#cutoff-score-how-many-question-req/75163


#learned new property of mod in python
print (5-7)%6

#after rotation we get a net value we can take its mode 
print (1-8%6)%6

#correct postion on rotation
print (-2)%6

#problem to solve this question asked in google
#keep track of left and right rotation and keep a net rotation -ve for left and +ve for #right
# when ever we are asked to update or need that position value we will find access that by using v[(cur+netRotation%n)%n]
