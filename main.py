import numpy as np
from scipy.spatial import KDTree
import trimesh
import time

# Load point cloud from PLY file
loading_start_time = time.perf_counter()
point_cloud = trimesh.load('sfm.ply').vertices  # Extract XYZ points
# Build KD-tree
tree = KDTree(point_cloud)
loading_end_time = time.perf_counter()

start_time = time.perf_counter()
# Define start and end points of the ray
point_A = np.array([0, 0, 0])  # Replace with actual coordinates
point_B = np.array([-1, -1, 1])

# Step size along the ray
num_steps = 100
threshold = 0.01  # Collision threshold distance

# Generate points along the ray

ray_points = np.linspace(point_A, point_B, num_steps)
# Check for collisions

for p in ray_points:
    distance, index = tree.query(p, 1)
    if distance < threshold:
        print(f"Collision detected at {p}")
        break
    else:
        print("No collision detected along the ray.")
end_time = time.perf_counter()
print("Loading took", loading_end_time - loading_start_time, "to run")
print("Generating ray and checking for collision took", end_time - start_time, "to run")