# Алгоритм Евклида нахождения НОД (наибольшего общего делителя)
# Даны два целых неотрицательных числа a и b. Требуется найти их 
# наибольший общий делитель, т.е. наибольшее число, которое является делителем одновременно и a, и b.

def gcd (a, b):
	if b == 0:
		return a
	return gcd(b, a % b)


# Функция Эйлера
# Функция Эйлера phi (n) — это количество чисел от 1 до n, взаимно простых с n. 
# Иными словами, это количество таких чисел в отрезке [1; n], наибольший общий делитель которых с n равен единице.

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


# Important:
# Нахождение наидлиннейшей возрастающей подпоследовательности: https://e-maxx.ru/algo/longest_increasing_subseq_log
# Динамика по профилю: https://e-maxx.ru/algo/profile_dynamics
# Алгоритм Манакера: https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-4/
# O(n)space: https://www.geeksforgeeks.org/longest-palindrome-subsequence-space/