import numpy as np
N=1000
p_i=np.array([1/N for i in range(1,7)])
my_list = (np.random.randint(low = 1, high = 7, size = 1000))
my_array = np.array(my_list)
x_i = np.array([1, 2, 3, 4, 5, 6])


count_1 = np.count_nonzero(my_array == 1)
count_2 = np.count_nonzero(my_array == 2)
count_3 = np.count_nonzero(my_array == 3)
count_4 = np.count_nonzero(my_array == 4)
count_5 = np.count_nonzero(my_array == 5)
count_6 = np.count_nonzero(my_array == 6)

prob_1 = count_1/N
prob_2 = count_2/N
prob_3 = count_3/N
prob_4 = count_4/N
prob_5 = count_5/N
prob_6 = count_6/N

p_i = np.array([prob_1, prob_2, prob_3, prob_4, prob_5, prob_6])
print(p_i)

E_x = p_i@x_i
print(f"mean is {(E_x)}")

E_x_2 = (x_i*x_i)@p_i
print(f"E(X^2) is {(E_x_2)}")

Var_x = E_x_2 - (E_x*E_x)
print(f"Var(X) is {(Var_x)}")

