# 파일을 엽니다.
with open("basic.txt", "r") as file:
    # 파일에 텍스트를 씁니다.
    contents = file.read()

print(contents)