import asyncio

from telethon import events

from userbot.utils import admin_cmd, register

# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# ===========================================


A = (
    "`▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `\n"
    "`████▌▄▌▄▐▐▌█████ `\n"
    "`████▌▄▌▄▐▐▌▀████ `\n"
    "`▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `\n"
)

B = (
    "`╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `\n"
    "`╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `\n"
    "`╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `\n"
    "`╱┗━━━┛╰━━━╯┗━━━┛╱ `\n"
)

C = (
    "\n......................................../´¯/) "
    "\n......................................,/¯../ "
    "\n...................................../..../ "
    "\n..................................../´.¯/"
    "\n..................................../´¯/"
    "\n..................................,/¯../ "
    "\n................................../..../ "
    "\n................................./´¯./"
    "\n................................/´¯./"
    "\n..............................,/¯../ "
    "\n............................./..../ "
    "\n............................/´¯/"
    "\n........................../´¯./"
    "\n........................,/¯../ "
    "\n......................./..../ "
    "\n....................../´¯/"
    "\n....................,/¯../ "
    "\n.................../..../ "
    "\n............./´¯/'...'/´¯¯`·¸ "
    "\n........../'/.../..../......./¨¯\ "
    "\n........('(...´...´.... ¯~/'...') "
    "\n.........\.................'...../ "
    "\n..........''...\.......... _.·´ "
    "\n............\..............( "
    "\n..............\.............\..."
)


@register(outgoing=True, pattern="^.lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
            "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
            "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `"
        )


@register(outgoing=True, pattern="^.nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n(\_/)`"
            "`\n(•_•)`"
            "`\n >🌹 *`"
            "`\n                    `"
            "`\n(\_/)`"
            "`\n(•_•)`"
            "`\n🌹<\ *`"
        )


@register(outgoing=True, pattern="^.hallo$")
async def gtfo(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n█████████`"
            "`\n█▄█████▄█`"
            "`\n█▼▼▼▼▼`"
            "`\n█  Hello Man`"
            "`\n█▲▲▲▲▲`"
            "`\n█████████`"
            "`\n ██   ██`"
        )


@register(outgoing=True, pattern="^.ml(?: |$)(.*)")
async def gtfo(e):
    message = e.pattern_match.group(1)
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n█████████`"
            "`\n█▄█████▄█`"
            "`\n█▼▼▼▼▼`"
            f"`\n█  {message}`"
            "`\n█▲▲▲▲▲`"
            "`\n█████████`"
            "`\n ██   ██`"
        )


@register(outgoing=True, pattern="^.taco$")
async def taco(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n{\__/}" "\n(●_●)" "\n( >🌮 Want a taco?")


@register(outgoing=True, pattern="^.paw$")
async def paw(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`(=ↀωↀ=)")


@register(outgoing=True, pattern="^.tf$")
async def tf(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@register(outgoing=True, pattern="^.gay$")
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
            "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
            "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈U GAY`"
            "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
        )


@register(outgoing=True, pattern="^.bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
            "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `"
        )


@register(outgoing=True, pattern="^.hai$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HELLO!┊😀`"
            "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HELLO!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
            "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`"
        )


@register(outgoing=True, pattern="^.nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
            "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
            "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
            "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
            "`\n┗━━┻━┛`"
        )


@register(outgoing=True, pattern="^.sayhi$")
async def shalom(e):
    await e.edit(
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛🔷🔷🔷🔷️🔷🔷🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷💛💛️💛💛💛🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷️🔷💛"
        "\n💛🔷💛💛💛💛️💛🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
    )


@register(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.edit(titid)


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "muth":

        await event.edit(input_str)

        animation_chars = [
            "8✊️===D",
            "8=✊️==D",
            "8==✊️=D",
            "8===✊️D",
            "8==✊️=D",
            "8=✊️==D",
            "8✊️===D",
            "8===✊️D💦",
            "8==✊️=D💦💦",
            "8=✊️==D💦💦💦",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])


@borg.on(admin_cmd(pattern=r"fail"))
async def kakashi(fail):
    await fail.edit(A)


@borg.on(admin_cmd(pattern=r"lul"))
async def kakashi(lol):
    await lol.edit(B)


@borg.on(admin_cmd(pattern=r"mf"))
async def kakashi(mf):
    await mf.edit(C)
