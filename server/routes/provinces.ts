import express from "express";
import Province from "../models/Province";

const router = express.Router();

// Get all the provinces
router.get("/", async (_, res) => {
  try {
    const provinces = await Province.find();
    res.json(provinces);
  } catch (err) {
    res.json({ message: err });
  }
});

export default router;
