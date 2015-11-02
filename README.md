# Cycle-of-pirates

I forgot to copy the word problem for this one, so I'll have to recreate what 
it said. The storyline for all these problems is that there is an evil doctor, 
Dr. Boolean, 
who wants to capture rabbits and turn them into zombies. In order to get to 
Dr. Boolean's lair, you come to a bar and have to ask the pirates sitting at 
the bar for directions to the lair. The pirates fill up the seats at the bar, 
and each of them have a tattoo of a number (all unique) on their arm. You 
start with th pirate with 0 tattooed on his arm, and ask him where the lair is. 
He says he doesn't know, but tells you the tattoo number of a pirate that you 
should ask. You go to that pirate, and says something similar. So you will 
go from pirate to pirate asking where the lair is. Each pirate tells you one and 
only one other pirate to ask, and no pirate directs you back to himself. Since 
there are (we are assuming) a finite number of pirates at the bar, you will 
eventually start going in a loop. 

This question asked, given that you start at pirate 0, what is the length of 
the loop that you end up in? For instance if the redirection goes 
0 -> 1 -> 2 -> 1, the length of the loop would be 2; 0 would not be included in 
this loop.

You are asked to define a function answer(numbers) in either python or 
javascript that took in a list of integers representing where the pirates 
redirect you to, and returns the length of the loop that you end up in. The 
input numbers represents the redirection information in the following way. 
The integer n in the list numbers having index i means that the pirate with 
the number i tattooed on his arm redirects you to the pirate with the number 
n tattooed on his arm. 

The script cycle.py was my solution to this problem.
