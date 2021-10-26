import { Schema, model } from "mongoose";

interface Booking {
  userId: string;
  genre: string | null;
  phone: string;
  email: string | null;
  nationality: string | null;
  pricePerPerson: number;
  peopleQty: number;
  currentMoney: boolean;
}

const BookingSchema = new Schema<Booking>({
  userId: { type: String, required: true },
  genre: { type: String, default: null },
  phone: { type: String, default: "0000-0000" },
  email: { type: String, default: null },
  nationality: { type: String, default: null },
  pricePerPerson: { type: Number, default: 0 },
  peopleQty: { type: Number, default: 1 },
  currentMoney: { type: Boolean, default: false },
});

const BookingModel = model<Booking>("bookings", BookingSchema);

export default BookingModel;

export {
  Booking
};
