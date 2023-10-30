def pearson_correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x2 = sum([x[i] ** 2 for i in range(n)])
    sum_y2 = sum([y[i] ** 2 for i in range(n)])
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x ** 2) *
                   (n * sum_y2 - sum_y ** 2)) ** 0.5
    return numerator / denominator


x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]


correl_coef = pearson_correlation(x, y)

print(f"Коэффициент корреляции Пирсона между x и y: {correl_coef}")
