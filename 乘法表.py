
#! for循环
# 方法一
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = %d' % (i,j,i*j),end =' ')
        if i == j:
            print('')
            break

# 方法二
for i in range(1,10):
    for j in range(1,i+1):
        print('%d X %d = %d' % (j,i,i*j),end='   ')
    print('   ')

#! while循环
# 方法三
i = 1
while i <= 9:
    j = 1
    while j <= 1:
        print('%d X %d = %d' % (j,i,i*j),end= ('  '))
        j += 1
    print(' ')
    i += 1