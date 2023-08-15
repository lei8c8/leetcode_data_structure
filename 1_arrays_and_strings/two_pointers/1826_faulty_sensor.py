class Solution:
    def badSensor(self, sensor1, sensor2):
        n = len(sensor1)
        i = 0 
        while i < n and sensor1[i] == sensor2[i]:
            i += 1
        p1 = p2 = i
        while p1 < n - 1 and sensor1[p1] == sensor2[p1 + 1]:
            p1 += 1
        while p2 < n - 1 and sensor2[p2] == sensor1[p2 + 1]:
            p2 += 1
        if p1 == p2:
            return -1
        return 1 if p1 == n - 1 else 2