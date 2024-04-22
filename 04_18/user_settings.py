import rhinoscriptsyntax as rs



def user_settings():
    side_number = rs.RealBox("Provide a side number", 3, 'side_number', minimum=3, maximum= 10)
    file_name = rs.StringBox('provide a file name', 'test', 'file_name')
    
    return side_number, file_name


def main():
    s_n, f_n, = user_settings()
    
    print(s_n, f_n)


main()