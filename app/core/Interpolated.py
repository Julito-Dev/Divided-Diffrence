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

        
        # Define the n
        n = len(self.nodes)
        
        
        # Bulding the table (matrix)
        matrix = self.build_0_matrix()
        
        
        #--------- Method------
        
        for i in range(n):
            matrix[i][0] = xi[i]
            matrix[i][1] = yi[i]
            
        # Calculate the divided differences
        
        for j in range(2,n+1):
            for i in range(n-j+1):
                numerator = ( matrix[i+1][j-1] - matrix[i][j-1])
                denomiator = xi[i+j-1] - xi[i]
                
                if denomiator == 0:
                    raise ValueError("The x coordinates must be distinct")

            matrix[i][j] = numerator/denomiator
            
            
        # Coefficients
        
        self.coeficients = [matrix[0][j] for j in range(1, n+1)]
        
        return matrix
        
    
    def getXs(self):
        return [node[0] for node in self.nodes]
    
    def getYs(self):
        return [node[1] for node in self.nodes]
    
    def build_0_matrix(self):
        """ Creates an n x (n+1) matrix of zeros
        """
        n = len(self.nodes)
        return  [[0.0 for _ in range(n+1)] for _ in range(n)]