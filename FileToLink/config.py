import os


class Config:
    API_ID = int(os.environ.get("API_ID", "392800"))
    API_HASH = os.environ.get("API_HASH", "f7f4316dac3b4959687b46860b44c265")
    Token = os.environ.get("BOT_TOKEN", "2045343811:AAH2YutndTCYokHpkk_rn83CeAivJSMIOa0")
    Session = os.environ.get("Session_String")
    if Session is None or Session == "":
        Session = ":memory:"
    App_Name = os.environ.get("APP_NAME")
    Port = int(os.environ.get("PORT", "80"))
    Archive_Channel_ID = int(os.environ.get("ARCHIVE_CHANNEL_ID", "-1001775795211"))
    Start_Message = os.environ.get("Start_Message", "💥برای استفاده از ربات کافی است فایل خود را ارسال کرده و سپس لینک آن را دریافت کنید.")
    Bot_Channel = os.environ.get("Bot_Channel_UserName", "King_network7")
    if Bot_Channel and Bot_Channel.startswith("@"):
        Bot_Channel = Bot_Channel[1:]
    elif Bot_Channel == "":
        Bot_Channel = None

    Link_Root = f"https://d3.kimo.vip/"
    Download_Folder = "/root/1"
    Dev_Channel = "King_network7"
    Bot_UserName = None  # The bot will set it after starting
    Part_size = 10 * 1024 * 1024  # (10MB) For Pyrogram
    Buffer_Size = 512 * 1024  # For Quart
    Pre_Dl = int(getenv("Pre_Dl", "8"))  # How many parts to download from telegram before client request them
    Separate_Time = int(getenv("Separate_Time", "5"))  # (seconds)  wait time between messages if user send more than one
    Sleep_Threshold = int(getenv("Sleep_Threshold", "60"))  # (Seconds) sleep threshold for flood wait exceptions
    Max_Fast_Processes = int(getenv("Max_Fast_Processes", "0"))  # How many links user can update them to fast links at the same time


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
