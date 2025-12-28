def calculate_area(height, width):
    return height * width

height = int(input("輸入高度："))
width = int(input("輸入寬度："))

area = calculate_area(height, width)
print("面積是：", area)