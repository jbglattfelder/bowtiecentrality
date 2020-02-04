### Initialize
v <- c(1,1,1,1,1,1) # Unit vector
I <- diag(1,6) # Identity matrix

W <- matrix(0, nrow=6, ncol=6) # Initialize adjacency matrix
W[1,2] <- 0.1
W[2,3] <- 0.5
W[2,4] <- 0.5
W[2,5] <- 0.2
W[3,2] <- 0.3
W[3,5] <- 0.2
W[4,2] <- 0.3
W[4,5] <- 0.6
W[5,2] <- 0.3
W[5,3] <- 0.5
W[5,4] <- 0.5
W[5,6] <- 1


### Access centrality
Winv <- solve(I - W) # Inverse of (I-W) is solve(I-W);
W_tilde <- Winv %*% W # matrix multiplication is %*%
c_acc <- W_tilde %*% v


### Corrected centrality
D <- diag(1 / (diag(solve(I-W)))) # Correction matrix
W_hat <- D %*% W_tilde
c_hat <- W_hat %*% v


### Bow-tie centrality
W_star <- W_hat + D
W_bar <- W %*% W_star
c_bt <- W_bar %*% v

