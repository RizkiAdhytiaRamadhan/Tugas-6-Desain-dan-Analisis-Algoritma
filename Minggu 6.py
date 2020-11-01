#!/usr/bin/env python
# coding: utf-8

# # DYNAMIC PROGRAMMING & ALGORITMA GREEDY
# # I. Algoritma Dynamic: Deret Fibonacci
# ## a. Fibonacci dengan while
# 
# nterms merupakan jumlah deret bilangan fibonacci yang akan dicetak. Dari nilai count hingga nterms, cetak n1 sebagai bilangan pertama, n2 sebagai bilangan ketiga, kemudian nth sebagai jumlah dari bilangan n1+n2. Lalu lakukan update dimana nilai n1 menjadi n2 dan n2 menjadi nth, nilai count ditambahkan setelah update dikerjakan.
# 

# In[2]:


#Fibbonaci dengan while
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

if nterms <= 0: 
    print("Please enter a positive integer") 
elif nterms == 1: 
    print("Fibonacci sequence upto ",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1+n2
        #update nitai
        n1 = n2
        n2 = nth
        count += 1 


# ## b. Fibonacci dengan rekursi
# 
# Fibonacci dengan rekursi, jika nilai n kurang dari sama dengan 1, maka tampilkan n, jika lainnya, kembalikan ke fungsi recur_fibo (n-1) dijumlahkan dengan recur_fibo (n-2). Nilai nterms sebagai masukan dinyatakan terlebih dahulu. Fibonacci dicetak dari i yang nilai pertamanya sebagai 0 hingga nterms.

# In[3]:


#Fibonacci dengan rekursi 
def recur_fibo(n):
    if n <= 1:
        return n
    else: 
        return(recur_fibo(n-1) + recur_fibo(n-2)) 
    
nterms = 20 
# cek apakah niLot nterms vaLid 
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i)) 


# # II.	Algoritma Greedy: Traveling Salesman Problem (TSP)
# ## Algoritma Greedy 
# Penerapan Algoritma Greedy pada TSP (Traveling Salesman/Salesperson Problem) dengan 

# In[13]:


import random
from itertools import permutations
alltours = permutations

def distance_tour(aTour):
    return sum(distance_points(aTour[i - 1], aTour[i])
        for i in range(len(aTour)))

aCity = complex

def distance_points(first, second):
    return abs(first - second) 
def generate_cities (number_of_cities):
    seed=111;width=500;height=300
    random.seed((number_of_cities, seed))
    return frozenset(aCity(random.randint(1, width), random.randint(1,height))
        for c in range(number_of_cities)) 


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

def visualize_tour(tour, style='bo-'):
    if len(tour) > 1000: plt.figure(figsize=(15, 10))
    start = tour[0:1]
    visualize_segment(tour + start, style)
    visualize_segment(start, 'rD')
def visualize_segment (segment, style='bo-'):
        plt.plot([X(c) for c in segment], [Y(c) for c in segment], style, clip_on=False)
        plt.axis('scaled')
        plt.axis('off')
        
def X(city): "X axis"; return city.real

def Y(city): "Y axis"; return city.imag 


# In[18]:


from time import process_time
from collections import Counter
def tsp(algorithm, cities):
    t0 = process_time()
    tour = algorithm(cities)
    t1 = process_time()
    assert Counter(tour) == Counter(cities)
    visualize_tour(tour)
    print("{}: {} cities => tour length {:.0f}(in {:.3f} sec)".format(name(algorithm), len(tour), distance_tour(tour), t1-t0))
    
    
def name(algorithm): return algorithm.__name__.replace('_tsp','')


# In[19]:


def greedy_algorithm(cities, start=None):
    C = start or first(cities)
    tour = [C]
    unvisited = set(cities - {C})
    while unvisited:
        C = nearest_neighbor(C, unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour 

def first(collection): return next(iter(collection))

def nearest_neighbor(A, cities):
    return min(cities, key=lambda C: distance_points(C, A)) 


# In[20]:


tsp(greedy_algorithm, generate_cities(10))


# # III. Algoritma Greedy: Huffman Coding
# ## Algoritma Greedy 
# Penerapan Algoritma Greedy dengan Huffman Coding

# In[21]:


string = 'BCAADDDCCACACAC'

# Creating tree nodes
class NodeTree(object):
    
    def __init__ (self, left=None, right=None):
        self.left = left
        self.right = right 
    
    def children(self):
        return (self.left, self.right)
    
    def nodes(self):
        return (self.left, self.right)
    
    def _str_(self):
        return '%s_%se' % (self.left, self.right) 


# In[28]:


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d 


# In[31]:


# Calculating frequency
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
        
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))
    
    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    
huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char])) 

