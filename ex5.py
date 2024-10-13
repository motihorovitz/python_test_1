class Participant:
  def __init__(self, name, id, price):
    self.name = name
    self.id = id
    self.price = price


class VickeryAuction:
  def __init__(self, product, arr,
               real_price):  # product = תיאור המוצר, arr = מערך של משתתפים, real_price = ערך של מוצר
    self.product = product
    self.arr = arr
    self.real_price = real_price
    self.current = len(arr)

  def winner(self):
    name = ''
    max_price = 0
    sec_price = 0
    for participant in self.arr:
      if participant.price > max_price:
        name = participant.name
        sec_price = max_price
        max_price = participant.price

      if max_price > participant.price > sec_price:
        sec_price = participant.price

    winner = Winner(name, sec_price)
    return winner

  def new_participant(self, participant):
    if self.current < 100 and participant.price >= self.real_price * 1.5:
      self.arr.append(participant)
      self.current += 1
      return True
    return False


class Winner:
  def __init__(self, name, last_price):
    self.name = name
    self.last_price = last_price

  def __str__(self):
    return f"Winner - {self.name}, lastPrice - {self.last_price}"


participant_1 = Participant("moti", 23, 1000)
participant_2 = Participant("tobi", 24, 500)
participant_3 = Participant("Miley", 25, 200)

vickery_auction = VickeryAuction("table", [], 100)
vickery_auction.new_participant(participant_1)
vickery_auction.new_participant(participant_2)
vickery_auction.new_participant(participant_3)

print(vickery_auction.winner())