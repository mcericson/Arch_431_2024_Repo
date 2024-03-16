import rhinoscriptsyntax as rs


color_val = rs.ListBox(['red', 'green', 'blue', 'alpha'], "Set color value")

if color_val == 'red':
    col = rs.CreateColor(255,0,0)
sphere = rs.AddSphere((0,0,0), 200)
rs.ObjectColor(sphere, hucol)