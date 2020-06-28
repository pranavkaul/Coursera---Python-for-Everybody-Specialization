score_inp = float(input("Enter Score: "))

if score_inp < 0.0 or score_inp >= 1.0:
    print('Error Input')

elif score_inp >= 0.9:
    print('A')

elif score_inp >= 0.8:
    print('B')

elif score_inp >= 0.7:
    print('C')

elif score_inp >= 0.6:
    print('D')

elif score_inp < 0.6:
    print('F')

else:
    print('Error Input')