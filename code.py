import numpy as np

# Initialize
v = np.ones(6)        # Unit vector [1,1,1,1,1,1]
I = np.eye(6)         # 6x6 Identity matrix

# Adjacency matrix
W = np.zeros((6, 6))
W[0,1] = 0.1
W[1,2] = 0.5
W[1,3] = 0.5
W[1,4] = 0.2
W[2,1] = 0.3
W[2,4] = 0.2
W[3,1] = 0.3
W[3,4] = 0.6
W[4,1] = 0.3
W[4,2] = 0.5
W[4,3] = 0.5
W[4,5] = 1.0

# Access centrality
Winv = np.linalg.inv(I - W)  # Inverse of (I - W)
W_tilde = Winv @ W           # Matrix multiplication
c_acc = W_tilde @ v          # Access centrality

# Corrected centrality
D = np.diag(1.0 / np.diag(np.linalg.inv(I - W)))  # Correction matrix
W_hat = D @ W_tilde
c_hat = W_hat @ v

# Bow-tie centrality
W_star = W_hat + D
W_bar = W @ W_star
c_bt = W_bar @ v

# Print results
print("Access centrality (c_acc):\n", c_acc)
print("Corrected centrality (c_hat):\n", c_hat)
print("Bow-tie centrality (c_bt):\n", c_bt)
