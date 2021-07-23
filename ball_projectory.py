import matplotlib.pyplot as plt
def ball_trajectory(x):
  location = 10*x - 5*(x**2)
  return(location)

xs = [x/100 for x in list(range(201))]
print(xs)
ys = [ball_trajectory(x) for x in xs]
print(ys)
plt.plot(xs,ys)
plt.title("Ball trajectory")
plt.xlabel('Horizontal ball position')
plt.ylabel('Vertical ball position')
plt.axhline(y=0)
plt.show()
