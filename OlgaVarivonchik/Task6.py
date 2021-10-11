# Task 6.6 Implement a class Money to represent value and currency. You need to implement methods to use all
# basic arithmetics expressions
# (+comparison,
# +division,
# +multiplication,
# +addition
# +and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information about exchange
# rates to your default currency:

class Money:

    def __init__(self, val, cur='USD'):
        self.exchange_rate = {
            "EUR": 0.5,
            "BYN": 2.5,
            "JPY": 150,
            "USD": 1}
        self.value = val
        self.cur = cur
        self.def_rate = self.value / self.exchange_rate[cur]

    def __repr__(self):
        return str(f"{self.value} {self.cur}")

    def calc_rate(self, from_cur, to_cur):
        rate = self.exchange_rate[to_cur] / self.exchange_rate[from_cur]
        return rate

    def __mul__(self, other):
        if isinstance(other, Money):
            m = other.value * self.calc_rate(other.cur, self.cur)
            return Money(self.value * m, self.cur)
        return Money(self.value * other, self.cur)

    def __rmul__(self, other):
        if isinstance(other, Money):
            m = other.value * self.calc_rate(other.cur, self.cur)
            return Money(self.value * m, self.cur)
        return Money(self.value * other, self.cur)

    def __add__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return Money(self.value + m, self.cur)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            m = other.value * self.calc_rate(other.cur, self.cur)
            return Money(self.value + m, self.cur)

    def __sub__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return Money(self.value - m, self.cur)

    def __rsub__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return Money(self.value - m, self.cur)

    def __eq__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return self.value == m

    def __lt__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return self.value < m

    def __gt__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return self.value > m

    def __le__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return self.value <= m

    def __ge__(self, other):
        m = other.value * self.calc_rate(other.cur, self.cur)
        return self.value >= m

    def __truediv__(self, other):
        if isinstance(other, Money):
            m = other.value * self.calc_rate(other.cur, self.cur)
            return Money(self.value / m, self.cur)
        return Money(self.value / other, self.cur)

    def __rtruediv__(self, other):
        if isinstance(other, Money):
            m = other.value * self.calc_rate(other.cur, self.cur)
            return money(self.value / m, self.cur)
        return money(self.value / other, self.cur)


if __name__ == "__main__":
    x = Money(10, 'BYN')
    y = Money(15)
    z = Money(15, 'EUR')
    print(z + 3.11 * x + y * 0.8)
    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)
