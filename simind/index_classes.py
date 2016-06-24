import numpy as np

class incidence_based_similarity():

    def __init__(self,a,b,ab=None,assume_unique=True):
        self.S_A = len(a)
        self.S_B = len(b)
        if ab is None:
            self.S_AB = float(len(np.intersect1d(a,b,assume_unique=assume_unique)))
        else:
            self.S_AB = float(len(ab))

    def jaccard(self):
        return self.S_AB / (self.S_A + self.S_B - self.S_AB)

    def sorensen(self):
        return 2. * self.S_AB / (self.S_A + self.S_B)

    def ochiai(self):
        return self.S_AB / np.sqrt( self.S_A * self.S_B )

    def lennon(self):
        return self.S_AB / ( self.S_AB + min(self.S_A-self.S_AB, self.S_B-self.S_AB) )

    def kulczynski_cody(self):
        return 0.5 * ( self.S_AB / self.S_A + self.S_AB / self.S_B )

    def kulczynski(self):
        return self.S_AB / (self.S_A + self.S_B - 2*self.S_AB)

    def anderberg(self):
        return self.S_AB / (2*self.S_A + 2*self.S_B - 3*self.S_AB)

class abundance_based_similarity(incidence_based_similarity):

    def __init__(self,a,b,wa,wb,assume_unique=True):

        # get shared species
        self.AB = np.intersect1d(a,b,assume_unique=assume_unique)

        # initialize parent class
        incidence_based_similarity.__init__(self,a,b,self.AB)
        
        #only if there are species in the intersection
        if self.S_AB > 0:

            # norm weights
            wa_sum = float(sum(wa.values()))
            wb_sum = float(sum(wb.values()))

            #self.wa = { a: v/wa_sum if wa_sum>0 else 0 for a,v in wa.items() }
            #self.wb = { b: v/wb_sum if wb_sum>0 else 0 for b,v in wb.items() }

            self.wa = { a: v/wa_sum for a,v in wa.items() }
            self.wb = { b: v/wb_sum for b,v in wb.items() }

            # loop through shared species and add probabilities
            self.S_A = 0.
            self.S_B = 0.
            for ab in self.AB:
                self.S_A += self.wa[ab]
                self.S_B += self.wb[ab]

            # now, self.S_A corresponds to U
            # now, self.S_B corresponds to V

            # compute new shared base quantity
            self.S_AB = self.S_A * self.S_B

            # now, self.S_AB corresponds to U*V

        # if there's no shared species, self.S_AB will be zero and all measures
        # will be naturally 0
