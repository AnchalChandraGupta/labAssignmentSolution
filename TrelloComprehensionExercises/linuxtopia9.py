portfolio = [("25-Jan-2001", 43.50, 25, 'CAT', 92.45),
             ("25-Jan-2001", 42.80, 50, 'DD', 51.19),
             ("25-Jan-2001", 42.10, 75, 'EK', 34.87),
             ("25-Jan-2001", 37.58, 100, 'GM', 37.58)
             ]

portfolio.sort(key=lambda x: x[2]*x[4], reverse=True)

print(*portfolio, sep='\n')

