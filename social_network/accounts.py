from datetime import datetime

class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        self.following = []
        self.posts = []
        

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for user in self.following:
            timeline.extend(user.posts)
            
        return sorted(timeline, key=lambda p:p.timestamp, reverse=False)
    # reverse is false as we sort in descending order of time
            

    def follow(self, other):
        self.following.append(other)
