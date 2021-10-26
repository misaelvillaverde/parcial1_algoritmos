import express from "express";
import Booking from "../models/Booking";

const router = express.Router();

// Get all bookings
router.get("/", async (_, res) => {
  try {
    const bookings = await Booking.find();
    res.json(bookings);
  } catch (err) {
    res.json({ message: err });
  }
});

// Post a booking
router.post("/", async (req, res) => {
  const { userId, genre, phone, email, nationality, pricePerPerson, peopleQty, currentMoney } = req.body;
  const booking = new Booking({
    userId,
    genre,
    phone,
    email,
    nationality,
    pricePerPerson,
    peopleQty,
    currentMoney
  });
  try {
    const savedBooking = await booking.save();
    res.json(savedBooking);
  } catch (err) {
    res.json({ message: err });
  }
});

// Update a booking
router.patch("/:id", async(req, res) => {
  const { userId, genre, phone, email, nationality, pricePerPerson, peopleQty, currentMoney } = req.body;
  const booking = new Booking({
    userId,
    genre,
    phone,
    email,
    nationality,
    pricePerPerson,
    peopleQty,
    currentMoney
  });

  try {
    const updatedBooking = await Booking.updateOne({_id: req.params.id}, booking);
    res.json(updatedBooking);
  } catch (err) {
    res.json({ message: err });
  }
});

export default router;
