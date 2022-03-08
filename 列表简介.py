bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[2].title().lower())
bicycles[2] = 'asl'
print(bicycles)
bicycles.append('onett')
print(bicycles)
bicycles.pop(2)
print(bicycles)
bicycles.insert(2,'twott')
print(bicycles)
del bicycles[0]
print(bicycles)
bicycles.remove('twott')
print(bicycles)
bicycles.reverse()
print(bicycles)
print(len(bicycles))