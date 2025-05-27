# bot.py
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルから環境変数を読み込む
TOKEN = os.getenv("DISCORD_TOKEN")  # .envファイルからトークンを取得
if not TOKEN:
    raise ValueError("DISCORD_TOKENが設定されていません。")

intents = discord.Intents.default()
intents.message_content = True  # メッセージ取得を有効にする

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot接続成功: {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！")


@bot.command()
async def shutdown(ctx):
    await ctx.send("Botを終了します...")
    await bot.close()


# 自分のトークンを貼る
bot.run(TOKEN)
