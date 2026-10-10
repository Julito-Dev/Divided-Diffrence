class Interpolated:
    def __init__(self, nodes):
        self.nodes = nodes   # Nodes is an Array its given with the form [(x0,y0), (x1,y1), ... , (xn, yn)]
        self.coeficients = []
        
    def divided_difference(self):
        # First Step: Obtain the x sub i and the y sub i
        
        # obtaining the x's
        xi = self.getXs() #List [x0, x1, x2, .... , xn]


        # obtaining the y's
        yi = self.getYs() # List [y0, y1, y2, .... , yn]

        # Bulding the table (matrix)
        matrix = self.build_0_matrix()
        
        return matrix
        
    
    
    

    def getXs(self):
        Xs = []
        for node in self.nodes:
            for number in node:
                if number//2 == 0:
                    Xs.append(number)
        return Xs 
    
    
    def getYs(self):
        Ys = []
        for node in self.nodes:
            for number in node:
                if number//2 != 0:
                    Ys.append(number)
        return Ys
    
    def build_0_matrix(self):
        """ Creates an n x (n+1) matrix of zeros
        """
        i = len(self.nodes)
        j = len(self.nodes) + 1
        matrix = [[0 for _ in range(j)] for _ in range(i)]
        return matrix
        

nodos = [(5,4),(6,3),(9,1)]

interpolator = Interpolated(nodos)

m = interpolator.divided_difference()

for row in m:
    print(row)