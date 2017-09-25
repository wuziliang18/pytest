num = 10
weights = [0.0 for _ in  range(num) ]
print(weights)
layers = [1, 2, 3, 4, 5]
layers2 = [11, 12, 13,14, 15]
layer_count = len(layers)
connections = [upstream_node + downstream_node
                           for upstream_node in layers
                           for downstream_node in layers2]
           
            
print(connections)

connections = [upstream_node + downstream_node
                           for upstream_node in layers
                           for downstream_node in layers2[:-1]]
print(connections)
connections = [downstream_node  
                           for downstream_node in layers2[:-1]]
           
            
print(connections)