import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import Membership
import Decision_Polygen


PERSON_HEIGHT = 6.3
PERSON_WEIGHT = 200

#            very_slim / slim / medium / heavy /  very_heavy
# very_short/  @          @       @        @         @   
# short/       @          @       @        @         @
# medium/      @          @       @        @         @
# tall/        @          @       @        @         @
# very_tall/   @          @       @        @         @

activate_rules = [['H','SH','LH','U','U'],
                  ['SH','H','SH','LH','U'],
                  ['LH','H','H','LH','U'],
                  ['U','SH','H','SH','U'],
                  ['U','LH','H','SH','LH']]

fuzzified_decision = {'U': 0 , 'LH': 0 ,'SH': 0 ,'H': 0}


membership_height = Membership.Membership_Height()
membership_weight = Membership.Membership_Weight()
height_mu = membership_height.all(PERSON_HEIGHT)
weight_mu = membership_weight.all(PERSON_WEIGHT)


print('weigth degrees : ' , weight_mu)
print('heigth degrees : ' , height_mu)




activate_rules_mu = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        activate_rules_mu[i,j] = min(height_mu[i],weight_mu[j])
        if activate_rules_mu[i,j] != 0:
            fuzzified_decision[activate_rules[i][j]] = activate_rules_mu[i,j]


print(activate_rules_mu)
print(fuzzified_decision)




polygen = Decision_Polygen.Polygen()
polygen.add_point(0 , 0)  # first point must be zero
polygen.add_point(0.2 , fuzzified_decision['U'])
polygen.add_point(0.4 , fuzzified_decision['LH'])
polygen.add_point(0.6 , fuzzified_decision['SH'])
polygen.add_point(0.8 , fuzzified_decision['H'])
polygen.add_point(1 , 0)  # last point must be zero


x_coords = np.arange(0, 1, 0.01)
y_coords = []

for x in x_coords:
    y_coords.append(polygen.find_y(x))


mfx = np.array(y_coords)

defuzz_centroid = fuzz.defuzz(x_coords, mfx, 'centroid')  
defuzz_bisector = fuzz.defuzz(x_coords, mfx, 'bisector')
defuzz_mom = fuzz.defuzz(x_coords, mfx, 'mom')



# Collect info for vertical lines
labels = ['centroid', 'bisector', 'mean of maximum']
xvals = [defuzz_centroid,
         defuzz_bisector,
         defuzz_mom]
colors = ['r', 'b', 'g']
ymax = [fuzz.interp_membership(x_coords, mfx, i) for i in xvals]

# Display and compare defuzzification results against membership function
plt.figure(figsize=(8, 5))

plt.plot(x_coords, mfx, 'k')
for xv, y, label, color in zip(xvals, ymax, labels, colors):
    plt.vlines(xv, 0, y, label=label, color=color)
plt.ylabel('Fuzzy membership')
plt.ylim(-0.1, 1.1)
plt.legend(loc=2)

plt.show()