n, m = [int(n) for n in input().split()]

n_set = set()
m_set = set()

for _ in range(n):
    n_number = int(input())
    n_set.add(n_number)

for _ in range(m):
    m_number = int(input())
    m_set.add(m_number)

print(*n_set.intersection(m_set), sep='\n')
