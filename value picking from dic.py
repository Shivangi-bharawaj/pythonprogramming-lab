sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
for key, value in sampleDict['class']['student']['marks'].items():
    if key == 'history':
        print(value)