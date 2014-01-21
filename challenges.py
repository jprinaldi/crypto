import factoring, rsa, pkcs_1_v1_5

class Challenge:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def show_status(self, is_solved):
        if is_solved:
            print "Successfully solved: {}".format(self.name)
        else:
            print "Failed to solve: {}".format(self.name)

class FactoringChallenge(Challenge):
    def __init__(self, id, name, N):
        Challenge.__init__(self, id, name)
        self.N = N

    def solve(self):
        N = self.N
        if self.id == 1:
            factors = factoring.factor_1(N)
        elif self.id == 2:
            factors = factoring.factor_2(N)
        elif self.id == 3:
            factors = factoring.factor_3(N)
        else:
            factors = None

        if factors != None:
            p, q = factors
            assert p*q == N
            self.show_status(True)
            print "p = {}".format(p)
            print "q = {}".format(q)
        else:
            self.show_status(False)

class RSAChallenge(Challenge):
    def __init__(self, id, name, N, e, c):
        Challenge.__init__(self, id, name)
        self.N = N
        self.e = e
        self.c = c

    def solve(self):
        if self.id == 4:
            m = rsa.crack(self.N, self.e, self.c, factoring.factor_1)
            msg = pkcs_1_v1_5.decode(m)
            plaintext = msg.decode("hex")
        else:
            plaintext = None

        if plaintext != None:
            self.show_status(True)
            print "Plaintext: \"{}\"".format(plaintext)
        else:
            self.show_status(False)