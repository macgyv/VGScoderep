import stripe
stripe.api_key = "sk_test_51KhPTvBI1KCMZju3sTZv5Zd6RryOKnmug0gqFBSrlFDP2gC74sKaKHN3Ay0eooD4wJusG9KuchKC7FJzhd360pBB00NdT5zgAD"

stripe.Token.create(
  card={
    "number": "4242424242424242",
    "exp_month": 3,
    "exp_year": 2023,
    "cvc": "314",
  },
)
