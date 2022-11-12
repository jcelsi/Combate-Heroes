"""
Module with the function for sending a mail with the battle results.
"""
import requests

def send_simple_message(recipient, log):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox8b27dcdc5c8342bbaf3a1b20d6bbca16.mailgun.org/messages",
		auth=("api", "38140b74b99d3a14d021b4b9f5461b52-48c092ba-fa3d82ba"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox8b27dcdc5c8342bbaf3a1b20d6bbca16.mailgun.org>",
			"to": recipient,
			"subject": "Hero Battle Log",
   			"html":f"<html>{log}</html>"})
