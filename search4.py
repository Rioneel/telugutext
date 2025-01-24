from googleapiclient.discovery import build
import openpyxl

# Replace 'YOUR_API_KEY' with your actual YouTube API key
api_key = "AIzaSyBsU4fxoQSum6YJcSQsu7Wvo7CfIhm4_wE"
youtube = build('youtube', 'v3', developerKey=api_key)

# Function to search for Telugu videos with Creative Commons license
def search_telugu_videos():
    request = youtube.search().list(
        part="snippet",            # Retrieve video snippet (title, description, etc.)
        q="telangana history",     # Search query, modify based on topics
        type="video",              # We want only videos
        videoLicense="creativeCommon",  # Filter for CC-licensed videos
	videoDuration="short",
        maxResults=10,             # Get 10 results (you can increase this number)
        videoCaption="closedCaption"  # Filter videos that have captions availab
    )
    response = request.execute()

    # Create an Excel workbook and add a sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Telugu Videos"

    # Write headers
    sheet['A1'] = 'Video ID'
    sheet['B1'] = 'URL'

    # Save video data into the Excel file
    for i, video in enumerate(response['items'], start=2):
        video_id = video['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        # Write the data to the Excel file
        sheet[f'A{i}'] = video_id
        sheet[f'B{i}'] = video_url

        # Print video details
        print(f"Video ID: {video_id}")
        print(f"Video URL: {video_url}")
        print("-----------------------------")

    # Save the Excel file
    wb.save("telugu_videos2.xlsx")
    print("Video URLs saved to telugu_videos1.xlsx")

# Run the search function
search_telugu_videos()
