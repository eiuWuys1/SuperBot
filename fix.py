import discord
from discord.ext import commands

# Load token từ file
with open("tokens.txt", "r") as f:
    TOKEN = f.read().strip()

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập với tên: {bot.user}")
    for guild in bot.guilds:
        print(f"Đang xử lý máy chủ: {guild.name}")
        for channel in guild.text_channels:
            print(f"  ➤ Kênh: {channel.name}")
            overwrite_changed = False
            overwrites = channel.overwrites
            for role in guild.roles:
                perms = channel.overwrites_for(role)
                if perms.read_message_history is not True:
                    perms.read_message_history = True
                    overwrites[role] = perms
                    overwrite_changed = True
            if overwrite_changed:
                try:
                    await channel.edit(overwrites=overwrites, reason="Enable Read Message History cho tất cả roles")
                    print(f"    ✅ Đã cập nhật quyền trong kênh {channel.name}")
                except Exception as e:
                    print(f"    ❌ Không thể cập nhật quyền cho kênh {channel.name}: {e}")

bot.run(TOKEN)
