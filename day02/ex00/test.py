from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce

test = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Proin aliquam elit ut nulla tempor, a suscipit tellus pulvinar.
Praesent aliquam, mauris eget blandit elementum, diam nisi cursus eros,
nec consequat felis ipsum sit amet nunc.
Aenean dolor mi, finibus nec ullamcorper non,
pretium et felis. Nulla porttitor tortor turpis,
vitae sodales velit blandit sit amet.
Pellentesque orci lacus, aliquam ut tincidunt et, volutpat vitae felis.
Phasellus vel magna id mauris elementum vestibulum ut non dui.
Mauris eleifend pellentesque ipsum accumsan tristique.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Aliquam quis faucibus felis. """
print(list(filter(lambda a: a > 8, range(0, 20))))
print((ft_filter(lambda a: a > 8, range(0, 20))))
print (42 * "#")
print(test)
print (42 * "#")
print(" ".join(list(map(str.capitalize, test.split(" ")))))
print (42 * "#")
print(" ".join(ft_map(str.capitalize, test.split(" "))))
print (42 * "#")
print(reduce(lambda a, b: a * b, range(80, 94)))
print(ft_reduce(lambda a, b: a * b, range(80, 94)))
