class countries:
    def __init__(self,name,size,continent,population,gdp,largestcity,capital):
        self.name=name
        self.size=size
        self.continent=continent
        self.population=population
        self.gdp=gdp
        self.largestcity=largestcity
        self.capital=capital
    def chota_abandoned_airstrip(self):
        print(f"The country is called {self.name}.")
        print(f"The country's size is {self.size} square kilometers.")
        print(f"The continent it is located in is {self.continent}.")
        print(f"The population of the country is {self.population}.")
        print(f"The GDP of the country is {self.gdp}.")
        print(f"The largest city of the country is {self.largestcity}.")
        print(f"The capital city of the country is {self.capital}.")
f1=countries("Switzerland","41,285","Europe","8.888 Million","$884.9 Billion","Zurich","Bern")
f1.chota_abandoned_airstrip()