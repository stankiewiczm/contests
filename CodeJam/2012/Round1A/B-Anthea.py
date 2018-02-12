from numpy import*

## Code jam 2012, round 1, question B. Kingdom Rush

filename = "B-test.txt"
FILE = open(filename, "r")
N = int(FILE.readline())

for k in range(N):
   levels = int(FILE.readline())    ## Number of levels in the game
   stars = []                       ## Number of stars required to complete a level with each rating [[]]

   L = 0       ## Number of levels completed
   S = 0       ## Number of stars earned
   
   for i in range(levels):
      stars.append( map(int, FILE.readline().split()) )
   print stars

   ## how???????
   # Need to get 2N stars (N levels), which will take num = 2N - K turns, where K is
   # the number of levels where both stars can be gained at once.
   # Do any levels were both can be completed at once first, or any levels
   # where only the 2-star part is left. Then, if only the 1-star part can be
   # completed on some levels, do the one that has the most inaccesible 2-star part.

   num = 2*levels
   possible = 1
      
   # For each level that is completed with both ratings at once, subtract 1
   # from num. If no level can be completed and there are still levels left,
   # possible == 0.

   while len(stars) > 0:
      for l in stars:
         if (l[0] <= S) and (l[1] <= S):
            S += 2
            num -= 1
            stars.pop(l)



      
   
   if possible == 0:
      print "Case #%d: %s"%(k+1, 'Too Bad')
   else:
      print "Case #%d: %d"%(k+1, num)

'''
   X = 0
   for x in stars:
      if (x[0] > 0) and (x[1] > 0):
         X += 1
         if X == len(stars):
            possible = 0
'''
