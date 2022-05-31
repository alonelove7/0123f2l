import os


class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    Token = os.environ.get("BOT_TOKEN")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID"))
    Start_Message = os.environ.get("Start_Message")
    Bot_Channel = os.environ.get("Bot_Channel_UserName")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://{App_Name}.herokuapp.com/"
    Download_Folder = "Files"
    Dev_Channel = "shadow_bots"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = 3  # How many parts to download from telegram before client request them
    Separate_Time = 4  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = 60  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = 1  # How many links user can update them to fast links at the same time


class Strings:
    start = Config.Start_Message
    dl_link = "⚡️لینک دانلود⚡️"
    st_link = "💥پخش آنلاین💥"
    generating_link = "♻️در حال تبدیل فایل به لینک...♻️"
    bot_channel = "☣️ورود به کانال☣️"
    dev_channel = "*/**\*"
    fast = "💠لینک دانلود بروزرسانی شد💠"
    update_link = "🌀بروزرسانی لینک دانلود🌀"
    update_limited = (f"⭕️شما فقط قادر به بروزرسانی {Config.Max_Fast_Processes} لینک هستید⭕️"
                      "❗️صبر کنید تا بروزرسانی قبلی به پایان برسد❗️")
    re_update_link = "🔄در حال بروزرسانی لینک...🔄"
    already_updated = "❗️این لینک قبلا بروزرسانی شده است❗️"
    wait_update = "🔄در حال بروزرسانی لینک...🔄"
    wait = "🔅صبر کنید...🔅"
    progress = "🔅صبر کنید...🔅"
    file_not_found = "📛فایل شما در دیتابیس یافت نشد، مجددا ارسال کنید♻️"
    delete_manually_button = "〽️شما نمیتوانید این فایل را حذف کنید〽️"
    delete_forbidden = "🔆ربات تنها فایل هایی که کمتر از 48 ساعت از ارسال آن گذشته میتواند حذف کند🔆"
    force_join = "📛 برای حمایت از ما و همچنان ربات ابتدا در کانال ما عضو شوید.\n\n✅ پس از عضویت وارد ربات شده و دستور /start را ارسال کنید."
