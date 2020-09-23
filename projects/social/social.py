import random
import math

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {} # {1: User("1"), 2: User("2"), ...}
        self.friendships = {} #{1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {4}} e.g. user 1 is friend with user 2, 3 and 4

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name) # {1: User("mari")}
        self.friendships[self.last_id] = set() # {1: {}}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
       
       # Add users
       # invoke add_user() until the number is num_users

        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create random friendships
        # Generate all the possible friendships and put them into an array
        # Go to each user and pair up with each other user that has id greater than itself
        # To prevent duplicate friendships by ensuring the first number is smaller than the second 
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        # Shuffle the possible friendship array
        random.shuffle(possible_friendships)

        # Create friendships for the the first X pair of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Needs do divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        # Applied BFT
        # Create empty queue
        queue = []
        # Add path to the starting noce to the queue
        queue.append([user_id])

        while len(queue) > 0:
            # Remove the first path from the queue
            path = queue.pop(0)
            # Get the last item in the path
            new_user_id = path[-1]
            # Check if visited
            if new_user_id not in visited:
                # If not visited, we add path to visited dictionary
                visited[new_user_id] = path
                # Add path to each friend at the end of the queue
                # Loop over adjacency list of all friends
                for friend_id in self.friendships[new_user_id]:
                    if friend_id not in visited:
                        new_path = list(path)
                        new_path.append(friend_id)
                        queue.append(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("Friendships:")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("Connections:")
    print(connections)
