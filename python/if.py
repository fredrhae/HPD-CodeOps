#!/usr/bin/env python
score = input("Enter score: ")

score = int(score)

if score >= 8:
	grade = 'A'
else:
	if score >=7:
		grade = 'B'
	else:
		grade = 'C'
print("\n\nSua nota é: %s" % grade)
