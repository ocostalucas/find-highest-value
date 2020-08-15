import time

def extractor(filename):
    archive = open(filename, "r")
    data = archive.read().split('\n')[:-1]
    archive.close()
    return [int(i) for i in data]

def program(filename):
    start = time.time()
    content = extractor(filename+'.csv')
    larger = max(i for i in content)
    finish=str((time.time() - start)*1000) 
    return larger 

print(program('dataset-2-b'))
