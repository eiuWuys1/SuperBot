
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.all()

with open("tokens.txt", "r") as f:
    tokens = [line.strip() for line in f if line.strip()]

bots = []

# ======= PHẦN HỖ TRỢ QUYỀN =======
def generate_mode_overwrite(mode: str) -> discord.PermissionOverwrite:
    allowed = []

    if mode == "1":
        allowed = ["view_channel", "add_reactions"]
    elif mode == "2":
        allowed = ["view_channel", "send_messages", "manage_messages", "add_reactions", "attach_files"]
    elif mode == "3":
        return discord.PermissionOverwrite(view_channel=False)

    overwrite = discord.PermissionOverwrite()
    for perm in discord.Permissions.VALID_FLAGS:
        setattr(overwrite, perm, perm in allowed)
    return overwrite

DENY_ALL = discord.PermissionOverwrite(
    view_channel=False, send_messages=False,
    manage_messages=False, add_reactions=False, attach_files=False
)

# ======= SETUP BOT =======
async def setup_bot(token):
    bot = commands.Bot(command_prefix="!", intents=intents)
    bots.append(bot)

    # ==== ON READY ====
    @bot.event
    async def on_ready():
        print(f"[+] Bot {bot.user} đã online!")

        # Set status
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="if anyone needs help~ 💫"
        ))

        # Tự động gửi tin nhắn mỗi 30 phút
        async def auto_chat():
            await bot.wait_until_ready()
            while not bot.is_closed():
                for guild in bot.guilds:
                    for channel in guild.text_channels:
                        if channel.permissions_for(guild.me).send_messages:
                            try:
                                await channel.send("Mình đang online nè 👀")
                                break
                            except:
                                pass
                            break
                await asyncio.sleep(1800)

        bot.loop.create_task(auto_chat())

    # ==== PHẢN HỒI KHI BỊ MENTION ====
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if bot.user.mentioned_in(message):
            await message.channel.send(f"{message.author.mention} Em đây!, anh muốn em giúp gì nào?")
        await bot.process_commands(message)

    # ==== LỆNH !chat ====
    @bot.command()
    async def chat(ctx, chanel_input: str = None, *, message: str = None):
        if not chanel_input or not message:
            await ctx.send("❗ Cú pháp: `!chat <id kênh hoặc #kênh> <nội dung>`")
            return

        target_channel = None
        if ctx.message.channel_mentions:
            target_channel = ctx.message.channel_mentions[0]
        else:
            try:
                channel_id = int(chanel_input)
                target_channel = ctx.guild.get_channel(channel_id)
            except:
                pass

        if not target_channel:
            await ctx.send("⚠️ Không tìm thấy kênh.")
            return

        try:
            await target_channel.send(message)
            await ctx.send(f"✅ Đã gửi tin nhắn tới `{target_channel.name}`.")
        except Exception as e:
            await ctx.send(f"⚠️ Lỗi gửi tin nhắn: {e}")

    # ==== LỆNH !setup ====
    @bot.command()
    async def setup(ctx):
        guild = ctx.guild
        author = ctx.author
        roles = [r for r in guild.roles if r.color.value != 0 and not r.is_default()]
        channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]

        role_list = "\n".join([f"{i}: {r.name}" for i, r in enumerate(roles)])
        await ctx.send(f"**Danh sách Role:**\n{role_list}\n\nGõ số role cách nhau bằng dấu phẩy (vd: `0,2,3`)")

        def check_msg(m): return m.author == author and m.channel == ctx.channel
        try:
            msg_roles = await bot.wait_for("message", timeout=60.0, check=check_msg)
            selected_roles = [roles[int(i.strip())] for i in msg_roles.content.split(",") if i.strip().isdigit()]
        except:
            await ctx.send("⛔ Không nhập hợp lệ hoặc hết thời gian.")
            return

        chan_list = "\n".join([f"{i}: {c.name}" for i, c in enumerate(channels)])
        await ctx.send(f"**Danh sách Channel:**\n{chan_list}\n\nGõ số kênh cách nhau bằng dấu phẩy (vd: `0,1,3`)")

        try:
            msg_chans = await bot.wait_for("message", timeout=60.0, check=check_msg)
            selected_channels = [channels[int(i.strip())] for i in msg_chans.content.split(",") if i.strip().isdigit()]
        except:
            await ctx.send("⛔ Không nhập hợp lệ hoặc hết thời gian.")
            return

        await ctx.send("Chọn mode:\n`1` - Kênh Thông Báo\n`2` - Kênh Chat\n`3` - Ẩn Kênh\nNhập số:")
        try:
            msg_mode = await bot.wait_for("message", timeout=30.0, check=check_msg)
            mode = msg_mode.content.strip()
            perm = generate_mode_overwrite(mode)
        except:
            await ctx.send("⛔ Không nhập hợp lệ hoặc hết thời gian.")
            return

        success = 0
        for channel in selected_channels:
            try:
                for role in selected_roles:
                    await channel.set_permissions(role, overwrite=perm)
                await channel.set_permissions(guild.default_role, overwrite=DENY_ALL)
                success += 1
            except Exception as e:
                await ctx.send(f"⚠️ Lỗi tại `{channel.name}`: {e}")

        await ctx.send(f"✅ Hoàn tất! Đã chỉnh quyền cho `{success}` kênh.")

    # ==== LỆNH !delete ====
    @bot.command()
    async def delete(ctx):
        guild = ctx.guild
        author = ctx.author

        if ctx.message.channel_mentions:
            target_channel = ctx.message.channel_mentions[0]
        else:
            text_channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]
            chan_list = "\n".join([f"{i}: {c.name}" for i, c in enumerate(text_channels)])
            await ctx.send(f"**Danh sách Channel:**\n{chan_list}\n\nNhập số kênh muốn xóa tin nhắn:")

            def check_msg(m): return m.author == author and m.channel == ctx.channel
            try:
                msg = await bot.wait_for("message", timeout=30.0, check=check_msg)
                index = int(msg.content.strip())
                target_channel = text_channels[index]
            except:
                await ctx.send("⛔ Không hợp lệ hoặc hết thời gian.")
                return

        await ctx.send(f"🔄 Đang xóa tất cả tin nhắn trong `{target_channel.name}`...")
        try:
            deleted = await target_channel.purge(limit=None)
            await ctx.send(f"✅ Đã xóa `{len(deleted)}` tin nhắn trong `{target_channel.name}`.")
        except Exception as e:
            await ctx.send(f"⚠️ Lỗi khi xóa: {e}")

    try:
        await bot.start(token)
    except Exception as e:
        print(f"[-] Lỗi khi khởi động bot với token {token[:10]}...: {e}")

# ======= MAIN =======
async def main():
    await asyncio.gather(*[setup_bot(token) for token in tokens])

if __name__ == "__main__":
    asyncio.run(main())
