import random 

def maxRevenue(r: list[int], n: int) -> list[int]:
  # Initialize with size n
  dp = [0] * n

  # Base cases
  dp[0] = r[0]
  dp[1] = max(r[0], r[1])
  dp[2] = max(dp[1], r[2])

  # Fill DP table
  for i in range(3, n):
    dp[i] = max(dp[i-1], r[i] + dp[i-3])
  
  # Reconstruct solution
  stores = []
  i = n - 1
  while i >= 0:
    if i == 0:
      stores.append(0)
      break
    elif i == 1:
      if dp[1] == r[i]:
        stores.append(1)
      else:
        stores.append(0)
      break
    elif i == 2:
      if dp[2] == r[2]:
        stores.append(2)
      elif dp[1] == r[1]:
        stores.append(1)
      else:
        stores.append(0)
      break
    else:
      if dp[i] == r[i] + dp[i-3]:
        stores.append(i)
        i = i - 3
      else:
        i = i - 1

  return list(reversed(stores))

random_16 = [random.randint(1, 17) for _ in range(16)]
random_19 = [random.randint(1, 20) for _ in range(19)]
random_21 = [random.randint(1, 22) for _ in range(21)]
random_23 = [random.randint(1, 24) for _ in range(23)]
random_25 = [random.randint(1, 26) for _ in range(25)]

print(f"random_16: {random_16}\nstores: {maxRevenue(random_16, len(random_16))}\n")
print(f"random_19: {random_19}\nstores: {maxRevenue(random_19, len(random_19))}\n")
print(f"random_21: {random_21}\nstores: {maxRevenue(random_21, len(random_21))}\n")
print(f"random_23: {random_23}\nstores: {maxRevenue(random_23, len(random_23))}\n")
print(f"random_25: {random_25}\nstores: {maxRevenue(random_25, len(random_25))}\n")