# prerequisite is compatible matplotlib 

from matplotlib import pyplot as plt

# still need to anticipate improper input like 'zero,' text, out of range, etc.

print('Hi! Let us draw a parabola. Please provide some attributes:')
a = float(input('    a:  '))
h = float(input('horizontal shift:  '))
c = float(input('vertical shift:  '))
xmin = 1.5
xmax = 1.5
while abs(float(xmin) - int(float(xmin))) > 0:
    xmin = input('Please enter an integer for X start:  ')
while abs(float(xmax) - int(float(xmax))) > 0:
    xmax = input('Please enter an integer for X end:  ')
width = abs(int(xmax) - int(xmin))
x = list(range(int(xmin), int(xmax)))
y = []
for i in range(0, width):
    y.append(a*((x[i]+h)*(x[i]+h))+c)

# create graph with matplotlib 
# more touch up of the graph output can be added here

plt.plot(x, y)
plt.vlines(0, int(xmin), int(xmax))
plt.hlines(0, int(xmin), int(xmax))
plt.ylim(int(xmin), int(xmax))
plt.xlim(int(xmin), int(xmax))
plt.legend(['y=a(x+h)^2+c'])
plt.show()

# display Y coordinate of parabola vertex
# can this be added to graph legend in dynamic manner?

if a < 0:
    print('Max Y is:  ', max(y))
else:
    print('Min Y is:  ', min(y))
