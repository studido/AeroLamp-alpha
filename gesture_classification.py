


class GestureClassification():

    #Entry point
    def classify_gesture(self, landmarks):
        base = landmarks[0]
        thumb = [landmarks[1], landmarks[2], landmarks[3], landmarks[4]]
        index = [landmarks[5], landmarks[6], landmarks[7], landmarks[8]]
        middle = [landmarks[9], landmarks[10], landmarks[11], landmarks[12]]
        ring = [landmarks[13], landmarks[14], landmarks[15], landmarks[16]]
        pinky = [landmarks[17], landmarks[18], landmarks[19], landmarks[20]]

        #These statements can then be directed to the motor control functions 
        if self.open_hand(thumb, index, middle, ring, pinky, base) == True:
            print('Open')
        elif self.closed_fist(thumb, index, middle, ring, pinky, base) == True:
            print('Closed')
        elif self.pointing_up(thumb, index, middle, ring, pinky, base) == True:
            print('Pointing Up')
        elif self.bending_up(thumb, index, middle, ring, pinky, base) == True:
            print('Bending Up') 
        elif self.pointing_right(thumb, index, middle, ring, pinky, base) == True:
            print('Pointing Right') 
        elif self.rotate_right(thumb, index, middle, ring, pinky, base) == True:
            print('Rotate Right')
        elif self.pointing_left(thumb, index, middle, ring, pinky, base) == True:
            print('Pointing Left') 
        elif self.rotate_left(thumb, index, middle, ring, pinky, base) == True:
            print('Rotate Left')  
        elif self.deactivate(thumb, index, middle, ring, pinky, base) == True:
            print('Deactivate') 
        else:
            print('None')

    #--Gesture Functions--#

    def closed_fist(self, thumb, index, middle, ring, pinky, base):
        ret = 0
        if self.orientation(base, thumb, pinky, index) == 2:
            ret += self.closed_finger(index, 2)
            ret += self.closed_finger(middle, 2)
            ret += self.closed_finger(ring, 2)
            ret += self.closed_finger(pinky, 2)
            if ret == 0:
                return True
            else:
                return False
        else:
            return False

    def open_hand(self, thumb, index, middle, ring, pinky, base):
        ret = 0
        if self.orientation(base, thumb, pinky, index) == 2:
            ret += self.closed_finger(index, 2)
            ret += self.closed_finger(middle, 2)
            ret += self.closed_finger(ring, 2)
            ret += self.closed_finger(pinky, 2)
            if ret == 4:
                return True
            else:
                return False
        else:
            return False
    
    def pointing_up(self, thumb, index, middle, ring, pinky, base):
        ret_index = 0
        ret = 0
        if self.orientation(base, thumb, pinky, index) == 2:
            ret_index += self.closed_finger(index, 2)
            ret += self.closed_finger(middle, 2)
            ret += self.closed_finger(ring, 2)
            ret += self.closed_finger(pinky, 2)
            if ret == 0 and ret_index == 1:
                return True
            else:
                return False
        else:
            return False

    def bending_up(self, thumb, index, middle, ring, pinky, base):
        ret_index = 0
        ret = 0
        if self.orientation(base, thumb, pinky, index) == 2:
            ret_index += self.closed_finger(index, 2)
            ret_index += self.closed_finger(middle, 2)
            ret += self.closed_finger(ring, 2)
            ret += self.closed_finger(pinky, 2)
            if ret == 0 and ret_index == 2:
                return True
            else:
                return False
        else:
            return False       

    def pointing_right(self, thumb, index, middle, ring, pinky, base):
        ret = 0 
        ret_index = 0
        if self.orientation(base, thumb, pinky, index) == 1:
                ret_index += self.closed_finger(index, 1)
                ret += self.closed_finger(middle, 1)
                ret += self.closed_finger(ring, 1)
                ret += self.closed_finger(pinky, 1)
                if ret == 0 and ret_index == 1:
                    return True
                return False
        return False
    
    def rotate_right(self, thumb, index, middle, ring, pinky, base):
        ret = 0
        ret_out = 0 
        if self.orientation(base, thumb, pinky, index) == 1:
            ret_out += self.closed_finger(index, 1)
            ret_out += self.closed_finger(middle, 1)
            ret += self.closed_finger(ring, 1)
            ret += self.closed_finger(pinky, 1)
            if ret == 0 and ret_out == 2:
                return True
            return False
        return False

    def pointing_left(self, thumb, index, middle, ring, pinky, base):
        ret = 0 
        ret_index = 0
        if self.orientation(base, thumb, pinky, index) == 0:
                ret_index += self.closed_finger(index, 0)
                ret += self.closed_finger(middle, 0)
                ret += self.closed_finger(ring, 0)
                ret += self.closed_finger(pinky, 0)
                if ret == 0 and ret_index == 1:
                    return True
                return False
        return False
    
    def rotate_left(self, thumb, index, middle, ring, pinky, base):
        ret = 0
        ret_out = 0 
        if self.orientation(base, thumb, pinky, index) == 0:
            ret_out += self.closed_finger(index, 0)
            ret_out += self.closed_finger(middle, 0)
            ret += self.closed_finger(ring, 0)
            ret += self.closed_finger(pinky, 0)
            if ret == 0 and ret_out == 2:
                return True
            return False
        return False

    def deactivate(self, thumb, index, middle, ring, pinky, base):
        ret = 0
        if self.orientation(base, thumb, pinky, index) == 2:
            y_dist = abs((float(index[3][1]) - float(thumb[3][1]))/float(index[3][1]))
            x_dist = abs((float(index[3][0]) - float(thumb[3][0]))/float(index[3][0]))
            distance = y_dist + x_dist
            ret += self.closed_finger(middle, 2)
            ret += self.closed_finger(ring, 2)
            ret += self.closed_finger(pinky, 2)
            if ret == 3 and distance < 0.12:
                return True
        else:
            return False

    #def brighten(self, thumb, index, middle, ring, pinky, base):

    #--Support functions--#

    #TIP and DIP below MCP
    def closed_finger(self, finger, orientation):
        if orientation == 2:
            if (finger[3][1] and finger[2][1]) > finger[1][1]:
                return 0
        elif orientation == 1:
            if (finger[3][0] and finger[2][0]) < finger[1][0]:
                return 0
        elif orientation == 0:
            if (finger[3][0] and finger[2][0]) > finger[1][0]:
                return 0
        return 1

    #Detects hand orientation
    def orientation(self, base, thumb, pinky, index):
        if abs(((float(base[1]) - float(pinky[0][1]))/float(base[1]))) < 0.12 and float(base[0]) > float(pinky[0][0]):
            #print('left')
            return 0 
        elif abs(((float(base[1]) - float(index[0][1]))/float(base[1]))) < 0.12 and float(base[0]) < float(index[0][0]):
            #print('right')
            return 1 
        elif thumb[0][1] < base[1]:
            #print('up')
            return 2 
        elif thumb[0][1] > base[1]:
            #print('down')
            return 3
        
    #TIP inside of IP
    def thumb_in(self, thumb):
        if thumb[3] < thumb[2]:
            return True
        return False

