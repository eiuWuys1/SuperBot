import discord
import asyncio
import random
from discord.ext import commands

intents = discord.Intents.all()

with open("tokens.txt", "r") as f:
    tokens = [line.strip() for line in f if line.strip()]

bots = []

fun_quotes = [
    "Anh hai ơi, mai em dậy trễ, anh nhớ gọi em dậy nha, không có anh là em trễ học á!",
    "Anh là siêu nhân của em, dù có dữ với em cỡ nào thì em vẫn yêu anh nhất nhà!",
    "Anh đi đâu là em nhớ liền đó, về nhớ mua trà sữa cho em chuộc lỗi nha!",
    "Ai cũng nói em nhõng nhẽo với anh, nhưng mà không nhõng nhẽo với anh thì nhõng nhẽo với ai giờ?",
    "Em mà có gì ngon là nghĩ tới anh trước á, thương anh ghê luôn!",
    "Chị ơi, mai em mượn áo nha, áo chị luôn làm em cảm thấy như được ôm bởi chị vậy á!",
    "Chị là phiên bản trưởng thành của em, nên em ráng học chị từng chút luôn á.",
    "Chị lúc nào cũng lo cho em như mẹ nhỏ của em vậy, em thương chị nhiều lắm luôn á!",
    "Chị là người duy nhất em có thể kể mấy chuyện nhảm nhí mà vẫn được nghe đến cuối câu.",
    "Em biết em hay làm chị phiền, nhưng mà có chị để mắng em cũng thấy vui vui á!"
]

gay_responses = [
    "Gay thì sao? Còn hơn thằng dị ứng với kiến thức như mày.",
    "Ủa? Tao gay mà mày vẫn quan tâm tao dữ vậy? Lộ rồi kìa.",
    "Mày chửi tao gay, mà giọng mày còn mềm hơn nước rửa chén pha loãng.",
    "Tao gay, còn mày là sản phẩm lỗi của xã hội dị ứng với LGBT.",
    "Đàn ông đích thực không sợ bị gọi là gay. Còn mày sợ gì vậy?",
    "Bố mày gay nhưng bố không đẻ ra cái lũ đầu buồi như mày.",
    "Tao gay, ít ra còn có gu. Còn mày thì loạn gene với cả não tàn.",
    "Gay mà vẫn khôn hơn mấy đứa sinh ra chỉ để ngồi chửi dạo như mày.",
    "Tao gay? Vậy còn mày? Mày đang ghen tị vì gái lẫn trai đều không ai thèm mày à?",
    "Tao gay, còn mày là cái thứ não phẳng đi bình phẩm người khác vì không ai thèm chơi cùng."
]

stupid_responses = [
    "Tôi ngu? Ừ, nhưng vẫn hơn cái đống não phẳng đang gõ phím như bạn.",
    "Mày chửi tao ngu, mà chính mày đang tranh luận với người mày gọi là ngu. Vậy ai ngu hơn?",
    "Mày nói chuyện như não mày đang chạy thử nghiệm beta vậy á.",
    "Tao tưởng Discord này có filter ngăn loài đầu đất vô mà?",
    "Góp ý mà não không bật là đang tự nhục đó bạn.",
    "Tao ngu mà còn dạy được thằng ngu hơn – mày đó.",
    "Nói chuyện với mày tao thấy tội cho Wi-Fi tao ghê, phải truyền dữ liệu ngu liên tục.",
    "Mày mà là thiên tài thì tao là chúa tể loài người rồi đó con.",
    "Tao không biết nên cười hay khóc vì có đứa còn thua cả trí thông minh của cái bot tao lập trình.",
    "Mày mà thông minh thì mấy cái group toxic như này giải tán lâu rồi."
]

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

async def setup_bot(token):
    bot = commands.Bot(command_prefix="!", intents=intents)
    bots.append(bot)

    def admin_only():
        async def predicate(ctx):
            return ctx.author.guild_permissions.administrator
        return commands.check(predicate)

    @bot.event
    async def on_ready():
        print(f"[+] Bot {bot.user} đã online!")
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="if anyone needs help~ 💫"
        ))

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

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return

        lowered = message.content.lower()
        if "bot gay" in lowered:
            await message.channel.send(random.choice(gay_responses))
        elif "bot ngu" in lowered:
            await message.channel.send(random.choice(stupid_responses))

        if bot.user.mentioned_in(message):
            await message.channel.send(f"{message.author.mention} Em đây!, anh muốn em giúp gì nào?")

        await bot.process_commands(message)

    @bot.command()
    async def fun(ctx):
        await ctx.send(random.choice(fun_quotes))

    @bot.command()
    async def version(ctx):
        await ctx.send("Phiên bản hiện tại: 1.0")

    @bot.command()
    @admin_only()
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

    @bot.command()
    @admin_only()
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

    @bot.command()
    @admin_only()
    async def fix(ctx):
        guild = ctx.guild
        await ctx.send("🔧 Đang xử lý toàn bộ kênh để bật quyền xem lịch sử tin nhắn...")
        for channel in guild.text_channels:
            overwrites = channel.overwrites
            overwrite_changed = False
            for role in guild.roles:
                perms = channel.overwrites_for(role)
                if perms.read_message_history is not True:
                    perms.read_message_history = True
                    overwrites[role] = perms
                    overwrite_changed = True
            if overwrite_changed:
                try:
                    await channel.edit(overwrites=overwrites, reason="Enable Read Message History cho tất cả roles")
                except Exception as e:
                    print(f"[❌] Không thể cập nhật quyền cho {channel.name}: {e}")
        await ctx.send("✅ Đã hoàn tất cập nhật quyền xem lịch sử tin nhắn!")

    @bot.command()
    @admin_only()
    async def fixfull(ctx):
        await ctx.send("⚠️ CẢNH BÁO: Lệnh này sẽ **cấp toàn bộ quyền** cho tất cả roles (trừ @everyone) trong toàn bộ kênh văn bản.\nGõ `yes` trong 10 giây để xác nhận.")

        def check(m): return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() == "yes"
        try:
            await bot.wait_for("message", timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("❌ Hủy bỏ vì không xác nhận.")
            return

        guild = ctx.guild
        await ctx.send("🔧 Đang cập nhật toàn bộ quyền...")

        for channel in guild.text_channels:
            overwrites = channel.overwrites
            overwrite_changed = False
            for role in guild.roles:
                if role.is_default():
                    continue
                perms = discord.PermissionOverwrite()
                for perm_name in discord.Permissions.VALID_FLAGS:
                    setattr(perms, perm_name, True)
                overwrites[role] = perms
                overwrite_changed = True
            if overwrite_changed:
                try:
                    await channel.edit(overwrites=overwrites, reason="Cấp lại toàn bộ quyền cho tất cả roles")
                except Exception as e:
                    print(f"[❌] Lỗi cập nhật kênh {channel.name}: {e}")
        await ctx.send("✅ Đã hoàn tất cập nhật toàn bộ quyền!")

    try:
        await bot.start(token)
    except Exception as e:
        print(f"[-] Lỗi khi khởi động bot với token {token[:10]}...: {e}")

async def main():
    await asyncio.gather(*[setup_bot(token) for token in tokens])

if __name__ == "__main__":
    asyncio.run(main())
