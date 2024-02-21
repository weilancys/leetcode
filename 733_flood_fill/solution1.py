# time complexity: O(n)
# space complexity: O(1)

# fill the pixels using recursion in a DFS mannaer

# image = [
#     [1,1,1],
#     [1,1,0],
#     [1,0,1]
#     ]
# sr = 1
# sc = 1
# color = 2

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        color_original = image[sr][sc]
        self.fill(image, sr, sc, color, color_original)
        return image

    def fill(self, image: list[list[int]], m: int, n: int, color_to_fill: int, color_original: int):
        if m < 0 or m >= len(image):
            return
        if n < 0 or n >= len(image[0]):
            return
        if image[m][n] != color_original:
            return
        if image[m][n] == color_to_fill: # avoid coloring the pixel again
            return
        image[m][n] = color_to_fill
        self.fill(image, m-1, n, color_to_fill, color_original)
        self.fill(image, m, n+1, color_to_fill, color_original)
        self.fill(image, m+1, n, color_to_fill, color_original)
        self.fill(image, m, n-1, color_to_fill, color_original)

if __name__ == "__main__":
    solution1 = Solution()
    image = solution1.floodFill(image, sr, sc, color)
    print("image:", image)