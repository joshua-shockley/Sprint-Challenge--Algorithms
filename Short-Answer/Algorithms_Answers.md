#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) running time should really be o(1) since the running is only going to run up until it gets to the value set as n^3.. its getting to its goal with increasing increments


b) o(n) this is linear its just multiplying each item in a specific range number until getting to the value of the value just less than the input... this is linear o(n)


c) this recursively adds the bunnies value returned to 2 while decreasing the input along the way... o(log(n))

## Exercise II


has f number of floors 
has e number of broken eggs
has be number of broken eggs

doesnt get broke at f and below

to minimize the amount of broken eggs well start with the lowest level and increment by one each time this repeats until an egg breaks and determine the value of that f by adding the number of broken eggs and what number of egs were droped. 

this would be linear since as we loop though the floors we are just doing simple math to add the 2 values into a sum.. stopping when the first egg breaks.