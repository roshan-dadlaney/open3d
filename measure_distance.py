import numpy as np
import open3d as o3d

vis = o3d.visualization.VisualizerWithVertexSelection()

def measure_dist():
    pts=vis.get_picked_points()
    if len(pts)>1:
        point_a=getattr(pts[1],'coord')
        point_b=getattr(pts[0],'coord')
        
        dist=np.sqrt((point_a[0]-point_b[0])**2 + (point_a[1]-point_b[1])**2 + (point_a[2]-point_b[2])**2)
        print(f"Point_A: {point_a}")
        print(f"Point_B: {point_b}")
        print(f"Distance: {dist}")

    else:
        print("Select atleast 2 points to calculate Dist")

if __name__ == "__main__":

    print("Load a ply point cloud, print it, and render it")
    file="/path/to/3d_file.ply"

    pcd =  o3d.io.read_point_cloud(file)

    vis.create_window()
    vis.add_geometry(pcd)
    vis.register_selection_changed_callback(measure_dist)
    vis.run()
    vis.destroy_window()
