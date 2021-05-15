class Polygen:
    x_coords = []
    y_coords = []
    def add_point(this,x,y):
        this.x_coords.append(x)
        this.y_coords.append(y)

    def find_nearest_points(this, x):
        pairs = {}
        for i in range(len(this.x_coords)):
            pairs[this.x_coords[i]] = this.y_coords[i]
        sorted_pairs = sorted(pairs.items())
        #print('Health coordinates: ' , sorted_pairs)

        for i in range(len(sorted_pairs)-1):
            pair1 = sorted_pairs[i]
            pair2 = sorted_pairs[i+1]
            if x >= pair1[0] and x <= pair2[0]:
                return pair1 , pair2

        print("can not find current pointer")
        return -1 , -1 # error
    
    
    def find_y(this,x):
        point1 , point2 = this.find_nearest_points(x)

        m = (point2[1]-point1[1]) / (point2[0]-point1[0])  # m = (y2-y1) / (x2-x1)
        b = point1[1] - m * point1[0] # b = y - mx

        return m * x + b  # y = mx + b

