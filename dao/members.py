class MembersDAO:
    def __init__(self):
        # member gid, pid
        M1 = [101, 120]
        M2 = [101, 117]
        M3 = [101, 131]

        M4 = [122, 99]
        M5 = [122, 76]
        M6 = [122, 81]

        self.members = []
        self.members.append(M1)
        self.members.append(M2)
        self.members.append(M3)
        self.members.append(M4)
        self.members.append(M5)
        self.members.append(M6)

    def getMembers(self, gid):
        result = []
        for member in self.members:
            if gid == member[0]:
                result.append(member)
        return result

    def getMember(self, gid, pid):
        result = []
        for member in self.members:
            if gid == member[0] & pid == member[1]:
                result.append(member)
        return result

    def addMember(self, gid, pid):
        member = [gid, pid]
        self.members.append(member)
