sports = ['archery', 'badminton', 'baseball', 'basketball', 'billiards', 'bowling', 'boxing', 'cricket', 'curling', 'cycling', 'darts', 'diving', 'football', 'golf', 'gymnastics', 'handball', 'hockey', 'judo', 'lacrosse', 'martial arts', 'netball', 'polo', 'rugby', 'shooting', 'skating', 'skiing', 'soccer', 'softball', 'squash', 'swimming', 'table tennis', 'tennis', 'track and field', 'triathalon', 'volleyball', 'water polo', 'wrestling']
if 'soccer' in sports:
    print('Soccer is a sport.')
else:
    print('Soccer is not a sport.')

#Check list if empty

toppings = ['mushrooms', 'extra cheese']

if toppings:
    for topping in toppings:
        print('Adding', topping + '.')
    print('Your pizza is ready.')
else:
    print("Are you sure you don't want toppings?")


sports = ['archery', 'badminton', 'baseball', 'basketball', 'billiards', 'bowling', 'boxing', 'cricket', 'curling', 'cycling', 'darts', 'diving', 'football', 'golf', 'gymnastics', 'handball', 'hockey', 'judo', 'lacrosse', 'martial arts', 'netball', 'polo', 'rugby', 'shooting', 'skating', 'skiing', 'soccer', 'softball', 'squash', 'swimming', 'table tennis', 'tennis', 'track and field', 'triathalon', 'volleyball', 'water polo', 'wrestling']
activities = ['soccer', 'bowling', 'football', 'video games']

for activity in activities:
    if activity in sports:
        print('Would you like to play', activity + '?')
    else:
        print("Sorry, we don't offer", activity + '.')