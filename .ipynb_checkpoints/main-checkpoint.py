import numpy as np
from scipy.spatial import KDTree
import trimesh

# Load point cloud from PLY file
point_cloud = trimesh.load('sfm.ply').vertices  # Extract XYZ points

# Build KD-tree
tree = KDTree(point_cloud)

# Define start and end points of the ray
point_A = np.array([0, 0, 0])  # Replace with actual coordinates
point_B = np.array([1, 1, 1])

# Step size along the ray
num_steps = 100
threshold = 0.01  # Collision threshold distance

# Generate points along the ray
ray_points = np.linspace(point_A, point_B, num_steps)

# Check for collisions
for p in ray_points:
    distance,  = tree.query(p)
    if distance < threshold:
        print(f"Collision detected at {p}")
        break
else:
    print("No collision detected along the ray.")