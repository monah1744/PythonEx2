class Element:
    temp_ci = "C"  # C, F = C*9/5 +32, K = C + 273.15

    def agg_state(self, temp, t_ci="C"):
        if t_ci == "F":
            temp = temp/9*5 - 32
        if t_ci == "K":
            temp = temp - 273.15
        my_state = "liquid"
        if temp < self.temp_min:
            my_state = "solid"
        if temp >= self.temp_max:
            my_state = "steam"
        return my_state
    # solid
    # liquid
    # steam


class Iron(Element):
    def __init__(self):
        super().__init__()
        self.temp_min = 1538
        self.temp_max = 2862


my_element = Iron()

print(my_element.agg_state(1811.16, "K"))
