import math

# mnozenie dodawanie dzielenie ułamkow
# zapisanie w najprostszej postaci
# x - self | y - other
# mniejszy rowny

class Fraction:
    def __init__(self, counter, denominator):
        self.counter = int(counter)
        self.denominator = int(denominator)


    def __add__(self, other_fraction):
        counters_norm = (self.counter*other_fraction.denominator, other_fraction.counter*self.denominator)
        counter_sum = counters_norm[0] + counters_norm[1]
        denominator_norm = self.denominator*other_fraction.denominator
        return Fraction(counter_sum, denominator_norm)

#X = Fraction(1,3)
#Y = Fraction(1,6)
#sum = X + Y
#print(sum.counter)
#print(sum.denominator)

fractions = open("fractions.txt", encoding="utf-8")
x_temp = fractions.readline().strip().split("/")
y_temp = fractions.readline().strip().split("/")

X = Fraction(x_temp[0], x_temp[1])
Y = Fraction(y_temp[0], y_temp[1])

sum2 = X + Y
print(sum2.counter, "/",sum2.denominator)
