import rhinoscriptsyntax as rs
import random 

def grid(start_point, x_num, y_num, space):
    point_list = []
    points_perp = []
    sx, sy, sz = start_point
    for i in range(sx, x_num*space + sx, space):
        for j in range(sy, y_num*space + sy, space):
            x = i
            y = j
            z = random.uniform(0.0,3.0)
            point = (x, y, z)
            point_perp = (y, x, z)
            points_perp.append(point_perp)
            point_list.append(point)
    return point_list, points_perp

def chunk_list(list_name, size):
    chunks = [list_name[i:i+size] for i in range(0, len(list_name), size)]
    return chunks
    


def main():
    rs.EnableRedraw(False)
    size = 10
    points_vert, points_hor= grid((0,0,0), size, size, 1)
    #rs.AddPoints(points_vert)
    chunks_vert = chunk_list(points_vert, size)
    chunks_hor = chunk_list(points_hor, size)
    for i in range(len(chunks_vert)):
        line = rs.AddPolyline(chunks_vert[i])
        rs.AddPolyline(chunks_hor[i])
        lines.append(line)
    rs.AddLoftSrf(lines)





main()