class SolarObject: #class - instance is created
    def __init__(self, distance_au, orbit_days): #initializes attributes
        self.distance_au = distance_au #instance attribute
        self.orbit_days = orbit_days #instance attribute

    def colonization(self): #defining method
        default_population = 6_000_000_000  # 6 billion default population
        return round(default_population / self.distance_au, 2) #rounds to 2 decimal places

    def spin(self): #"placeholder" is needed when there is more than one class, helps with clarity
        pass

    def __str__(self): #declares the string method - will return or PRINT the following string when call
        return f"Distance from the Sun: {self.distance_au} AU, Orbit: {self.orbit_days} days" #returns the representation of the object

class Planet(SolarObject): # Planet class inherits from SolarObject
    def __init__(self, name, distance_au, orbit_days): #initializes attributes from Planet & SolarObject class
        super().__init__(distance_au, orbit_days) #calling from the parent class
        self.name = name #instance attribute

    def spin(self):  #not a placeholder this time - it is defined now - overrides the spin in parent class
        return "slightly elliptical" #when called -it will return this and print it

    def __str__(self): #declares the string method - will return or PRINT the following string when call
        colonization_potential = self.colonization() #calculation
        return (f"Planet: {self.name}, Distance from the Sun: {self.distance_au} AU, "
                f"Orbit: {self.orbit_days} days, Spin: {self.spin()}, "
                f"Colonization Potential: {colonization_potential} people")

class Comet(SolarObject):  #Class 2 Comet class - inherits information from SolarObject
    def __init__(self, name, distance_au, orbit_days): #initializes attributes from Comet & SolarObject class
        super().__init__(distance_au, orbit_days) #calling from the parent class
        self.name = name #instance attribute

    def spin(self): #not a placeholder this time - it is defined now - overrides the spin in parent class
        return "like crazy" #when called -it will return this and print it

    def __str__(self): #declares the string method - will return or PRINT the following string when call
        colonization_potential = self.colonization() #calucltion
        return (f"Comet: {self.name}, Distance from the Sun: {self.distance_au} AU, "
                f"Orbit: {self.orbit_days / 365.25:.2f} years, Spin: {self.spin()}, "
                f"Colonization Potential: {colonization_potential} people")


#Instances or objects of the Planet class
earth = Planet("Earth", 1, 365) #object
mars = Planet("Mars", 1.4, 687) #object

#Instanecs or objects of the Comet class
halley_comet = Comet("Halley", 35, 76.95 * 365.25)  # object - Orbital period in days
hale_bopp_comet = Comet("Hale-Bopp", 354, 2397.29 * 365.25)  # object - Orbital period in days

# Print the attributes and colonization potential of each object
print(earth)
print(mars)
print(halley_comet)
print(hale_bopp_comet)