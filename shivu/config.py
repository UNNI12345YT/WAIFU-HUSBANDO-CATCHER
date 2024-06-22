class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6171681404"
    sudo_users = "6171681404"
    GROUP_ID = -1002110035934
    TOKEN = "7478405221:AAHh-mBrzPFpx0FNN1N8J8FDj8KrcY_jMvY"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "HAPPY_SUPPORT_GRP"
    UPDATE_CHAT = "HAPPY_SUPPORT_GRP"
    BOT_USERNAME = "Unni_secure_bot"
    CHARA_CHANNEL_ID = "-1002237242985"
    api_id = 27408015
    api_hash = "2f07e7c921c8d2b982df12d65a46ca46"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
