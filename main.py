import time

def extractor(filename):
    archive = open(filename, "r")
    data = archive.read().split('\n')[:-1]
    archive.close()
    return [int(i) for i in data]

def output(filename,larger, time):
    archive = open('resposta-'+filename+'.txt','w')
    archive.write(larger)
    archive.write(time)
    archive.close() 

def program(filename):
    start = time.time()
    content = extractor(filename+'.csv')
    larger = max(i for i in content)
    finish=str((time.time() - start)*1000)
    output(filename, str(larger) + '\n', str(finish)) 

program('dataset-2-a')
program('dataset-2-b')
program('dataset-2-c')
program('dataset-2-d')
program('dataset-2-e')