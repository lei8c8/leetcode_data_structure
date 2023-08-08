class Solution:
    def flipAndInvertImage(self, image):
        m, n = len(image), len(image[0])

        def flip():
            for i in range(m):
                left, right = 0, len(image[i]) - 1
                while left < right:
                    image[i][left], image[i][right] = image[i][right], image[i][left]
                    left += 1
                    right -= 1

        def invert():
            for i in range(m):
                for j in range(n):
                    image[i][j] ^= 1 

        flip()
        invert()
        return image
