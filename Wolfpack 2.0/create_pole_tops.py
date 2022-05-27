from shapely import *
from shapely.geometry import Polygon
from shapely import wkt
import re

file = 'xy_of_foreign_strc_shapes.txt'

def find_centroid():
    coords = []
    x = []
    y = []
    z = []
    xy = []
    txt = ''
    s = ''
    points = 0

    'this will read the txt file and assing to str "txt"'
    with open('D:\\Macros\\Python\\xy_of_foreign_strc_shapes.txt') as f:
        for line in f.readlines():
            txt += line.strip(',')
            points +=1
        f.close()
        print(str(points) + ' points read from file...')

    'remove new lines from string'

    txt = txt.split('\n')

    'returns a list of each point seperated by commas'
    for t in txt:
        s += t + ','
    coords = s.split(',')

    for c in coords:
        if len(c) < 5:
            coords.remove(c)
    coords.pop()   

    'sorts z list into every z coordinate'
    z = coords[2::3]
    x = coords[::3]
    y = coords[1::3]

    count = 0

    for i in x:
        x[count] = float(i)
        count +=1 
    print(str(count) + ' x points converted to floats') 

    count = 0

    for i in y:
        y[count] = float(i)
        count +=1 
    print(str(count) + ' y points converted to floats')

    count = 0

    for i in z:
        z[count] = float(i)
        count +=1 
    print(str(count) + ' z points converted to floats')

    'assign counter'
    count = 0
    polys = 0

    'parse through x values and seperate if > than 50ft'
    for i in x:
        if count > 0 and x[count-1] != '#':
            diff = x[count] - x[count-1]
            if diff > 1 or diff < -1:                
                x.insert(count, '#')                
                count += 1
                polys += 1                
            else:                
                count += 1                
        else:
            count += 1
    print(str(polys) + ' polygons created...')
    count = 0

    'append x values with y values while keeping them seprated'
    for i in x:
        if i != '#':
            xy.append((i, y[count]))        
            count += 1
        else:
            xy.append('#')         
    
    poly = []
    centroid = []
    count = 0
    cen_count = 0
    poly_point = 0
    z_point = []
    highest_z = 0
    high_points = []

    for i in xy:
        if i != '#':
            poly.append(i)
            count += 1
            z_point.append(z[poly_point])
            poly_point += 1
        else: 
            c = str(Polygon(poly))
            p = wkt.loads(c)
            centroid.append(p.centroid.wkt)
            poly.clear()
            cen_count += 1
            highest_z = max(z_point)
            print(highest_z)
            high_points.append(highest_z)
            z_point.clear()
            highest_z = 0

    print(str(cen_count) + ' centroids found...')
    count = 0
            
    for i in centroid:
        centroid[count] = i.strip('POINT ')        
        count +=1 

    count = 0

    with open('xy_of_foreign_strc_centroids.txt', 'w') as f:
        for i in centroid:
            t = i.strip('()')
            l = t.replace(' ', ',')
            f.write(l + ',' + str(high_points[count]) + '\n')
            count +=1 
        f.close()


    print(centroid)


  

find_centroid()