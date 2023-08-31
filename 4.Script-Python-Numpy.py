import numpy
np_city = numpy.array([[12500000],[6300000],[3300000]])

print(list(np_city))
print(numpy.shape(list(np_city)))

print("Mediana = {}".format(numpy.mean(np_city,dtype=numpy.float64)))
print("Média = {}".format(numpy.median(np_city)))
print("Desvio Padrão = {}".format(numpy.std(np_city,dtype=numpy.float64)))

