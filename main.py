from pythonnn import models

model = models.Sequential()
model.add([2, 'relu'])
model.add([4, 'relu'])
model.add([4, 'relu'])
model.add([2, 'cutoff'])

print(model.compile())
