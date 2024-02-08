import rhinoscriptsyntax as rs
import box_tools as bt
import color_tools as ct

def get_point_cloud():
    rs.Command('Import ')
    point_cloud = rs.GetObject('Select a point cloud object.', rs.filter.pointcloud)
    return point_cloud



def main():
    
    cloud_id = get_point_cloud()
    colors = rs.PointCloudPointColors(cloud_id)
    points = rs.PointCloudPoints(cloud_id)
    
    for i in range(0, len(colors), 20):
        r_value = colors[i][1]
        rs.EnableRedraw(False)
        if r_value > 100:
            color_val = colors[i]
            box = bt.center_cube(points[i], 10)
            ct.assign_material_color(box, color_val)
        
    
    rs.DeleteObject(cloud_id)


main()