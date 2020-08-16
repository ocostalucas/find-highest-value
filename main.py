from matplotlib import pyplot as plt
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
    return finish

def plot():
    datasets = ['a', 'b', 'c', 'd', 'e']
    times = [float(program('dataset-2-'+i)) for i in datasets]
    plt.plot(datasets, times)
    print(times)
    plt.show()    

plot()