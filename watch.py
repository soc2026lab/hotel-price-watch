import requests
import yaml

with open("config.yml") as handle:
    CONFIG = yaml.safe_load(handle)


def notify(text):
    bot = CONFIG["telegram"]
    requests.post("https://api.telegram.org/bot" + bot["bot_token"] + "/sendMessage", data={"chat_id": bot["chat_id"], "text": text}, timeout=10)


if __name__ == "__main__":
    notify("Checked " + str(len(CONFIG["targets"])) + " hotel sites")
