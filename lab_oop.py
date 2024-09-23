class Showtime:
    movieNum = 1

    @staticmethod
    def getMovieCount():
        return Showtime.movieNum

    def __init__(self, title,genre,length,date,time,cost):
        self._title = title
        self._genre = genre
        self._length = length
        self._date = date
        self._time = time
        self._cost = cost

    def getMovieName(self):
        return self._title

    def printShow(self):
        print(f'{Showtime.movieNum}')
        print(f'Title: "{self._title}"')
        print(f'Genre: {self._genre}')
        print(f'Length: {self._length} min')
        print(f'\nDate: {self._date}       Time: {self._time}     Cost: {self._cost}')
        print('______________________________________________________')
        Showtime.movieNum+=1

    def getCost(self):
        return self._cost
    def getDate(self):
        return self._date
    def getTime(self):
        return self._time


class Viewer:
    def __init__(self, name, phone_number):
        self._name = name
        self._phoneNumber = phone_number
    def getName(self):
        return self._name
    def getPhoneNumber(self):
        return self._phoneNumber
    def greatings(self):
        print('Processioning your order. You are second in line')

class ViewerVIP(Viewer):
    def __init__(self, name, phone_number):
        super().__init__(name, phone_number)
    def greatings(self):
        print('Processioning your order. You are first in line. You will have snack packs options')

class Room:
    def __init__(self,room_number,seats_available):
        self.room_number = room_number
        self.seats_available = seats_available

    def isAvailable(self,seat_number):
        if seat_number in self.seats_available:
            self.seats_available.remove(seat_number)
            return True
        return False

class Snack:
    def __init__(self,snack,drink):
        self.snack = snack
        self.drink = drink

class Ticket:
    def __init__(self, viewer_name, session_info,seat_number, room_number):
        self.viewer_name = viewer_name
        self.session_info = session_info
        self.seat_number = seat_number
        self.room_number = room_number

    def printTicket(self):
        print('______________________________________________________')
        print(f'"{self.session_info.getMovieName()}"')
        print(f'{self.session_info.getCost()}$')
        print(f'{self.session_info.getDate()} at {self.session_info.getTime()}')
        print(f'Room: {self.room_number}    Seat: {self.seat_number}')
        print(f'Bought under name : {self.viewer_name.getName()}    Phone number:  {self.viewer_name.getPhoneNumber()}')
        print('______________________________________________________')

class VIPTicket(Ticket,Snack):
    def __init__(self, viewer_name, session_info,seat_number,room_number,snack,drink):
        Ticket.__init__(self, viewer_name, session_info,seat_number,room_number)
        Snack.__init__(self, snack,drink)
    def printTicket(self):
        print('______________________________________________________')
        print(f'"{self.session_info.getMovieName()}"')
        print(f'{self.session_info.getCost()}$')
        print(f'{self.session_info.getDate()} at {self.session_info.getTime()}')
        print(f'Room: {self.room_number}    Seat: {self.seat_number}')
        print(f'Bought under name : {self.viewer_name.getName()}    Phone number:  {self.viewer_name.getPhoneNumber()}')
        print(f'Added VIP snacks : {self.snack}, {self.drink}')
        print('______________________________________________________')


showtime=[Showtime('Avatar','adventure',150,'03.03.2024','20:00',150),
          Showtime('Roman Holiday','romance',84,'26.08.25','12:15',200)]
rooms=[Room(1,[1,3,4,5,6]),
       Room(2,[1,2])]
tickets=[]

for show in showtime:
    show.printShow()
chosen=0
while chosen!=3:
    print('Choose an option')
    print('1. Buy a ticket')
    print('2. Purchased tickets information')
    print('3. Exit')
    chosen = int(input())
    if chosen == 1:
        print('Chose a movie')
        moviechoice=int(input())-1
        if moviechoice+1 > Showtime.getMovieCount() or moviechoice<0:
            print('Chosen movie is not available')
            continue

        print('Choose a room number')
        roomchoice=int(input())
        if roomchoice> len(rooms) or roomchoice<0:
            print('Chosen room is not available')
            continue

        print('Choose a seat number')
        seatchoice=int(input())
        if not rooms[roomchoice-1].isAvailable(seatchoice):
            print('Chosen seat is not available')
            continue

        print('Enter your name')
        nameinput=input()
        print('Enter your phone number')
        phoneinput=input()
        print('Do you have a VIP subscription? Y/N')
        vipinput=input()
        if vipinput.capitalize()=='Y':
            viewer_new=ViewerVIP(nameinput,phoneinput)
            viewer_new.greatings()
            print('Choose a snack')
            snackinput=input()
            print('Chose a drink')
            drinkinput=input()
            tickets.append(VIPTicket(viewer_new, showtime[moviechoice], seatchoice,roomchoice,snackinput,drinkinput))
        elif vipinput.capitalize()=='N':
            viewer_new=Viewer(nameinput,phoneinput)
            viewer_new.greatings()
            tickets.append(Ticket(viewer_new, showtime[moviechoice], seatchoice,roomchoice))
        else:
            print('Invalid letter')
    if chosen == 2:
        if not tickets:
            print("No tickets purchased yet.")
        for ticket in tickets:
            ticket.printTicket()
    if chosen==3:
        break


