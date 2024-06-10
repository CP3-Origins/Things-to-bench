# SR-benchmark
Benchmarking symbolic regression algorithms using cosmological data (Sofie og Mattias)


## srbench

Go to the python folder for installation instructions.


## Notes on dataset
Koza2 with data range [-1,1,20]

return x**5 - 2*x**3 + x

Keijzer1 with data range [-1,1,20]

return 0.3*x*np.sin(2*np.pi*x)

Keijzer4 with data range [0,10,20]

return x**3*np.exp(-x)*np.cos(x)*np.sin(x)*( np.sin(x)**2*np.cos(x) -1 )

Jin1 in interval [-3,3, N = 100]

return 2.5*x**4 - 1.3*x**3 + 0.5*y**2 - 1.7*y

Jin4 in interval [-3,3, N = 100]

return 1.5*np.exp(x) + 5.0*np.cos(y)

Vladislavleva1 in interval [0.3,4, N = 100]

return np.exp(-(x-1)**2)/( 1.2+(y-2.5)**2 )

Korns2 in interval [-5,5,N = 50]

return 0.23+14.2*(xx1 + xx2)/(3*xx3)

Korns8 in interval [0,10, N = 50]

#return 6.78+11*np.sqrt(7.23*xx1*xx2*xx3) 

Jeg har navngivet og (stortset) valgt intervaller ud fra tabel 7-9 i https://arxiv.org/pdf/2211.10873.pdf
