import instaloader

profile_name = input ("Enter Instagram Profile Name: ")
instaloader.Instaloader().download_profile(profile_name, profile_pic_only=True)
print("Done!")
