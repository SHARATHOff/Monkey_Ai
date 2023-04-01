import pickle


def Read():
    with open("passwords.dat","rb") as fp:
        while True:
            try:
                r = pickle.load(fp)
                for i in r:
                    print(i," : ",r[i])
            except EOFError:
                break