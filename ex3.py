class Song:
  def __init__(self, name, performer, length):
    self.name = name
    self.performer = performer
    self.length = length

  def __str__(self):
    return f"Song: {self.name}, performer: {self.performer}, length(min): {self.length}"

  def status(self):
    return f"{self.performer}/{self.name}:{self.length}"


class Disc:
  def __init__(self, disk_name, songs):
    self.disk_name = disk_name
    self.songs = songs

  def __str__(self):
    return f"The name of the disc: {self.disk_name}, An array of songs: {self.songs}"

  def exist(self, n_song, p_song):
    is_exist = False
    for song in self.songs:
      if song.name == n_song and song.performer == p_song:
        is_exist = True
        break
    return is_exist


def large_disk_name(d1, d2):
  if len(d1.songs) > len(d2.songs):
    return d1.disk_name
  return d2.disk_name


alohi = Song("אלוהי", "Eyal Golan", 3)
mapheha = Song("מהפכה", "Omer Adam", 2)

mizrahit = Disc("mizrahit", [alohi, mapheha])

yellow = Song("yellow", "Coldplay", 4)

english = Disc("english", [yellow])

print(yellow.status())
print(mizrahit.exist("מהפכה", "Omer Adam"))

print(large_disk_name(mizrahit, english))

# מעולה !