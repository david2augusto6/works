def convert(ti, ei, ef):
	tf = 0
	if ei == "C":
		match ef:
			case "F":
				return f'{(ti*9/5) + 32:.2f}'
			case "K":
				return f'{ti + 273.15:.2f}'
			case "R":
				return f'{(ti*9/5) + 491.67:.2f}'
			case _:
				return ti

	if ei == "F":
		match ef:
			case "C":
				return f'{(ti-32)*(5/9):.2f}'
			case "K":
				return f'{((ti-32)*(5/9))+273.15:.2f}'
			case "R":
				return f'{ti+459.67:.2f}'
			case _:
				return ti

	if ei == "K":
		match ef:
			case "C":
				return f"{ti-273.15:.2f}"
			case "F":
				return f"{((ti-273.15)*9/5)+32:.2f}"
			case "R":
				return f"{((ti-273.15)*9/5)+491.67:.2f}"
			case _:
				return ti