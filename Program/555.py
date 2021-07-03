



def list_sub(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])  # 限制偏差角
    return c


list_bias_before = [90, 90, 90, 89, 90, 90, 99, 99, 99, 99, 99, 99, 109, 108, 108, 109, 109, 108]
list_bias_after = [85, 96, 80, 85, 85, 95, 110, 105, 115, 99, 110, 99, 105, 90, 95, 109, 105, 108]

if __name__ == '__main__':
    print(list_sub(list_bias_after , list_bias_before))
