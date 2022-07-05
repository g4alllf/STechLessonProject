import re
# 选择题目：第九题
# 输入单词
word1 = "horse"
word2 = "ros"

len1 = len(word1)
len2 = len(word2)

dp = [[0] * (len2+1)] * (len1+1)

for i in range(len1+1):
    dp[i][0] = i

for j in range(len2+1):
    dp[0][j] = j

# i指向word1，j指向word2
for i in range(1, len1+1):
    for j in range(1, len2+1):
        # 如果字符匹配，就不需要进行额外操作
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 否则从增删改中找出操作数最少的一个增加一次操作
        else:
            dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1

print(dp[len1][len2])
