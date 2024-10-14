# Things to bench

This repository shows an example of how one can work with the symbolic regression benchmark `cp3-bench`.
Furthermore, one can find our results related to our [paper](https://arxiv.org/abs/2406.15531).

Benchmarking symbolic regression algorithms using cosmological data.

The authors of this paper would like to close by stating that we are open to cooperation in regards to develop the 
framework of cp3-bench further, including adding more algorithms to the suite, but also adding new features and 
improving compatibility to other platforms. 
We suggest contacting the authors per e-mail and code contributions done via pull requests.

## Getting started

To try out this repository clone it with recursion:
```bash
git clone https://github.com/CP3-Origins/Things-to-bench.git --recursive
```

To run the benchmark go to the cp3-bench folder for installation instructions.


## Notes on test datasets
Here you can see specifications of the test dataset found in `datasets`.

F1 with data range x=[-10,1] N=1000

Function: $x^5 - 2*x^3 + x$

F2 with data range x=[-10,10] N=1000

Function: $0.3*x*sin(2*\pi*x)$

F3 with data range x=[0,10] N=1000

Function: $x^3*exp(-x)*cos(x)*sin(x)*(sin(x)^2*cos(x)-1)$

F4 in interval x,y=[-3,3] N=100

Function: $2.5*x^4 - 1.3*x^3 + 0.5*y^2 - 1.7*y$

F5 in interval x,y=[-3,3] N=100

Function: $1.5*e^x + 5.0*cos(y)$

F6 in interval x,y=[0.3,4] N=100

Function: $e^{-(x-1)^2}/( 1.2+(y-2.5)^2)$

F7 in interval x,y,z=[-5,5] N=30

Function: $0.23+14.2*(x + y)/(3*z)$

F8 in interval x,y,z=[-5,5] N=30

Function: $6.78+11*sqrt(7.23*x*y*z)$

These equation are inspired by: https://arxiv.org/pdf/2211.10873.pdf

## Citing this work

If you find `cp3-bench` and this example useful, please cite:

```
@misc{thing2024cp3bench,
      title={cp3-bench: A tool for benchmarking symbolic regression algorithms tested with cosmology}, 
      author={Mattias E. Thing and Sofie M. Koksbang},
      year={2024},
      eprint={2406.15531},
      archivePrefix={arXiv},
      primaryClass={astro-ph.IM},
      url={https://arxiv.org/abs/2406.15531}, 
}
```