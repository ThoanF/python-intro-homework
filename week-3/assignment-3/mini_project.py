user_day = input("What day is it? ")
norm_user_day = user_day.strip().lower()
user_time_of_day = input("What is the time of day? (e.g., Morning, Afternoon, Evening) ")
norm_time_of_day = user_time_of_day.strip().lower()

if norm_user_day != "monday" or norm_user_day != "tuesday" or norm_user_day != "wednesday" or norm_user_day != "thursday" or norm_user_day != "friday" or norm_user_day != "saturday" or norm_user_day != "sunday":
    print("Sorry, I don't recongize that day. Try: Monday, Tuesday, Wednesday...")

if norm_user_day == "sunday" or norm_user_day == "saturday" and norm_time_of_day == "morning":
    print("Suggestion: A good weekend begins with a good brunch!")
if norm_user_day == "friday" and norm_time_of_day == "evening":
    print("Suggestion: It's Friday! Friday! Gotta get down on Friday! Time to party!")
if norm_user_day == "monday" or norm_user_day == "tuesday" or norm_user_day == "wednesday" or norm_user_day == "thursday" and norm_time_of_day == "afternoon":
    print("Suggestion: Another day, another dollar. Get working!")

