from igramscraper.instagram import Instagram
# from context import Instagram
from time import sleep

instagram = Instagram()

# authentication supported
instagram.with_credentials('armanroutray', '88ii((88')
instagram.login()
detail = instagram.get_following('itz_me_sweta26', delayed_time_max=6.0, delayed_time_min=2.0 ,delayed=True)
# medias = instagram.get_medias('itz_me_sweta26', 30)
# print(medias)
# media = medias[10]

# print(media)
# account = media.owner
print(detail)












# --------------------------------
# Available fields
# print('Account info:')
# print('Id: ', account.identifier)
# print('Username: ', account.username)
# print('Full name: ', account.full_name)
# print('Biography: ', account.biography)
# print('Profile pic url: ', account.get_profile_picture_url())
# print('External Url: ', account.external_url)
# print('Number of published posts: ', account.media_count)
# print('Number of followers: ', account.followed_by_count)
# print('Number of follows: ', account.follows_count)
# print('Is private: ', account.is_private)
# print('Is verified: ', account.is_verified)

# or simply for printing use 
# print(account)