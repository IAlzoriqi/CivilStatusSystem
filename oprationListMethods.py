IdentificationCardList = []

FamilyCardList = []
MilitaryCardList = []
PrivateCardList = []
DeathCertificateList = []
BirthCertificateList = []


class OprationMethodsIdentificationCard:

    #IdentificationCardList = []

    @staticmethod
    def reviewAllCard():
        print("Index", "Data User")
        for i in range(len(IdentificationCardList)):
            print(i, "    {0}".format(IdentificationCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        IdentificationCardList.pop(index)

    @staticmethod
    def updateOneCard(self, index):
        IdentificationCardList[index] = {
            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "datebirth": self.datebirth,
            "gender": self.gender,
            "placebirth": self.placebirth,
            "bloodtype": self.bloodtype,
            "release": self.releasedate,
            "expiry": self.expirydate,

        }
        print("Done Update Data")

    @staticmethod
    def saveNewCard(self):
        IdentificationCardList.append(
            {
                "ID":    self.ID,
                "firstname":    self.firstname,
                "fathername":    self.fathername,
                "grandfathername":    self.grandfathername,
                "familyname": self.familyname,
                "datebirth": self.datebirth,
                "gender": self.gender,
                "placebirth": self.placebirth,
                "bloodtype": self.bloodtype,
                "release": self.releasedate,
                "expiry": self.expirydate,

            }
        )
        print("Done Save")


class OprationMethodsFamilyCard:
    @staticmethod
    def saveNewCard(self):
        FamilyCardList.append(
            {
                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "wifename": self.wifename,
                "city": self.city,
                "directorate": self.directorate,
                "street": self.street,
                "releasedate": self.releasedate,

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        print("Index", "Data User")
        for i in range(len(FamilyCardList)):
            print(i, "    {0}".format(FamilyCardList[i]))

    @staticmethod
    def deleteOneCard(index):
        FamilyCardList.pop(index)

    @staticmethod
    def updateOneCard(self, index):
        FamilyCardList[index] = {
            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "wifename": self.wifename,
            "city": self.city,
            "directorate": self.directorate,
            "street": self.street,
            "releasedate": self.releasedate,

        }
        print("Done Update Data")


class OprationMethodsDeathCertificate:
    @staticmethod
    def saveNewCard(self):
        DeathCertificateList.append(
            {



                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "mothername": self.mothername,
                "IC_ID": self.IC_ID,
                "datedeath": self.datedeath,
                "placedath": self.placedath,
                "releasedate": self.releasedate,

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        print("Index", "Data User")
        for i in range(len(DeathCertificateList)):
            print(i, "    {0}".format(DeathCertificateList[i]))

    @staticmethod
    def deleteOneCard(index):
        DeathCertificateList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(self, index):
        DeathCertificateList[index] = {

            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "mothername": self.mothername,
            "IC_ID": self.IC_ID,
            "datedeath": self.datedeath,
            "placedath": self.placedath,
            "releasedate": self.releasedate,

        }
        print("Done Update Data")


class OprationMethodsBirthCertificate:
    @staticmethod
    def saveNewCard(self):
        BirthCertificateList.append(
            {



                "ID": self.ID,
                "firstname": self.firstname,
                "fathername": self.fathername,
                "grandfathername": self.grandfathername,
                "familyname": self.familyname,
                "mothername": self.mothername,
                "gender": self.IC_ID,
                "motherID": self.datedeath,
                "fatherID": self.placedath,
                "releasedate": self.releasedate,

            }
        )
        print("Done Save")

    @staticmethod
    def reviewAllCard():
        print("Index", "Data User")
        for i in range(len(BirthCertificateList)):
            print(i, "    {0}".format(BirthCertificateList[i]))

    @staticmethod
    def deleteOneCard(index):
        BirthCertificateList.pop(index)
        print("Done Delete Card")

    @staticmethod
    def updateOneCard(self, index):
        BirthCertificateList[index] = {


            "ID": self.ID,
            "firstname": self.firstname,
            "fathername": self.fathername,
            "grandfathername": self.grandfathername,
            "familyname": self.familyname,
            "mothername": self.mothername,
            "gender": self.IC_ID,
            "motherID": self.datedeath,
            "fatherID": self.placedath,
            "releasedate": self.releasedate,

        }
        print("Done Update Data")
