const router = require("express").Router();

const stripe = require("stripe")("SECRET_KEY");

const { getCartItems } = require("./store-service");

router.post("/", async (req, res) => {
  const { userId } = req;

  const cartItems = await getCartItems(userId);

  const paymentIntent = await stripe.paymentIntents.create({
    amount: cartItems.amount * 100,
    currency: "inr",
    customer: "{{CUSTOMER_ID}}",
  });

  return res.json({
    checkoutSecret: paymentIntent.client_secret,
    ...cartItems,
  });
});

module.exports = router;
