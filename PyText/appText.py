from twilio.rest import Client
account_SID = "whatever it is here"
auth_token = "whatever"
client = Client(account_SID, auth_token)

client.messages.create(
    to="their number",
    from_="twilio number",
    body="Hello"
)

print(client)