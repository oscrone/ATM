

class User:
    def __init__(self):
        self.database = []
        self.userdata = []
        self.initialize_data()

    def initialize_data(self):
        try:
            f = open("accounts/data.txt", "r")
            file_data = f.read().split(";")
            for x in range(len(file_data)):
                file_data[x] = file_data[x].split(",")
            self.database = file_data
        except ValueError:
            print("!there was an error while opening the file!")
        finally:
            f.close()
            print("User database initialized.")

    def authenticate(self, id):
        for x in self.database:
            if int(x[0]) == id:
                print("ID match!")
                self.userdata = x
                print(f"Data authenticated, card holder {self.userdata[1]}.")

    def save_userdata(self):
        try:
            f = open("accounts/data.txt", "w")
            txt = ""
            d = len(self.database)  # should return 3
            for sublist in self.database:
                d -= 1
                i = len(sublist)              # should return 4
                if sublist[0] == self.userdata[0]:            # if ID matches
                    sublist[2] = self.userdata[2]             # write balance value to x
                    print(f"User {self.userdata[1]} balance updated.")
                for item in sublist:
                    txt += item
                    i -= 1
                    if i > 0:
                        txt += ","
                    elif d > 0:
                        txt += ";"
            f.write(txt)
            print("File saved successfully.")
        except ValueError:
            print("there was an error while saving to the file")
        finally:
            f.close()
