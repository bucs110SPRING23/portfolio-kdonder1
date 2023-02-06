import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

#my class variables:
calculus = 3
print("calculus:", calculus, type(calculus))
computerscience = 3
print("computerscience:", computerscience, type(computerscience))
physics = 6
print("physics:", physics, type(physics))
linearalgebra = 3
print("linearalgebra:", linearalgebra, type(linearalgebra))
research = 2
print("research:", research, type(research))

# final calculations:
classes_per_week = calculus + computerscience + physics + linearalgebra + research
cost_per_class = cost_per_week / classes_per_week
print(f"Your classes cost ${cost_per_class:.2f} each! Make sure to get your money's worth by attending all of them!")

print()

# Part B
randomlist = ("class", 6, "raquetball", 365, int(25 /5), float(297 / 36), "helloworld", float(36 / 5), int(99), 27)
diceroll = random.choice(randomlist)
print("randomness for today:", diceroll)