class User:
    def __init__(self, id, username):
        print('New user')
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


    pass


user1 = User(1, 'bani')
#print(user1.id)
user2 = User('h', 'angela')


user1.follow(user2)

print(user1.following)
print(user2.followers)