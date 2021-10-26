import express from "express";
import { connect } from "mongoose";
import cors from "cors";

import provincesRouter from "./routes/provinces";
import bookingsRouter from "./routes/bookings";

const app = express();

app.use(cors());
app.use(express.json());

app.use("/provinces", provincesRouter);
app.use("/bookings", bookingsRouter);

app.get("/", (_, res) => {
  res.send("Parcial 1 - ADA - 🦀");
});

connect(
  "mongodb+srv://boroko:1234@provincias.0vbb7.mongodb.net/Agencia_de_Turismo?retryWrites=true&w=majority",
  () => console.log("Connected to DB")
);

const port = process.env.PORT || 5000;
app.listen(port, () => console.log(`Listening on port ${port}`));
