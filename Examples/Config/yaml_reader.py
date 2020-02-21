import yaml

with open('experiment_test.yml', 'r') as f:
	e = yaml.load(f)

print (e['Experiment'])
for k in e['Experiment']:
	print(k)
	print(e['Experiment'][k])
	print(10*'-')

