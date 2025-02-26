# The random module has pseudo-random number generators.
# Note: pseudo-random numbers mean that the numbers appear to be random, but in reality they aren't. Therefore, this module should not be used for security or cryptographic purpose. The reason for this is that when we have the same input and the same algorithm, the output can be predictable.
import random
import time
#Functions:

#1. seed
#   ->Initializes the random number generator ( hence "pseudo-random numbers")
random.seed(0)



#2. random.randrange(start, end, step)
#   -> Generates an integer within a specified range 

r_range = random.randrange(10, 20, 3)
print(r_range)

#3. random.randint(start, end) 
# -> Generates an integer within a specified range "without a step"
r_int = random.randint(10, 20)
print(r_int)

#4. random.uniform(start, end)
#  -> Generates a random floating-point number within a range "without a step"

r_uniform = random.uniform(10, 20)
print(r_uniform)

#5. random.shuffle(Mutable Sequence) -> shuffles the original list

names = ['Ailton', 'Maria', 'Helena', 'Joana', 'Darc', 'Luiza']
random.shuffle(names)
print(names)

#6. random.sample(iterable, k=N)
#   -> Selects elements from an iterable and returns another iterable (NO REPEATS *)
new_names = random.sample(names, k=2)
print(new_names)

#7. random.choices(iterable, k=N)
#   -> Chooses elements from iterable and returns another iterable(REPEATS*)

new_names1 = random.choices(names, k=3)
print(new_names1)

#8. random.choice(iterable)
#   -> Choice an element from iterable
print(random.choice(names))