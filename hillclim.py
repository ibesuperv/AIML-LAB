





def hill_climbing(f, x_start, step_size, max_iter):
    x_cur = x_start
    f_cur = f(x_start)
    print(f"Initial x = {x_cur}, f(x) = {f_cur}")
    for i in range(max_iter):
        nei = [x_cur - step_size, x_cur + step_size]
        best_nei = x_cur
        best_val = f_cur
        for x in nei:
            fx = f(x)
            if fx > best_val:
                best_nei = x
                best_val = fx
        if best_val == f_cur:
            print("\n No further improvement. Terminating..")
            break
        x_cur = best_nei
        f_cur = best_val
        print(f"iteration {i + 1}: x = {x_cur}, f(x) = {f_cur}")
    
    print("\n Final Best solution: ")
    print(f"x = {x_cur}, f(x) = {f_cur}")
        


print("Hill climbing")

func_str = input("Enter Objective: ")
f = lambda x: eval(func_str)

x_start = float(input("Enter initial value of X: "))
step_size = float(input("Enter step size: "))
max_iter = int(input("Enter maximum number of iterations: "))

hill_climbing(f, x_start, step_size, max_iter)