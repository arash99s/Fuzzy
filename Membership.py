class Membership_Height:
    def all(this , x):
        return [this.very_short(x) , this.short(x) , this.medium(x) , this.tall(x) , this.very_tall(x)]

    def very_short(this , x):
        mu = 1
        if x <= 3.83:
            mu = 1
        elif x <= 4.16:
            mu = -3 * x + 12.5
        else:
            mu = 0
        return mu 
    def short(this , x):
        mu = 1
        if x <= 3.83:
            mu = 0
        elif x <= 4.16:
            mu = 3 * x - 11.49
        elif x <= 4.91:
            mu = 1
        elif x <= 5.24:
            mu = -3 * x + 15.75
        else :
            mu = 0
        return mu
    def medium(this , x):
        mu = 1
        if x <= 4.91:
            mu = 0
        elif x <= 5.24:
            mu = 3 * x - 14.75
        elif x <= 6:
            mu = 1
        elif x <= 6.33:
            mu = -3 * x + 18.99
        else :
            mu = 0
        return mu
    def tall(this , x):
        mu = 1
        if x <= 6:
            mu = 0
        elif x <= 6.33:
            mu = 3 * x - 18
        elif x <= 7.08:
            mu = 1
        elif x <= 7.41:
            mu = -3 * x + 22.23
        else :
            mu = 0
        return mu
    def very_tall(this , x):
        mu = 1
        if x <= 7.08:
            mu = 0
        elif x <= 7.41:
            mu = 3 * x - 21.24
        else :
            mu = 1
        return mu




class Membership_Weight:
    def all(this , x):
        return [this.very_slim(x) , this.slim(x) , this.medium(x) , this.heavy(x) , this.very_heavy(x)]

    def very_slim(this , x):
        mu = 1
        if x <= 133.33:
            mu = 1
        elif x <= 166.66:
            mu = -0.03 * x + 5
        else:
            mu = 0
        return mu 
    def slim(this , x):
        mu = 1
        if x <= 133.33:
            mu = 0
        elif x <= 166.66:
            mu = 0.03 * x - 4
        elif x <= 191.66:
            mu = 1
        elif x <= 225:
            mu = -0.03 * x + 6.74
        else :
            mu = 0
        return mu
    def medium(this , x):
        mu = 1
        if x <= 191.66:
            mu = 0
        elif x <= 225:
            mu = 0.03 * x - 5.75
        elif x <= 250:
            mu = 1
        elif x <= 283.33:
            mu = -0.03 * x + 8.5
        else :
            mu = 0
        return mu
    def heavy(this , x):
        mu = 1
        if x <= 250:
            mu = 0
        elif x <= 283.33:
            mu = 0.03 * x - 7.5
        elif x <= 308.33:
            mu = 1
        elif x <= 341.66:
            mu = -0.03 * x + 10.24
        else :
            mu = 0
        return mu
    def very_heavy(this , x):
            mu = 1
            if x <= 308.33:
                mu = 0
            elif x <= 341.66:
                mu = 0.03 * x - 9.24
            else :
                mu = 1
            return mu