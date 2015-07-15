__author__ = 'John Kusner'

import datetime

_1_jan_1000 = datetime.datetime(1000, 1, 1)

class CACBarcode:
    """
    Generic barcode class, constructing this will do nothing
    """
    def __init__(self):
        pass
    def read(self, data, count):
        return data[:count], data[count:]

    def readnum(self, data, count, base = 32):
        return int(data[:count], base), data[count:]

    def readdate(self, data):
        days, data = self.readnum(data, 4)
        date = _1_jan_1000 + datetime.timedelta(days=days)
        return date, data

    def _getbranch(self, code):
        """
        Called by constructor, don't call this method
        http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, page 50
        :param code: Branch Code
        :return: Branch Service String
        """
        # Series of ifs for speed since this is a one way conversion
        if code == "A": return "USA"
        if code == "C": return "USCG"
        if code == "D": return "DOD"
        if code == "F": return "USAF"
        if code == "H": return "USPHS"
        if code == "M": return "USMC"
        if code == "N": return "USN"
        if code == "O": return "NOAA"
        if code == "1": return "Foreign Army"
        if code == "2": return "Foreign Navy"
        if code == "3": return "Foreign Marine Corps"
        if code == "4": return "Foreign Air Force"
        if code == "X": return "Other"
        return "N/A"

    def _getpdt(self, code):
        """
        Called by constructor, don't call this method
        http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, page 50
        :param code: Person Designator Type Code
        :return: Person Designator Type String
        """
        # Series of ifs for speed since this is a one way conversion
        if code == "S": return "Social Security Number (SSN)"
        if code == "N": return "9 digits, not valid SSN"
        if code == "P": return "Special code before SSNs"
        if code == "D": return "Temporary Identifier Number (TIN)"
        if code == "F": return "Foreign Identifier Number (FIN)"
        if code == "T": return "Test (858 series)"
        if code == "I": return "Individual Taxpayer Identification Number"
        return "N/A"

    def _getcategory(self, code):
        """
        Called by constructor, don't call this method
        http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, page 51
        :param code: Personnel Category Code
        :return: String of category description
        """
        # Series of ifs for speed since this is a one way conversion
        if code == "A": return "Active Duty member"
        if code == "B": return "Presidential Appointee"
        if code == "C": return "DoD civil service employee"
        if code == "D": return "100% disabled American veteran"
        if code == "E": return "DoD contract employee"
        if code == "F": return "Former member"
        if code == "N" or code == "G": return "National Guard member"
        if code == "H": return "Medal of Honor recipient"
        if code == "I": return "Non-DoD Civil Service Employee"
        if code == "J": return "Academy student"
        if code == "K": return "non-appropriated fund (NAF) DoD employee"
        if code == "L": return "Lighthouse service"
        if code == "M": return "Non-Government agency personnel"
        if code == "N": return "National Guard member"
        if code == "O": return "Non-DoD contract employee"
        if code == "Q": return "Reserve retiree not yet eligible for retired pay"
        if code == "R": return "Retired Uniformed Service member eligible for retired pay"
        if code == "V" or code == "S": return "Reserve"
        if code == "T": return "Foreign military member"
        if code == "U": return "Foreign national employee"
        if code == "V": return "Reserve member"
        if code == "W": return "DoD Beneficiary"
        if code == "Y": return "Retired DoD Civil Service Employees"
        return "N/A"

    def _getpect(self, code):
        """
        http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, pp. 52-53
        :param code: PECT code (numeric 01-42)
        :return: Personnel Entitlement Condition Type
        """
        # Series of ifs for speed since this is a one way conversion
        if code == "01": return "On Active Duty. Segment condition."
        if code == "02": return "Mobilization. Segment condition."
        if code == "03": return "On appellate leave. Segment condition."
        if code == "04": return "Military prisoner. Segment condition."
        if code == "05": return "POW/MIA. Segment condition."
        if code == "06": return "Separated from Selected Reserve. Event condition."
        if code == "07": return "Declared permanently disabled after temporary disability period. Event condition."
        if code == "08": return "On non-CONUS assignment. Segment condition."
        if code == "09": return "Living in Guam or Puerto Rico. Segment condition."
        if code == "10": return "Living in government quarters. Segment condition."
        if code == "11": return "Death determined to be related to an injury, illness, or disease while on Active duty for training or while traveling to or from a place of duty. Event condition."
        if code == "12": return "Discharged due to misconduct involving family member abuse. (Sponsors who are eligible for retirement.) Segment condition."
        if code == "13": return "Granted retired pay. Event condition."
        if code == "14": return "DoD sponsored in U.S. (foreign military). Segment condition."
        if code == "15": return "DoD non-sponsored in U.S. (foreign military). Segment condition."
        if code == "16": return "DoD sponsored overseas. Segment condition."
        if code == "17": return "Deserter. Segment condition."
        if code == "18": return "Discharged due to misconduct involving family member abuse. (Sponsors who are not eligible for retirement.) Segment condition."
        if code == "19": return "Reservist who dies after receiving their 20 year letter. Event condition."
        if code == "20": return "Transitional assistance (TA-30). Segment condition."
        if code == "21": return "Transitional assistance (TA-Res). Segment condition."
        if code == "22": return "Transitional assistance (TA-60). Segment condition."
        if code == "23": return "Transitional assistance (TA-120). Segment condition."
        if code == "24": return "Transitional assistance (SSB program). Segment condition."
        if code == "25": return "Transitional assistance (VSI program). Segment condition."
        if code == "26": return "Transitional assistance (composite). Segment condition."
        if code == "27": return "Senior Executive Service (SES)."
        if code == "28": return "Emergency Essential - overseas only."
        if code == "29": return "Emergency Essential - CONUS."
        #                        v   Not sure if this 2 is meant to be here, see pdf page 53
        if code == "30": return "2Emergency Essential - CONUS in living quarters, living on base, and not drawing a basic allowance for quarters, serving in an emergency essential capacity"
        if code == "31": return "Reserve Component TA-120 Reserve Component Transition Assistance TA 120 (Jan 1, 2002 or later)"
        if code == "32": return "On MSC owned and operated vessels Deployed to foreign countries on Military Sealift Command owned and operated vessels. Segment condition."
        if code == "33": return "Guard/Reserve Alert Notification Period" # this is written twice on the pdf
        if code == "34" or code == "35": return "Reserve Component TA-180 - 180 days TAMPS for reserve return from named contingencies"
        if code == "36" or code == "37": return "TA-180 - 180 days TAMP for involuntary separation"
        if code == "38": return "Living in Government Quarters in Guam or Puerto Rico, Living on base and not drawing an allowance for quarters in Guam or Puerto Rico."
        if code == "39": return "Reserve Component TA-180 - TAMP - Mobilized for Contingency"
        if code == "40": return "TA-180 TAMP - SPD Code Separation"
        if code == "41": return "TA-180 - TAMP - Stop/Loss Separation"
        if code == "42": return "DoD Non-Sponsored Overseas - Foreign Military personnel serving OCONUS not sponsored by DoD"
        return ""



class PDF417Barcode(CACBarcode):
    """
    Reads a PDF417 2D Barcode on the front of CACs
    See http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, pp. 13-14
    """

    def __init__(self, data):
        self.data = data

        # 2D barcode Version "1" and Version "N" have 88 and 89 chars
        # VN's 89'th char is middle initial
        if len(data) != 88 and len(data) != 89:
            raise Exception

        # Read the barcode version
        self.barcode_version, data = self.read(data, 1)

        # Only version 1 and N supported
        if self.barcode_version != "1" and self.barcode_version != "N":
            print("Version", self.barcode_version, "not recognized!")
            raise Exception

        # Read the PDI (Personal Designator Identifier) in base 32
        self.pdi, data = self.readnum(data, 6)

        # Read personal designator type
        self.pdt, data = self.read(data, 1)

        # Get PDT name
        self.pdtname = self._getpdt(self.pdt)

        # Read EDIPI (EDI Person Identifier) in base 32
        self.edipi, data = self.readnum(data, 7)

        # Read first name
        self.firstname, data = self.read(data, 20)
        self.firstname = self.firstname.strip()

        # Read last name
        self.lastname, data = self.read(data, 26)
        self.lastname = self.lastname.strip()

        # Full name
        self.name = self.firstname + " " + self.lastname

        # Read DOB (num of days since 1 Jan 1000)
        self.dob, data = self.readdate(data)

        # Read PCC (Personnel Category Code)
        self.pcc, data = self.read(data, 1)

        # Get PCC
        self.category = self._getcategory(self.pcc)

        # Read Branch Code
        self.bc, data = self.read(data, 1)

        # Get branch
        self.branch = self._getbranch(self.bc)

        # Read Personnel Entitlement Condition Type
        self.pect, data = self.read(data, 2)

        # Get pect description
        self.pectdesc = self._getpect(self.pect)

        # Read Rank
        self.rank, data = self.read(data, 6)
        self.rank = self.rank.strip()

        # Read Pay Plan Code
        self.ppc, data = self.read(data, 2)

        # Read Pay Plan Grade Code
        self.ppgc, data = self.read(data, 2)

        # Card issue date (days since 1 Jan 1000)
        self.issuedate, data = self.readdate(data)

        # Card expiration date
        self.expdate, data = self.readdate(data)

        # Card instance identifier (random)
        self.instanceid, data = self.read(data, 1)

        # Middle initial (VN only)
        self.middleinitial, _ = "", "" if self.barcode_version == "1" else self.read(data, 1)

        # Full name
        if self.middleinitial != "":
            self.fullname = self.firstname + " " + self.middleinitial + " " + self.lastname
        else:
            self.fullname = self.firstname + " " + self.lastname

    def debugprint(self):
        """
        Print out all values for test purposes
        """
        print("Barcode Version:", self.barcode_version)
        print("PDI:", self.pdi)
        print("PDT:", self.pdt, ":", self.pdtname)
        print("EDIPI:", self.edipi)
        print("Name:", self.fullname)
        print("DOB:", self.dob.strftime("%x"))
        print("Category:", self.pcc, ":", self.category)
        print("Branch:", self.branch, "(" + self.bc + ")")
        print("PECT:", self.pect, ":", self.pectdesc)
        print("Rank:", self.rank)
        print("PayPlan: ", self.ppc, ":", self.ppgc, sep="")
        print("Issued:", self.issuedate.strftime("%x"))
        print("Exp:", self.expdate.strftime("%x"))
        print("InstanceID:", self.instanceid)

    def __str__(self):
        return "PDF417Barcode" + str(self.__dict__)


class Code39Barcode(CACBarcode):
    """
    Reads the Code39 Barcode on the back of CACs
    See http://www.cac.mil/docs/DoD-ID-Bar-Code_SDK-Formats_v7-5-0_Sep2012.pdf, pp. 13-14
    """

    def __init__(self, data):
        self.data = data

        if len(data) != 18:
            raise Exception

        # Only version 1 supported, 18 char length
        self.barcode_version, data = self.read(data, 1)
        if self.barcode_version != "1":
            print("Bad version:", self.barcode_version)
            raise Exception

        # Read PDI
        self.pdi, data = self.readnum(data, 6)

        # Read PDT
        self.pdt, data = self.read(data, 1)
        self.pdtname = self._getpdt(self.pdt)

        # Read EDIPI
        self.edipi, data = self.readnum(data, 7)

        # Read Personnel Category
        self.pcc, data = self.read(data, 1)
        self.category = self._getcategory(self.pcc)

        # Read Branch Code
        self.bc, data = self.read(data, 1)
        self.branch = self._getbranch(self.bc)

        # Read Card Instance Identifier
        self.instanceid, data = self.read(data, 1)

    def debugprint(self):
        """
        Print out all values for test purposes
        """
        print("Barcode Version:", self.barcode_version)
        print("PDI:", self.pdi)
        print("PDT:", self.pdt, ":", self.pdtname)
        print("EDIPI:", self.edipi)
        print("Category:", self.pcc, ":", self.category)
        print("Branch:", self.branch, "(" + self.bc + ")")
        print("InstanceID:", self.instanceid)

    def __str__(self):
        return "Code39Barcode" + str(self.__dict__)
