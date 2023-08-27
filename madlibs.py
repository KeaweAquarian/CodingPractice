#strings
# the_str = "hi"

# print("I said " + the_str)

# print("I said {}".format(the_str))

# print(f"I said {the_str}")

name = input("name")
name2 = input('name')
title = input("title")
course = input("course")
verb = input("nverb")
noun = input("noun")
noun2 = input("noun")
verb2 = input("verb")
place = input("place")
place2 = input("place")
verb4 = input("verb")
noun4 = input("noun")
noun3 = input("noun")
madlib = f"Albert Einstein, the son of {name} and {name2},\
was born in Ulm, Germany, in 1879. In 1902, he had a job\
as assistant {title}.in the Swiss patent office and attended\
the University of Zurich. There he began studying atoms, molecules,\
and {course}. He developed the theory of\
{verb}.relativity, which expanded the phenomena of sub-atomic\
{noun}.and {noun2}.magnetism. In 1921,\
he won the Nobel prize for {verb2}.and was director of\
theoretical physics at the Kaiser Wilhelm {noun3}.in Berlin.\
In 1933, when Hitler became Chancellor of {place},\
Einstein came to America to take a post at Princeton Institute for\
{verb4}, where his theories helped America devise the first\
atomic bomb. There is no question about it: Einstein was\
one of the most brilliant {noun4}.of our time."

print(madlib)