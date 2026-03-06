from instabot import Bot
bot  = Bot()
bot.login(username = "your_name",password = "your_password")
bot.follow('')
bot.upload_photo("img",caption="comments")
bot.unfollow("")
bot.send_message("your_message",['id'])
followers = bot.get_user_followers("username")
for follower in followers:
    print(bot.get_userinfo(follower))