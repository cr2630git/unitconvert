from unitconvert.unitconvert import temperature
from unitconvert.unitconvert import distance

def test_unitconvert():
    #Include some known results

    #1. Test temperature functions
    #a. We know that -40 C = -40 F
    assert temperature.fahrenheit_to_celsius(-40)==-40
    assert temperature.celsius_to_fahrenheit(-40)==-40

    #b. We know that 0 C = 32 F
    assert temperature.fahrenheit_to_celsius(32)==0
    assert temperature.celsius_to_fahrenheit(0)==32


    #2. Test distance functions
    #We know that 1 mile is 1.609344 km (to 7 significant figures)
    assert distance.miles_to_kilometers(1)>1.6093
    assert distance.miles_to_kilometers(1)<1.6094

    assert distance.kilometers_to_miles(1.609344)>0.999
    assert distance.kilometers_to_miles(1.609344)<1.0001
