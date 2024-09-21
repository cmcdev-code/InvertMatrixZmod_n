### Inverting Matrices in Rings

This function inverts matrices that are invertible over the ring $ \mathbb{Z}_n $. The method attaches an identity matrix to the input matrix and uses row reduction to transform the augmented matrix into the reduced row echelon form (RREF). By tracking row operations, the right-hand side of the augmented matrix becomes the inverse.

```python
def inv_matrix(matrix, mod):
    dim = len(matrix)
    ...
```

#### Conditions for Invertibility

A matrix $ M \in (\mathbb{Z}_n)^{m \times m} $ is invertible if and only if $ \gcd(\det(M), n) = 1 $, meaning the determinant of the matrix $ M $ is coprime with $ n $. This ensures the existence of a modular inverse for the determinant under mod $ n $.

#### Example of Non-Invertibility in $ \mathbb{Z}_{26}^{2 \times 2} $

Consider the matrix $ \begin{pmatrix} 5 & 7 \\ 4 & 6 \end{pmatrix} \in \mathbb{Z}_{26}^{2 \times 2} $. This matrix is **not invertible**, and the row reduction process illustrates why:

$$
\begin{pmatrix} 5 & 7 \\ 4 & 6 \end{pmatrix} \sim \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}
$$

The determinant of this matrix is 2, and $ \gcd(2, 26) = 13 $. Since 13 is not coprime with 26, no inverse exists for the matrix. In other words, for any $ a \in \mathbb{Z}_{26} $, we have $ 2 \cdot a \neq 1 $. Elementary row operations preserve the kernel of the matrix, and since the reduced form $ \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix} $ has a non-trivial kernel, the matrix is not invertible.

#### Practical Observations

Matrices in $ \mathbb{Z}_n^{m \times m} $ can exhibit undesirable properties when $ n \notin \mathbb{P} $ (i.e., when $ n $ is not prime). In these cases, the behavior of matrices becomes more complicated due to divisors of $ n $, leading to situations where many matrices are not invertible. Despite this, the function handles these cases correctly and efficiently computes the inverse when it exists.

