import json

def load_ytd(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    eq_idx = content.find("=")

    if eq_idx == -1:
        raise ValueError(f"Invalid format in {path}")

    json_str = content[eq_idx + 1:].strip()

    if json_str.endswith(";"):
        json_str = json_str[:-1].strip()

    return json.loads(json_str)




# Load the tweets
tweets = load_ytd("tweets.js")

# Counters
total_tweets = 0
total_retweets = 0

# Dictionary to count tweets on each day
daily_counts = {}

# Go through every record
for item in tweets:

    # Extract the tweet dictionary
    tweet = item["tweet"]

    # Get the timestamp and text
    date = tweet["created_at"]
    text = tweet["full_text"]

    # Check whether the tweet belongs to January 2020
    if date[4:7] == "Jan" and date[-4:] == "2020":

        # Part (a): Count total tweets
        total_tweets += 1

        # Part (b): Count retweets
        if text.startswith("RT @"):
            total_retweets += 1

        # Extract the day from the timestamp
        day = int(date[8:10])

        # Count tweets for each day
        if day in daily_counts:
            daily_counts[day] += 1
        else:
            daily_counts[day] = 1

# Part (c): Find the busiest day
busiest_day = 0
maximum = 0

for day in daily_counts:
    if daily_counts[day] > maximum:
        maximum = daily_counts[day]
        busiest_day = day

# Print answers
print("Q1(a) Total January tweets:", total_tweets)
print("Q1(b) January retweets:", total_retweets)
print("Q1(c) Busiest day:", busiest_day)
print("Tweets on that day:", maximum)

attributed = load_ytd(
    "ad-mobile-conversions-attributed.js"
)

unattributed = load_ytd(
    "ad-mobile-conversions-unattributed.js"
)

print("Attributed data type:", type(attributed))
print("Unattributed data type:", type(unattributed))

if isinstance(attributed, list) and attributed:
    print("Attributed fields:", list(attributed[0].keys()))

if isinstance(unattributed, list) and unattributed:
    print("Unattributed fields:", list(unattributed[0].keys()))


print("Attributed ad fields:")
print(list(attributed[0]["ad"].keys()))

print("Unattributed ad fields:")
print(list(unattributed[0]["ad"].keys()))


print("Attributed adsUserData fields:")
print(list(attributed[0]["ad"]["adsUserData"].keys()))

print("Unattributed adsUserData fields:")
print(list(unattributed[0]["ad"]["adsUserData"].keys()))


# Inspect the conversion collection types
attributed_conversions = attributed[0]["ad"]["adsUserData"]["attributedMobileAppConversions"]

unattributed_conversions = unattributed[0]["ad"]["adsUserData"]["unattributedMobileAppConversions"]

print("Attributed conversions type:", type(attributed_conversions))
print("Unattributed conversions type:", type(unattributed_conversions))

if isinstance(attributed_conversions, list) and attributed_conversions:
    print("Attributed conversion fields:", list(attributed_conversions[0].keys()))

if isinstance(unattributed_conversions, list) and unattributed_conversions:
    print("Unattributed conversion fields:", list(unattributed_conversions[0].keys()))

if isinstance(attributed_conversions, dict):
    print("Attributed conversion keys:", list(attributed_conversions.keys()))

if isinstance(unattributed_conversions, dict):
    print("Unattributed conversion keys:", list(unattributed_conversions.keys()))


# Get the conversions from both files
attributed_conversions = attributed[0]["ad"]["adsUserData"]["attributedMobileAppConversions"]["conversions"]

unattributed_conversions = unattributed[0]["ad"]["adsUserData"]["unattributedMobileAppConversions"]["conversions"]

print("Attributed conversions type:", type(attributed_conversions))
print("Unattributed conversions type:", type(unattributed_conversions))

if isinstance(attributed_conversions, list):
    print("Attributed number of records:", len(attributed_conversions))
    if attributed_conversions:
        print("Attributed field names:", list(attributed_conversions[0].keys()))

if isinstance(unattributed_conversions, list):
    print("Unattributed number of records:", len(unattributed_conversions))
    if unattributed_conversions:
        print("Unattributed field names:", list(unattributed_conversions[0].keys()))

if isinstance(attributed_conversions, dict):
    print("Attributed keys:", list(attributed_conversions.keys()))

if isinstance(unattributed_conversions, dict):
    print("Unattributed keys:", list(unattributed_conversions.keys()))

# QUESTION 2

# Extract conversion records from both files
attributed_conversions = attributed[0]["ad"]["adsUserData"]["attributedMobileAppConversions"]["conversions"]

unattributed_conversions = unattributed[0]["ad"]["adsUserData"]["unattributedMobileAppConversions"]["conversions"]

# Counters
total_events = 0
unattributed_events = 0

# Store dates of matching events
event_dates = []

# Process attributed events
for event in attributed_conversions:
    if event["applicationName"] == "INDmoney - Stock, Mutual Fund":
        total_events += 1
        event_dates.append(event["conversionTime"])

# Process unattributed events
for event in unattributed_conversions:
    if event["applicationName"] == "INDmoney - Stock, Mutual Fund":
        total_events += 1
        unattributed_events += 1
        event_dates.append(event["conversionTime"])

# Find the earliest event date
earliest_date = None

for date in event_dates:
    if earliest_date is None or date < earliest_date:
        earliest_date = date

# Print answers
print("\nQ2(a) Total INDMoney events:", total_events)
print("Q2(b) Unattributed INDMoney events:", unattributed_events)
print("Q2(c) Earliest event date:", earliest_date)
