import unittest
class Song:
    def __init__(self, song_name, user):
        self.song_name = song_name
        self.user = user
        self.next = None
        self.prev = None


class RecentlyPlayedStore:
    def __init__(self, initial_capacity):
        self.capacity = initial_capacity
        self.user_songs = {}
        self.head = None
        self.tail = None

    def add_song(self, song_name, user):
        # check if the user already exists in the dictionary
        if user in self.user_songs:
            # update the existing node with the new song and move it to the head
            node = self.user_songs[user]
            node.song_name = song_name
            self._move_to_head(node)
        else:
            # create a new node and add it to the head of the list
            node = Song(song_name, user)
            self.user_songs[user] = node
            self._add_to_head(node)

        # check if the linked list is at capacity and remove the tail if necessary
        if len(self.user_songs) > self.capacity:
            tail_user = self.tail.user
            self.user_songs.pop(tail_user)
            self._remove_tail()

    def get_recently_played(self, user):
        # check if the user exists in the dictionary
        if user in self.user_songs:
            # move the node to the head of the list and return the song name
            node = self.user_songs[user]
            self._move_to_head(node)
            return node.song_name
        else:
            return None

    def _add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def _remove_tail(self):
        if self.tail is None:
            return
        elif self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def _move_to_head(self, node):
        if node == self.head:
            return
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        self.head = node