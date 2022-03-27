import stripe
stripe.api_key = "sk_test_51KhPTvBI1KCMZju3sTZv5Zd6RryOKnmug0gqFBSrlFDP2gC74sKaKHN3Ay0eooD4wJusG9KuchKC7FJzhd360pBB00NdT5zgAD"

stripe.Token.create(
  bank_account={
    "country": "US",
    "currency": "usd",
    "account_holder_name": "Jenny Rosen",
    "account_holder_type": "individual",
    "routing_number": "110000000",
    "account_number": "000123456789",
  },
)
