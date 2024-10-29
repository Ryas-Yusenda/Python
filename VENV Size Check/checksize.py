"""Calculate and report disk space usage of installed Python packages."""

import os
from datetime import datetime
import pkg_resources


def calc_container(pkg_path):
    """Calculate total size of a package directory in bytes.

    Args:
        pkg_path (str): Path to the package directory

    Returns:
        int: Total size in bytes
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(pkg_path):
        for file in filenames:  # Changed 'filename' to 'file'
            fp = os.path.join(dirpath, file)
            total_size += os.path.getsize(fp)
    return total_size


dists = [d for d in pkg_resources.working_set]
packages = []

for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = calc_container(path)
        # Convert bytes to MB (1 MB = 1024² bytes)
        size_in_mb = size / (1024**2)
        if size_in_mb > 0.01:  # Only include if larger than 0.01 MB
            packages.append((dist.project_name, size_in_mb))
    except OSError:
        print(f"{dist.project_name} no longer exists")

# Sort packages by size in descending order
packages.sort(key=lambda x: x[1], reverse=True)

# Calculate total size
total_size_mb = sum(size for _, size in packages)

# Create filename with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"pipsize_{timestamp}.txt"

# Write sorted results to file
with open(filename, "w", encoding="utf-8") as f:
    for package, size in packages:
        f.write(f"{package}: {size:.2f} MB\n")
    f.write("\n")  # Add empty line before total
    f.write(f"Total size: {total_size_mb:.2f} MB")

print(f"Results have been saved to {filename}")
