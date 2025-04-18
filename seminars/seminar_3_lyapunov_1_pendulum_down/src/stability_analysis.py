import numpy as np

# Function to classify equilibrium based on system matrix A
def classify_equilibrium(A):
    """Classifies the equilibrium type based on the eigenvalues of matrix A."""
    eigenvalues = np.linalg.eigvals(A)
    trace = np.trace(A)
    determinant = np.linalg.det(A)
    discriminant = trace**2 - 4 * determinant

    # Based on determinant, trace, and discriminant analysis
    if abs(determinant) < 1e-9:  # Degenerate cases (Delta = 0)
        if trace < -1e-9:
            return 7  # Saddle-Node
        else:
            return 8  # Degenerate Case
    elif determinant > 0:  # Nodes or Foci (Delta > 0)
        if trace < -1e-9:  # Stable region (tau < 0)
            if discriminant < -1e-9:
                return 1  # Stable Focus
            elif discriminant > 1e-9:
                return 2  # Stable Node
            else:
                return 3  # Critical Damping
        elif trace > 1e-9:  # Unstable region (tau > 0)
             # Assuming original intent lumps unstable focus/node based on tau > 0, Delta > 0
             return 5 # Unstable Focus / Node
        else:  # trace == 0 (tau = 0)
            return 4  # Center
    else:  # determinant < 0 (Delta < 0)
        return 6  # Saddle Point

# Function to get eigenvalues and eigenvectors
def get_eigenvalues(A):
    """Computes eigenvalues and eigenvectors for matrix A."""
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors 