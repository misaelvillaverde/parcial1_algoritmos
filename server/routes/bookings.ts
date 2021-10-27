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

// Get bookings by userId
router.get("/:id", async (req, res) => {
  try {
    const booking = await Booking.find({ userId: req.params.id });
    res.json(booking);
  } catch (err) {
    res.json({ message: err });
  }
});

// Post a booking
router.post("/", async (req, res) => {
  const {
    userId,
    name,
    genre,
    phone,
    email,
    nationality,
    peopleQty,
    currentDebt,
    placeName,
    totalCost,
    payment,
  } = req.body;
  const booking = new Booking({
    userId,
    name,
    genre,
    phone,
    email,
    nationality,
    peopleQty,
    currentDebt,
    placeName,
    totalCost,
    payment,
  });
  try {
    const savedBooking = await booking.save();
    res.json(savedBooking);
  } catch (err) {
    res.json({ message: err });
  }
});

router.delete("/:id", async (req, res) => {
  try {
    const deletedBooking = await Booking.deleteOne({ _id: req.params.id });
    res.json(deletedBooking);
  } catch (err) {
    res.json({ message: err });
  }
});

export default router;
