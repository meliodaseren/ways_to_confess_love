#!/usr/bin/env python3

import sympy as syp
import matplotlib.pyplot as plt

syp.var('x y')
graph = syp.plot_implicit((x**2+y**2-1)**3 - x**2*y**3, show=False)

backend = graph.backend(graph)
backend.backend(graph).process_series()
backend.backend(graph).fig.savefig('./002/002_heart.png')
backend.backend(graph).show()
