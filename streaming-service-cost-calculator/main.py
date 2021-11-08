streaming_records = ["00:02:05,123-32-4535","00:01:23,321-46-9871","00:35:18,528-28-7659","00:03:02,123-32-4535"]

def map_records_in_dictionary(input_records):
    dictionary = {}
    for record in input_records:
        [duration,identifier] = record.split(',')
        seconds = map_duration_to_seconds(duration)
        if (identifier not in dictionary):
            dictionary[identifier]=seconds
        else:
            dictionary[identifier]+=seconds
    return dictionary

def map_duration_to_seconds(duration):
    [hours_str,minutes_str,seconds_str] = duration.split(':')
    seconds=int(seconds_str)+int(minutes_str)*60+int(hours_str)*60*60
    return seconds

def find_longest_duration_record_from_dictionary(dictionary):
    longest_duration_identifier=''
    longest_duration_seconds=0
    for identifier, seconds in dictionary.items():
        if (seconds > longest_duration_seconds):
            longest_duration_identifier = identifier
            longest_duration_seconds = seconds
    return longest_duration_identifier

def calculate_cost(seconds):
    minutes=seconds/60
    if (minutes< 3):
        return 5 * seconds
    return 200 * minutes

# Step 1: Map the list of track records into a dictioary with their respectice total duration in seconds.
track_time_dictionary = map_records_in_dictionary(streaming_records)

# Step 2: Find the song with the longest duration played.
longest_record_identifier=find_longest_duration_record_from_dictionary(track_time_dictionary)

# Step 3: Iterate through the dictionary and calculate all the costs.
total_cost=0
for identifier, seconds in track_time_dictionary.items():
    track_cost = calculate_cost(seconds)
    if (identifier == longest_record_identifier):
        track_cost*=0.5
    total_cost+=track_cost

print('\nThe user has the track records:')
print(streaming_records)
print('\nThe total cost for ther user is $'+ str(total_cost/100)+"\n")