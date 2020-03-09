#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
## This fn adds n**2 + a at each step until it gets to n**3 starting first from 0
## But it’s not n**3 because we already are adjusting the constant by n**2
## Must be o(n) as we will only need to run this about an (n) number of times



b)
## This fn takes a loop for range of (n) and then has another constant and nested loop
## Internal loop is a while loop that takes the constant and *2 then adds to sum
## Both sum and j are constants and don’t change the loops too much
## The while loop only runs  about log(n) times as it doubles each step value towards (n) and stops once it equals (n) value
## This must be (n)log(n)



c)
## This fn takes the variable (bunnies) and then recursively returns the addition of 2 and the next lower value of (bunnies) until it gets to 0 returning 0 additional ears.
## This is o(n) as this addition happens for each step from (n) to 0


## Exercise II


Going from 0 to f at which point the first egg breaks since that floor is the proper height at which one will break. Starting from 0 and working our way up guarantees that the least amount of eggs will be broken. 

So it could look kinda like this below

Def broke-egs(n):
	count=0
	eggs=n**2
	eggs_b=0
	While count <= n and eggs==n**2:
		##input here asking if the dropped egg broke or not
		If didnt break:
			count+=1
			##egg not broke so doesn’t change number of eggs
		If did break:
			eggs-=1
		
	Return  count +1 ## this returns the count of dropped (also the floor number) and then the only broken egg
		
