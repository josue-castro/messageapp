class MessageDAO:
    def __init__(self):
        # message id, content, sender id, group id, replied = NULL, date
        M1 = [300, 'Que hacen?', 120, 101, '', '3/23/18']
        M2 = [301, 'Trabajando en el proyecto de DB. Y tu?', 117, 101, '', '3/23/18']
        M3 = [302, 'Estudiando para un examen', 120, 101, '', '3/23/18']
        M4 = [303, 'Yo voy a salir, no hare na de la uni hoy', 131, 101, '', '3/23/18']

        M5 = [257, 'Van para la actividad de hoy?', 99, 122, '', '3/11/18']
        M6 = [258, 'No voy a poder ir mano tengo compromiso', 76, 122, '', '3/11/18']
        M7 = [259, 'Mala mia me quede dormido. Como estuvo?', 81, 122, '', '3/12/18']

        self.messages = []
        self.messages.append(M1)
        self.messages.append(M2)
        self.messages.append(M3)
        self.messages.append(M4)
        self.messages.append(M5)
        self.messages.append(M6)
        self.messages.append(M7)

    def getAllMessages(self):
        return self.messages

    def getGroupMessages(self, gid):
        result = []
        for m in self.messages:
            if gid == m[3]:
                result.append(m)
        return result


