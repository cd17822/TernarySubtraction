from baseconv import BaseConverter
import random

primary_numbers = []
secondary_numbers = []
outputs = []

for i in xrange(25):
	ternary_string1 = ""
	for j in xrange(random.randint(50, 100)):
		ternary_string1 += str(random.randint(0,2))

	ternary_string2 = ""
	for j in xrange(random.randint(50, 100)):
		ternary_string2 += str(random.randint(0,2))

	base3 = BaseConverter("012")
	decimal_string1 = base3.decode(ternary_string1)
	decimal_string2 = base3.decode(ternary_string2)
	decimal_output = int(decimal_string1) - int(decimal_string2)
	ternary_output = base3.encode(str(decimal_output))

	input = ternary_string1 + "#" + ternary_string2
	expected_output = ternary_output

	print "Input:"
	print input
	print "Expected Output:"
	print expected_output
	print
