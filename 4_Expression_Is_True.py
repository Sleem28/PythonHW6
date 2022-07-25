# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


b_list = [[False ,False, False], [False, False, True], [False, True, True], [True, True, True], [True, True, False], [True, False, False], [False, True, False], [True, False, True]]

result = list(map(lambda b_vals: f'Для значений x = {b_vals[0]}, y = {b_vals[1]} и z = {b_vals[2]} выражение {"верно" if  (not(b_vals[0] or b_vals[1] or b_vals[2]) == (not b_vals[0] and not b_vals[1] and not b_vals[2])) else "ложь"}', b_list))

for item in result: print(item)