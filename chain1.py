import numpy as np
import networkx as nx

#make graph
G = nx.Graph()
G.add_nodes_from(["a","b","c","d","e","f"])
G.add_edges_from([
    ("a","b"), ("b","c"), ("a","c"),   
    ("a","f"), ("f","e"), ("a","e"),  
    ("c","e"),                        
    ("c","d"), ("e","d"),         
])

#Random-walk sim
def hitting_time_one_trial(G, start="a", target="d", rng=None):
    if rng is None:
        rng = np.random.default_rng()
    x = start
    steps = 0
    while x != target:
        x = rng.choice(list(G.neighbors(x)))
        steps += 1
    return steps

def simulate_hitting_times(G, start="a", target="d", n_trials=100_000, seed=0):
    rng = np.random.default_rng(seed)
    times = np.empty(n_trials, dtype=int)
    for i in range(n_trials):
        times[i] = hitting_time_one_trial(G, start, target, rng)
    return times
# Run 
times = simulate_hitting_times(G, start="a", target="d", n_trials=100_000, seed=42)
mean = times.mean()
print(f"Estimated E_a[T_d] ≈ {mean:.4f}")