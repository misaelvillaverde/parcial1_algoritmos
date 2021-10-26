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

// Get a province by name
router.get("/:name", async (req, res) => {
  try {
    const province = await Province.findOne({ name: req.params.name });
    res.json(province);
  } catch (err) {
    res.json({ message: err });
  }
});

export default router;
