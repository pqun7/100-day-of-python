# class User:
#     pass
# pass = اذا وضعت كلاس او فوكنشن بدون اوامر لن تتنفذ الاوامر الذي تليها وسوف ياتي خطاء والحل للمشكله هو باس
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Ali")
print(user1.id, user1.username)

user2 = User("002", "Ahmed")
print(user2.id, user2.username)

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)