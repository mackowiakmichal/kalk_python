def oblicz():
print("Kalkulator")
try:
 a = float(input("Podaj liczbe"))
op = input("Wybierz +, -, * lub /")
b = float(input("Podaj  liczbe:))
if op == '+': print(f"Wynik: {a + b}")
elif op == '-': print(f"Wynik: {a - b}")
elif op == '*': print(f"Wynik: {a * b}")
elif op == '/': 
print(f"Wynik: {a / b}") if b != 0 else print("nie da sie dzielic przez 0!")
else: print("Nieznana operacja.")
except ValueError:
print("wprowadz liczby.")
if __name__ == "__main__":
oblicz()
