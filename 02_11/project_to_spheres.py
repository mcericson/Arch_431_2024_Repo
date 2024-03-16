import rhinoscriptsyntax as rs
from math import sin, cos, radians


def xz_vector(angle_degrees):
    x = cos(radians(angle_degrees))
    y = 0
    z = sin(radians(angle_degrees))
    return(x, y, z)


def spherical_grid(num_spheres, radius):
    spheres = []
    step = int(radius*2)
    stop = num_spheres * step
    for i in range(0, stop, step):
        for j in range(0, stop, step):
            x = i
            y = j
            sphere = rs.AddSphere((x, y, 0), radius)
            spheres.append(sphere)
    return spheres

def conical_grid(num_cones, radius):
    cones = []
    step = int(radius*2)
    stop = num_cones * step
    for i in range(0, stop, step):
        for j in range(0, stop, step):
            x = i
            y = j
            cone = rs.AddCone((x, y, 0), radius/2, radius)
            cones.append(cone)
    return cones


def main():
    spheres = spherical_grid(5, 100)
    rs.ZoomExtents()
    vector = xz_vector(70)
    count = 0

    while count < 200:
        count += 1
        x, y, z = rs.GetCursorPos()[0]
        circle = rs.AddCircle((x,y,0), 50)
        for i in range(len(spheres)):
            try:
                
                rs.ProjectCurveToSurface(circle, spheres[i], vector)

            except:
                pass
    rs.DeleteObjects(spheres)
    rs.ZoomExtents()
main()