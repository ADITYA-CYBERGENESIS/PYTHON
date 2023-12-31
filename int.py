from instagram_private_api import Client, ClientCompatPatch

# Instagram account credentials
username = 'EARN.CREDITX_'
password = 'INSTAEarn11@22'

# Log in to Instagram
api = Client(username, password)
api.login()

# Get the list of accounts you follow
rank_token = Client.generate_uuid()
following = api.user_following(api.authenticated_user_id, rank_token=rank_token)

# Iterate over each account
reels_links = []
for user in following['users']:
    # Get user's Reels videos
    reels_videos = []
    results = api.user_feed(user['pk'])
    reels_videos.extend([item for item in results.get('items') if item.get('media_type') == 2])

    while results.get('more_available'):
        next_max_id = results.get('next_max_id')
        results = api.user_feed(user['pk'], max_id=next_max_id)
        reels_videos.extend([item for item in results.get('items') if item.get('media_type') == 2])

    # Extract links from Reels videos
    for video in reels_videos:
        reels_links.append(video['video_versions'][0]['url'])

# Create or open the file to write the links
file_path = r"C:\Users\adity\Music\hello\input.txt"
with open(file_path, 'a') as file:
    # Write the links to the file
    for link in reels_links:
        file.write(link + '\n')

num_links = len(reels_links)
print(f"{num_links} link(s) have been appended to {file_path}.")
